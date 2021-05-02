from django.contrib import admin

# Register your models here.
from .models import HeadingNewsPublicationsTypes,NewsPublicationTag
@admin.register(HeadingNewsPublicationsTypes)
class AdminHeadingNewsPublications(admin.ModelAdmin):
    list_display = ('name_heading_ru','name_heading_uk','id',)
@admin.register(NewsPublicationTag)
class AdminNewsPublicationTag(admin.ModelAdmin):
    list_display = ('id',)
