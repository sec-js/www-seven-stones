"""sevenstones URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.http import HttpResponse
import www.views
from django.contrib import admin
from django.urls import include, re_path
admin.autodiscover()

urlpatterns = [
    re_path(r'^$', www.views.index, name='home'),
    re_path(r'^googlea423953eaf1a9da1\.html$', lambda r: HttpResponse("google-site-verification: googlea423953eaf1a9da1.html")),
    #re_path(r'^admin/', admin.site.urls, name='admin'),
    re_path(r'^privacy/', www.views.privacy),
    re_path(r'^thanks/', www.views.thanks),
    re_path(r'^error/', www.views.error),
    re_path(r'^services/', www.views.services),
    re_path(r'^software/', www.views.software),
    re_path(r'^security_de_engineering/', www.views.secdeng),
    re_path(r'^pentest-profile/', www.views.pentest),
    re_path(r'^service-definition/', www.views.service_definition),
    re_path(r'^service-definition-plain/', www.views.service_definition_plain),
]

handler404 = 'www.views.handler404'
handler500 = 'www.views.handler500'
