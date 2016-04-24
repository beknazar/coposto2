from rest_framework import serializers, viewsets

from django.contrib.auth.models import User

from models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'passport_number', 'phone_number', 'is_passport_verified',
            'is_phone_verified', 'success_rate'
        )


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = (
            'id', 'password', 'email', 'first_name', 'last_name',
            'profile',
        )

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user
