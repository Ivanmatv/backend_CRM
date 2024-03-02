"""URLs for API version 1."""

from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

from merch.views import MerchViewSet, OrderViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'merch', MerchViewSet, basename='merch')
router.register(r'order', OrderViewSet, basename='order')


urlpatterns = [
    path('signup/', UserViewSet.as_view({'post': 'create'}), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('djoser.urls')),
    path('', include(router.urls)),
]
