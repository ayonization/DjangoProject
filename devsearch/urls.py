"""devsearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

#* When user goes to a url listed below, the corresponding function is called
urlpatterns = [
    path('admin/', admin.site.urls),
    #* include urls defined in projects app
    path('',include('projects.urls'))
]

#* Setting url route for user uploaded content
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

#* Setting staticfiles url for production
urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
