"""storefront URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from djoser.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

admin.site.site_header = 'Storefront Admin'
admin.site.index_title = 'Admin'

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('store/', include('store.urls')),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    path('__debug__/', include(debug_toolbar.urls)),
]


custom_djsoer_endpoints = [
path('register/', UserViewSet.as_view({'post': 'create'}), name="register"),
path("login/", TokenObtainPairView.as_view(), name="login"),
path("resend-activation/", UserViewSet.as_view({"post": "resend_activation"}), name="resend_activation"),
path("activation/<str:uid>/<str:token>/", UserViewSet.as_view({"post": "activate"}), name="activate"),
path("reset-password/", UserViewSet.as_view({"post": "reset_password"}), name="reset_password"),
path("reset-password-confirm/<str:uid>/<str:token>/", UserViewSet.as_view({"post": "reset_password_confirm"}), name="reset_password_confirm"),
]

urlpatterns += custom_djsoer_endpoints


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]