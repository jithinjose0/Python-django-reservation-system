from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [

    path('login',views.tousignin,name="login"),
    path('touristsignup',views.register_view,name="touristsignup"),
    path('touristsignout',views.touristsignout,name='touristsignout'),
    path('tourist_register',views.tourist_register,name='tourist_register'),
    path('fullseebooking',views.fullseebookings,name='fullseebooking'),
    path('update',views.update_view,name='update'),
    path('viewed',views.viewed,name='viewed'),
    path('dash',views.dash,name='dash'),
    url(r'^password/$',views.change_password, name='changepass'),
    path('profile',views.profile,name='profile'),
    path('del/<int:id>',views.delete_view,name='del'),

    
]

    