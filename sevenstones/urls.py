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
from django.contrib import admin
from django.conf.urls import url
from django.http import HttpResponse
import www.views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', www.views.index, name='home'),
    url(r'^googlea423953eaf1a9da1\.html$', lambda r: HttpResponse("google-site-verification: googlea423953eaf1a9da1.html")),
    #url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^privacy/', www.views.privacy),
    url(r'^thanks/', www.views.thanks),
    url(r'^error/', www.views.error),
    url(r'^services/', www.views.services),
    url(r'^software/', www.views.software),
    url(r'^security_de_engineering/', www.views.secdeng),
    url(r'^pentest-profile/', www.views.pentest),
    url(r'^service-definition/', www.views.service_definition),
    url(r'^service-definition-plain/', www.views.service_definition_plain),
]

handler404 = 'www.views.handler404'
handler500 = 'www.views.handler500'
