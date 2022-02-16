from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views
from website_admin_api.api import api_router
from website_admin_api import views as website_admin_api_view
urlpatterns = [
    path('feedback-admin/', admin.site.urls),

    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

    path('search/', search_views.search, name='search'),
    path('api/', api_router.urls),
    # path('feedback/', include('website_admin_api.urls')),
    path('feedback/',website_admin_api_view.FeedbackView.as_view(),name='feedback'),
    path('feedback_for_team_member/',website_admin_api_view.FeedbackForTeamMemberView.as_view(),name='feedback_for_team_member'),
    # path('get_subscription/',website_admin_api_view.GetSubscriptionView.as_view(),name='subscription'),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
