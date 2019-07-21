from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import *
# Register your models here.


adminSite=AdminSite()

adminSite.register(Expense)

adminSite.register(User)

