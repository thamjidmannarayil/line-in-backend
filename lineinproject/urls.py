"""Resort_Business_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include("django.contrib.auth.urls"), name='authentication'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('apps.index.urls'), name='api-index'),
    path('api/v1/auth/', include('apps.authentication.urls'), name='api-auth'),
    path('api/v1/faq/', include('apps.faq.urls'), name='api-faq'),
    path('api/v1/products/', include('apps.products.urls'), name='api-products'),
    path('api/v1/contacts/', include('apps.contacts.urls'), name='api-contacts'),
    path('api/v1/bookings/', include('apps.bookings.urls'), name='api-bookings'),
    path('api/v1/cart/', include('apps.carts.urls'), name='api-cart'),
    path('api/v1/account/', include('apps.account.urls'), name='api-account'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
