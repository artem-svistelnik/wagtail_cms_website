from django.urls import path
# from .views import HomePageView,AboutCompanyPageView,NewsPublicationPageView
app_name = "website_admin_api"


# from .views import TagsView,TestTags,TestTags2
# app_name will help us do a reverse look-up latter.

from .api import api_router
from .views import FeedbackView
urlpatterns = [
    path('', FeedbackView.as_view(),name='feedback'),

]
