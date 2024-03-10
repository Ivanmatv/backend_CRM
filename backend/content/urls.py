# from django.urls import include, path
from rest_framework import routers

from content.views import ContentAmbassadorView


router = routers.DefaultRouter()
router.register('content', ContentAmbassadorView, basename='content')

# urlpatterns = [
#     path('ambassadors/<int:ambassadorId>/content/',
#          ContentAmbassadorView.as_view()),
# ]
