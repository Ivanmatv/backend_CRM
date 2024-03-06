"""URLs for API version 1."""

from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from ambassadors.views import (AmbassadorViewSet,
                               AmbassadorMerchViewSet,
                               AmbassadorPromocodeViewSet)


from merch.views import MerchViewSet, OrderViewSet, MerchOrderViewSet

app_name = 'api'

router = DefaultRouter()
router.register('ambassadors', AmbassadorViewSet, basename='ambassador')
router.register(r'merch', MerchViewSet, basename='merch')
router.register(r'order', OrderViewSet, basename='order')
router.register(r'ordering_merch',
                MerchOrderViewSet, basename='ordering_merch')


urlpatterns = [
    path('signup/', UserViewSet.as_view({'post': 'create'}), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('ambassadors/<int:id>/promocodes/',
         AmbassadorPromocodeViewSet.as_view({'get': 'list', 'post': 'create'}
                                            ), name='get_promo'),
    path('ambassadors/<int:id>/merch/', AmbassadorMerchViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='get_merch'),
    path('', include('djoser.urls')),
    path('', include(router.urls)),
]
