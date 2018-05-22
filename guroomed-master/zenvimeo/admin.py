from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Item

class ItemAdmin(AdminVideoMixin, admin.ModelAdmin):
    fields = ['title','description','video','video_group']

admin.site.register(Item, ItemAdmin)