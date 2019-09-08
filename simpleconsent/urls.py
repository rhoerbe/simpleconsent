"""simpleconsent URL Configuration

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
from django.urls import path
from consent.views import has_consent, display_consent_request, accept_consent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('has_consent/<str:entityid>/<str:userid>/', has_consent),
    path('request_consent/<str:consent_requ_json>/', display_consent_request),
    path('accept_consent/<str:consent_requ_json>/', accept_consent),
]
