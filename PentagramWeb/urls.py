"""PentagramWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from pentagram import views as pentagram_views
from PentagramWeb import settings
from rest_framework.authtoken import views as authtoken_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/login', authtoken_views.obtain_auth_token),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name = 'homepage'),
    url(r'api-token-auth', authtoken_views.obtain_auth_token, name = 'fetch_token'),
    url(r'^api/v1/users',pentagram_views.users, name = 'users'),
    url(r'^api/v1/photos/(?P<id_photos>[0-9]*)/likes/$', pentagram_views.likes, name = 'likes'),
    url(r'^api/v1/photos/(?P<id_photos>[0-9]*)/comments/$', pentagram_views.comments, name = 'comments'),
    url(r'^api/v1/photos/(?P<id_photos>[0-9]*)', pentagram_views.getphoto, name = 'getphoto'),
    url(r'^api/v1/photos', pentagram_views.photos, name = 'photos')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
