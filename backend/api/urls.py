"""URLs for API version 1."""

from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from ambassadors.views import AmbassadorViewSet, PromocodeViewSet


router = DefaultRouter()
router.register('ambassadors', AmbassadorViewSet, basename='ambassador')


urlpatterns = [
    path('signup/', UserViewSet.as_view({'post': 'create'}), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('ambassadors/<int:id>/promocodes/', PromocodeViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='get_promo'),
    path('', include('djoser.urls')),
    path('', include(router.urls)),
]
