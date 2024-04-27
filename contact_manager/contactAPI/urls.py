from django.urls import path
from rest_framework.routers import DefaultRouter
from contactAPI.views import UserProfileViewSet

router=DefaultRouter()
router.register(f'user',UserProfileViewSet)


urlpatterns = []+router.urls
