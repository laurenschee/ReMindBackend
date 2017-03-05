"""dementiaHack2017 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin
from . import views
from reMind import views as homesense_views
from alerts import views as alert_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^remind_home/', views.home_page, name='ReMind Home'),
    url(r'^create_user/', views.create_user, name='create_user'),
    url(r'^create_emergency_contact/', homesense_views.create_emergency_contact, name='create_emergency_contact'),
    url(r'^send_alert/$', alert_views.send_alert, name='send_alert'),
    url(r'^send_alert_2/$', homesense_views.AlertView.as_view()), #for testing
]
