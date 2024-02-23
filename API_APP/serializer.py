from rest_framework import serializers
from API_APP.models import Profile

class ProfileSerializersAPI(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__" 