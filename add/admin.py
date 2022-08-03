from django.contrib import admin
from .models import Stu

# Register your models here.
@admin.register(Stu)
class modeladm(admin.ModelAdmin):
    list_display=['id','name','email','password']