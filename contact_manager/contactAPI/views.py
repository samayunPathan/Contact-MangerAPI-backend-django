from rest_framework.viewsets import ModelViewSet
from contactAPI.models import UserProfile
from contactAPI.serializers import UserProfileSerializers

# Create your views here.
class UserProfileViewSet(ModelViewSet):
    serializer_class=UserProfileSerializers
    queryset=UserProfile.objects.all()

