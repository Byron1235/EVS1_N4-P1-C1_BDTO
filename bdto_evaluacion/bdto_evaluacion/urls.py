"""bdto_evaluacion URL Configuration

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
from django.urls import path
from evs1firstapp import views as app1
from evs1secondapp import views as app2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('futbol/', app1.displayapp1re1),
    path('elden/', app1.displayapp1re2),
    path('ricky/', app2.displayhugemessage),
    path('final/', app2.displayfinal),
]
