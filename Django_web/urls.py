"""Django_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from app_.views import main_page
from app_one.views import homepage, showpost

urlpatterns = [
    path('', main_page),
    path('admin/', admin.site.urls),
]

# app_one
urlpatterns += [
    path('app_one/', homepage),
    path('/app_one/post/<slug>', showpost),
    path('/app_one/mdeditor/', include('mdeditor.urls'))
]


if settings.DEBUG:
    # static files (images, css, js, etc...)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
