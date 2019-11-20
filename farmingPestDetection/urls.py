"""farmingPestDetection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from FPD.views import HomePage , LoginPage , RegisterPage,RegisterFarmPage, PestsPage


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePage, name='home'),
    url(r'^login/$', LoginPage, name='login'),
    url(r'^register/$', RegisterPage, name='register'),
    url(r'^register_farm/$', RegisterFarmPage, name='register_farm'),
    url(r'^pest_form/$', PestsPage, name='pest_form'),


]
if settings.DEBUG:
    urlpatterns=urlpatterns+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns=urlpatterns+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)