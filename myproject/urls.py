"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import *
    
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search/$', search, name='search'),
    url(r'^seebookings/$',seebookings, name='seebook'),
    url(r'^signup/$',signup, name='signup'),
    url(r'^signin/$',signin, name='signin'),
    url(r'^signout/$',signout, name='signout'),
    url(r'^success/$',success, name='success'),
    url(r'^tourist_list/$',tourist_list, name='tourist_list'),
    url(r'^tourist_list/(?P<id>\d+)/$',tourist_details, name='tourist_details'),
    url(r'^tourist_list/seatchoice/(?P<id>\d+)/$',reserve_seat, name='reserve_seat'),
    url(r'^booking/payment/$',payment_gateway, name='payment_gateway'),
    url(r'^booking/payment_confirmation/$',payment_confirmation, name='payment_confirmation'),
    path('touristpage/',include('tourist.urls')),
    path('',index,name='index'),
    path('indexx',indexx,name='indexx'),
    path('sample',sample,name='sample'),
    path('delete/<int:id>',delete_view,name='delete'),
    url(r'^password/$',change_password, name='change_password'),
    path('userprofile',profile,name='userprofile'),
    path('travelpage/',include('travel.urls')),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
    
