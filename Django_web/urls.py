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
from django.urls import path, include, re_path

import app_one.views as v1
import app_three.views as v3
import app_two.views as v2
from app_.views import main_page

urlpatterns = [
    path('', main_page),
    path('admin/', admin.site.urls),
]

# app_one
urlpatterns += [
    path('app_one/', v1.homepage),
    re_path('app_one/post/(\w+)', v1.showpost),
    path('mdeditor/', include('mdeditor.urls'))
]

# app_two
urlpatterns += [
    path('app_two/', v2.index),
    re_path('app_two/detail/(\d+)', v2.detail, name='detail-url')
]

# app_three
urlpatterns += [
    path('app_three/', v3.index),
    path('app_three/list/', v3.listing),
    path('app_three/post/', v3.posting),
    path('app_three/post2db/', v3.post2db),
    path('app_three/contact/', v3.contact),
    path('captcha/', include('captcha.urls')),
]


if settings.DEBUG:
    # static files (images, css, js, etc...)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
