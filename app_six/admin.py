from django.contrib import admin

from app_six import models


# Register your models here.
class PollAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'created_at', 'enabled')
    ordering = ('-created_at',)


class PollItemAdmin(admin.ModelAdmin):
    list_display = ('poll', 'name', 'vote', 'image_url')
    ordering = ('poll',)


admin.site.register(models.Poll, PollAdmin)
admin.site.register(models.PollItem, PollItemAdmin)
admin.site.register(models.VoteCheck)
