"""
URL configuration for PouryaTel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_module.urls')),
    path('auth/', include('account_module.urls')),
    path('products/', include('product_module.urls')),
    path('us/', include('about_module.urls')),
    path('panel/', include('user_panel_module.urls')),
    path('order/', include('order_module.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
