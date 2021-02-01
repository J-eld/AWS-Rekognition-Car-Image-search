"""Mission2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from webpage.views import home_view, sedan_view, coupe_view, van_view, truck_view, suv_view, convertible_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('upload', include('webpage.urls')),
    path('sedan', sedan_view),
    path('coupe', coupe_view),
    path('truck', truck_view),
    path('convertible', convertible_view),
    path('van', van_view),
    path('suv', suv_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()


