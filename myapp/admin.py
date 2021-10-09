from django.contrib import admin
from .models import *
from travel.models import *
from django.contrib.auth.models import Group
# Register your models here.
admin.site.unregister(Group)
admin.site.register(tourist)
admin.site.register(Bus)

admin.site.site_header = 'JOURNEY ADMIN'
admin.site.site_title = 'JOURNEY ADMIN'
admin.site.site_url = 'http://127.0.0.1:8000/'
admin.site.index_title = 'Journey admin '
admin.empty_value_display = '**Empty**'
