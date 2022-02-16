from django.contrib import admin

# Register your models here.
# from .models import HeadingNewsPublicationsTypes,Subscribers
# @admin.register(HeadingNewsPublicationsTypes)
# class AdminHeadingNewsPublications(admin.ModelAdmin):
#     list_display = ('name_heading_ru','name_heading_uk','id',)

# @admin.register(Subscribers)
# class AdminSubscribers(admin.ModelAdmin):
#     list_display = ('email','id')


from .models import Feedback, FeedbackForTeamMember


@admin.register(Feedback)
class AdminFeedback(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'created')
    list_filter = ('status', 'created')
    ordering = ('status', 'created')

@admin.register(FeedbackForTeamMember)
class AdminFeedbackForTeamMember(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'created','team_member')
    list_filter = ('status', 'created','team_member')
    ordering = ('status', 'created','team_member')
