from myapp.models import *
from django.shortcuts import render, redirect
from .form import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import ugettext as _
def tourist_register(request):
    if request.method == 'POST':
        form = touristForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print('sucessssss')
            return render(request,'tourist/wait.html')
    else:
        form=touristForm()
    return render(request,'tourist/tourist.html',{'form':form})
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print('successssssss')
            return redirect('tourist_register')
    else:
        form=RegisterForm()
    return render(request,'tourist/tousignup.html',{'form':form})
def tousignin(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        password_r = request.POST.get('password')
        user = authenticate(request, username=name_r, password=password_r)
        if user:
            login(request, user)
            if tourist.objects.filter(status=True):
                return redirect('dash')
            else:
                return render(request,'tourist/wait.html')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'tourist/tousignin.html', context)
    else:
        return render(request, 'tourist/tousignin.html', context)
def touristsignout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'tourist/tousignin.html', context)
@login_required(login_url='login')
def fullseebookings(request,new={}):
    context = {}
    owner=request.user.first_name
    book_list = Book.objects.filter(ownername=owner)
    
    if book_list:
        return render(request, 'tourist/booklist.html', locals())
    else:
        context["error"] = "Sorry no  booked"
        return render(request, 'tourist/sorry.html', context)
@login_required(login_url='login')
def dash(request):
    owner=request.user.first_name
    book_list = Book.objects.filter(ownername=owner)
    x=book_list.count()
    if x==0:
        return render(request,'tourist/sorry.html')
    else:
        return render(request,'base/dash.html',{'x':x})
@login_required(login_url='login')
def update_view(request,new={}):
    owner=request.user.first_name
    update = Book.objects.filter(ownername=owner)
    form =touristForm(request.POST,request.FILES)
    if form.is_valid():
        form.save(commit=True)
        return redirect('dash')
    return render(request,'tourist/update.html',{'update':update,'form':form})
@login_required(login_url='login')
def viewed(request):
    owner=request.user.first_name
    v = tourist.objects.all().filter(ownername=owner)
    return render(request,'tourist/view.html',{'v':v})
@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('Your password was successfully updated!'))
            return redirect('login')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'tourist/change_password.html', {
        'form': form
    })
@login_required(login_url='login')
def profile(request):
    p = request.user
    return render(request,'tourist/profile.html',{'p':p})
def delete_view(request,id):
    booked = Book.objects.get(id=id)
    booked.delete()
    return redirect('fullseebooking')
