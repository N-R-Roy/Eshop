"""Eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import re

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve

# from . import settings


urlpatterns = [
    path('', include('store.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # """This is work when debug is off"""
    # re_path(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')), serve, kwargs={'document_root':settings.STATIC_ROOT}),
    # re_path(r'^%s(?P<path>.*)$' % re.escape(settings.MEDIA_URL.lstrip('/')), serve, kwargs={'document_root':settings.MEDIA_ROOT}),
]

"""
This is work when debug is on
# """
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



