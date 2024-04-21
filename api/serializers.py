
from rest_framework import serializers
from api.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','name', 'email','dob','country','state','gender','location','image','file']
