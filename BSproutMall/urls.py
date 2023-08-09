"""
URL configuration for BSproutMall project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from apps.merchandise import views as merchandise_views
from apps.login import views as login_views
from rest_framework import routers
from rest_framework.authtoken import views as authtoken_views

router = routers.DefaultRouter()
router.register('spu', merchandise_views.SpuInfoView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/spu-list', merchandise_views.SpuInfoList.as_view()),
    path('api/login', login_views.Login.as_view()),
    path('api/token-auth', authtoken_views.obtain_auth_token)
]
