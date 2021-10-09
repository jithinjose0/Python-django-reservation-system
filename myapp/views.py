from django.http.response import Http404
from django.shortcuts import render, redirect
from travel.models import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from .forms import Bookform, members
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import ugettext as _
import datetime
@login_required(login_url='signin')
def search(request):
    context = {}
    if request.method == 'POST': 
        place_r = request.POST.get('place')    
        place_list = tourist.objects.filter(place=place_r,status=True)
        if place_list:
            return render(request, 'myapp/tourist_list.html',locals())
        else:
            context["error"] = "Sorry no place availiable"
            return redirect('tourist_list')
    else:
        return redirect('tourist_list')
@login_required(login_url='signin')
def seebookings(request,new={}):
    context = {}
    id_r = request.user.id
    book_list = Book.objects.filter(userid=id_r)
    book_list_bus = BusBook.objects.filter(userid=id_r)
    if book_list:
        return render(request, 'myapp/user_dash.html',{'book_list':book_list,'book_list_bus':book_list_bus})
    else:
        return redirect('tourist_list')
def signup(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        password_r = request.POST.get('password')
        user = User.objects.create_user(name_r, email_r, password_r, )
        if user:
            login(request, user)
            return redirect('tourist_list')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'myapp/signup.html', context)
    else:
        return render(request, 'myapp/signup.html', context)
def signin(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        password_r = request.POST.get('password')
        user = authenticate(request, username=name_r, password=password_r)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('tourist_list')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'myapp/signin.html', context)
    else:
        return render(request, 'myapp/signin.html', context)
def signout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'myapp/signin.html', context)
def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'myapp/success.html', context)
def tourist_list(request):
    tourists=tourist.objects.all().filter(status=True)
    return render(request,'myapp/sample.html',{'tourists':tourists})
@login_required(login_url='signin')
def tourist_details(request,id):
    try:
        place_info=tourist.objects.get(pk=id)
    except tourist.DoesNotExist:
        raise Http404("page does not exit")
    return render(request,'myapp/tourist_details.html', { 'place_info':place_info })    
@login_required(login_url='signin')
def reserve_seat(request, id):
    try:
        place_info = tourist.objects.get(pk=id)
    except tourist.DoesNotExist:
        raise Http404("Page Does Not Exist.")
    form  = members()
    context = {'place_info':place_info,'form':form}
    return render(request,'myapp/reserve_seat.html',context)
@login_required(login_url='signin')
def payment_gateway(request):
    if request.POST:
        seats = request.POST.get('mem')
        date_r= request.POST.get('date')
        timeslot=request.POST.get('timeslot')
        id = request.POST.get('place_id')
        show = tourist.objects.get(pk=id)
        #form = BookingForm()'form':form,
        price_r = show.price
        name_r = show.place_name
        cost = int(seats) * show.price
        form = Bookform()
        context = {'form':form,'name_r':name_r,'cost':cost,'seats': seats,'show':show,'tourist':tourist,'date_r':date_r,'timeslot':timeslot,}
        return render(request,'myapp/book.html',context)
    else:
        return render(request,'myapp/tourist_list.html')
@login_required(login_url='signin')
def payment_confirmation(request):
    if request.POST:
        place_id = request.POST.get('place_id')
        show = tourist.objects.get(pk=place_id)
        seats = request.POST.get('mem')
        date_r= request.POST.get('date')
        timeslot=request.POST.get('timeslot')
        name_r=show.place_name
        place_r=show.place
        owner_r=show.ownername
        price_r=show.price
        username_r=request.user.username
        userid_r=request.user.id
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        payment_type = request.POST.get('payment_type')
        book=Book.objects.create(place=place_r,date=date_r,time=timeslot,ownername=owner_r,timestamp=timestamp, payment_type=payment_type,name=username_r,place_name=name_r,nos=seats,userid=userid_r,placeid=place_id,price=price_r)
        book.save()
        return render(request,'myapp/payment_confirmation.html')
def index(request):
    return render(request,'base/index.html')
def indexx(request):
    return render(request,'base/indexx.html')
def sample(request):
    return render(request,'myapp/sample.html')
def delete_view(request,id):
    booked = Book.objects.get(id=id)
    booked.delete()
    return redirect('seebook')
@login_required(login_url='signin')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('Your password was successfully updated!'))
            return redirect('signin')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'myapp/change_password.html', {
        'form': form
    })
@login_required(login_url='signin')
def profile(request):
    x=request.user
    return render(request,'myapp/profile.html',{'x':x})
    