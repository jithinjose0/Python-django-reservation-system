from django.urls import path
from .views import *
from django.conf.urls import url
urlpatterns = [
    path('travelsignup',travelsignup,name="travelsignup"),
    path('travelsignin',travelsignin,name="travelsignin"),
    path('travelsignout',travelsignout,name='travelsignout'),
    path('busregister',bus_register,name='busregister'),
    path('findbus',findbus,name='findbus'),
    url(r'^travel_list/seats/(?P<id>\d+)/$',reserve_seat, name='reserve_bus_seat'),
    url(r'^booking/payment/$',bookings, name='bus_payment'),
    path('busbooked',busbooked,name='busbooked'),
    path('busdash',dashboard,name='busdash'),
    path('changepassword',change_password,name='change'),
    path('profile',prof,name='prof'),
    path('edit',edit,name='edit'),
    path('buslist',Buslist,name='buslist'),
    path('del/<int:id>',delete_view,name='deletebooked'),

]