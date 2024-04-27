from rest_framework.serializers import ModelSerializer
from contactAPI.models import UserProfile

class UserProfileSerializers(ModelSerializer):
    class Meta:
        model=UserProfile
        fields=(
            "id",
            "email",
            "password",
        )
        extra_kwargs={
            "password":{"write_only":True,"style":{"input_style":"password"}}
        }

    def create(self, validated_data):
        user=UserProfile.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user