"""day3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from myapp.views import (IndexView, TinhToanView, LoginView,
                         FormView, ViewBaiViet, ListBaiViet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="index_views"),
    path('tinhtoan/', TinhToanView.as_view(), name='tinh_toan'),
    path('login/', LoginView.as_view(), name='login_url'),
    path('form/', FormView.as_view(), name='form_url'),
    path('a/', include('myapp.urls')),
    path('post/<slugg>/', ViewBaiViet.as_view(), name='post_detail'),
    path('post/', ListBaiViet.as_view())

]
