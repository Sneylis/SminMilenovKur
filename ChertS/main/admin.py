from django.contrib import admin
from .models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'news_photo','time_create','is_published')
    list_display_links = ('id','title')
    search_fields = ('title','Text')

# Register your models here.
admin.site.register(News, NewsAdmin)