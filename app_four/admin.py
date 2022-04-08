from django.contrib import admin

from app_four import models

# Register your models here.
admin.site.register(models.Profile)
admin.site.register(models.Diary)