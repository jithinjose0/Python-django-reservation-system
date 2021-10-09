from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import ugettext as _
from django.contrib import messages
def travelsignup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print('successssssss')
            return redirect('busregister')
    else:
        form=RegisterForm()
    return render(request,'travel/travelsignup.html',{'form':form})
def travelsignin(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        password_r = request.POST.get('password')
        user = authenticate(request, username=name_r, password=password_r)
        if user:
            login(request, user)
            return redirect('busdash')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'travel/travelsignin.html', context)
    else:
        context["error"] = "You are not logged in"
        return render(request, 'travel/travelsignin.html', context)
def travelsignout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'travel/travelsignin.html', context)
def bus_register(request):
    if request.method == 'POST':
        form = travelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print('sucessssss')
            return render(request,'travel/wait.html')
    else:
        form=travelForm()
    return render(request,'travel/busregister.html',{'form':form})
@login_required(login_url='signin')
def findbus(request):
    context = {}
    if request.method == 'POST':
        source_r = request.POST.get('source')
        dest_r = request.POST.get('dest')
        time_r=request.POST.get('time1')
        bus_list = Bus.objects.filter(source=source_r, dest=dest_r,time1=time_r).filter(status=True)
        if bus_list:
            return render(request, 'travel/list.html', {'bus_list':bus_list})
        else:
            context["error"] = "Sorry no buses available"
            return render(request, 'travel/findbus.html', context)
    else:
        return render(request, 'travel/findbus.html')
@login_required(login_url='signin')
def reserve_seat(request, id):
    try:
        bus_id = Bus.objects.get(pk=id)
    except Bus.DoesNotExist:
        raise Http404("Page Does Not Exist.") 
    context = {'bus_id':bus_id}
    return render(request,'travel/seat.html',context)
@login_required(login_url='signin')
def bookings(request):
    if request.method == 'POST':
        seats_r = int(request.POST.get('no_seats'))
        date_r = str(request.POST.get('date'))
        id_r = request.POST.get('bus_id')
        bus = Bus.objects.get(id=id_r)
        if bus:
            if bus.Total_seats > int(seats_r):
                name_r = bus.bus_name
                cost = int(seats_r) * bus.price
                source_r = bus.source
                dest_r = bus.dest
                time_r = bus.time1
                owner_r=bus.ownername
                username_r = request.user.username
                email_r = request.user.email
                userid_r = request.user.id
                #rem_r = bus.Total_seats - seats_r
                #Bus.objects.filter(id=bus_id).update(rem=rem_r)
                book = BusBook.objects.create(name=username_r, email=email_r, userid=userid_r,ownername=owner_r, bus_name=name_r,
                                           source=source_r, busid=id_r,
                                           dest=dest_r, price=cost, nos=seats_r, date=date_r, time=time_r,
                                           status='BOOKED')
                print('------------book id-----------', book.id)
                book.save()
                return render(request, 'travel/bookings.html', locals())
            else:
                #context["error"] = "Sorry select fewer number of seats"
                return render(request, 'travel/findbus.html', )
@login_required(login_url='travelsignin')
def busbooked(request,new={}):
    context = {}
    owner=request.user.first_name
    booked_list = BusBook.objects.filter(ownername=owner)
    if booked_list:
        return render(request, 'travel/booklist.html', locals())
    else:
        context["error"] = "Sorry no  booked"
        return render(request, 'travel/sorry.html', context)
@login_required(login_url='travelsignin')
def dashboard(request):
    owner=request.user.first_name
    book_list = BusBook.objects.filter(ownername=owner)
    x=book_list.count()
    if x==0:
        return render(request,'travel/sorry.html')
    else:
        return render(request,'base/bus_dash.html',{'x':x})
@login_required(login_url='travelsignin')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('Your password was successfully updated!'))
            return redirect('travelsignin')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'travel/change_password.html', {
        'form': form
    })
@login_required(login_url='travelsignin')
def prof(request):
    p = request.user
    return render(request,'travel/profile.html',{'p':p})
@login_required(login_url='travelsignin')
def edit(request,new={}):
    owner=request.user.first_name
    update = BusBook.objects.filter(ownername=owner)
    form =travelForm(request.POST,request.FILES)
    if form.is_valid():
        form.save(commit=True)
        return redirect('busdash')
    return render(request,'travel/edit.html',{'update':update,'form':form})
@login_required(login_url='travelsignin')
def Buslist(request):
    owner=request.user.first_name
    v = Bus.objects.all().filter(ownername=owner)
    return render(request,'travel/view.html',{'v':v})
def delete_view(request,id):
    booked = BusBook.objects.get(id=id)
    booked.delete()
    return redirect('busbooked')