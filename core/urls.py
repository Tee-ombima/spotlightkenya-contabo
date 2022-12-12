from django.conf import settings
from django.urls import include, re_path
from django.contrib import admin
from django.urls import path
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.contrib.sitemaps.views import sitemap
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from django.views.generic import RedirectView
# from home import views
from django.contrib.staticfiles.storage import staticfiles_storage
from magazine import urls as magazine_urls
from search import views as search_views
from subscription import urls as subscription_urls
#from mpesa.urls import mpesa_urls


from django_registration.backends.one_step.views import RegistrationView

# TODO: Change this line to send verification emails when registering users
# Note: this will require two activation email tempates (subject and body)
# from django_registration.backends.activation.views import RegistrationView
from accounts.forms import CustomUserForm

urlpatterns = [
    #path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),

    re_path(
        r"^accounts/register/$",
        RegistrationView.as_view(form_class=CustomUserForm),
        name="django_registration_register",
    ),
    path("accounts/", include("django_registration.backends.one_step.urls")),
    path("accounts/", include("django.contrib.auth.urls")),

    path("magazine/", include(magazine_urls), name="magazine"),

    
    path("documents/", include(wagtaildocs_urls)),
    re_path(r"^search/$", search_views.search, name="search"),
    path("subscriptions/", include(subscription_urls), name="subscriptions"),
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    re_path("^sitemap\.xml$", sitemap),

    path("", include(wagtail_urls)),


    # path("", include("home.urls")),
    # path("homepagefeaturedevent/", include("home.urls")),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("img/favicon.ico")),
    ),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
