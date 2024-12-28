from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from djoser.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

admin.site.site_header = 'Storefront Admin'
admin.site.index_title = 'Admin'

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]


custom_djsoer_endpoints = [
    path('register/', UserViewSet.as_view({'post': 'create'}), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("resend-activation/", UserViewSet.as_view({"post": "resend_activation"}), name="resend_activation"),
    # path("activation/<str:uid>/<str:token>/", UserViewSet.as_view({"post": "activate"}), name="activate"),
    path("users/activation/", UserViewSet.as_view({"post": "activation"}), name='users_activation'),
    path("users/reset-password/", UserViewSet.as_view({"post": "reset_password"}), name="reset_password"),
    path("users/reset_password_confirm/", UserViewSet.as_view({"post": "reset_password_confirm"}), name="reset_password_confirm"),
    path("users/change_password/", UserViewSet.as_view({"post": "set_password"}), name="change_password"),
]

urlpatterns += custom_djsoer_endpoints

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
