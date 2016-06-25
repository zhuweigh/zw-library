# -*- coding:utf-8 -*-

from django.contrib import admin
from .models import Book,MyUser,Image

# Register your models here.

# 关于这里的 modelsadmin问题以及 inline stack 问题，呵呵
# unregister(admin)???
class MyUserAdmin(admin.ModelAdmin):
	pass
admin.site.register(MyUser,MyUserAdmin)
admin.site.register(Book)
admin.site.register(Image)
