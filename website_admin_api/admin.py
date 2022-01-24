from django.contrib import admin

# Register your models here.
# from .models import HeadingNewsPublicationsTypes,Subscribers
# @admin.register(HeadingNewsPublicationsTypes)
# class AdminHeadingNewsPublications(admin.ModelAdmin):
#     list_display = ('name_heading_ru','name_heading_uk','id',)

# @admin.register(Subscribers)
# class AdminSubscribers(admin.ModelAdmin):
#     list_display = ('email','id')



#TODO Добавить в админку инфу о заявках
from .models import Feedback
@admin.register(Feedback)
class AdminSubscribers(admin.ModelAdmin):
    list_display = ('id','name','status')
    list_filter = ('status',)
    ordering = ('status',)
