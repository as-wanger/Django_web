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
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path

import app_five.views as v5
import app_four.views as v4
import app_one.views as v1
import app_six.views as v6
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

# app_four
urlpatterns += [
    path('app_four/', v4.index),
    re_path('app_four/(\d+)/(\w+)/', v4.index),
    path('app_four/userinfo/', v4.userinfo),
    path('app_four/post/', v4.posting),
    path('app_four/login/', v4.login),
    path('app_four/logout/', v4.logout),
]

# app_five
urlpatterns += [
    path('app_five/', v5.index),
    re_path('app_five/(\d+)/(\w+)/', v5.index),
    path('app_five/userinfo/', v5.userinfo),
    path('app_five/post/', v5.posting),
    path('app_five/login/', v5.login),
    path('app_five/logout/', v5.logout),
    # path('accounts/', include('django_registration.backends.activation.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
]

# app_six for a vote platform
urlpatterns += [
    path('app_six/', v6.index),
    path('app_six/', auth_views.LoginView.as_view()),
    path('app_six/', auth_views.LogoutView.as_view()),
    re_path('app_six/poll/(\d+)', v6.poll, name='poll-url'),
    path('app_six/govote/', v6.govote),
    re_path('app_six/vote/(\d+)/(\d+)', v6.vote, name='vote-url'),
    re_path('app_six/delpoll/(\d+)', v6.delpoll, name='delpoll-url'),
    re_path('app_six/delpollitem/(\d+)/(\d+)', v6.delpollitem, name='delpollitem-url'),
    path('app_six/addpoll/', v6.addpoll, name='addpoll-url'),
    path('app_six/addpollitem/', v6.addpollitem),
    re_path('app_six/addpollitem/(\d+)', v6.addpollitem, name='addpollitem-url'),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    # static files (images, css, js, etc...)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
