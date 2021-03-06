from rest_framework import serializers

from restaurants.models import Restaurant
from .models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'name',
            'email',
        )


class SignupSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'pk',
            'name',
            'email',
            'password1',
            'password2',
        )

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('Password does not match')
        return data

    def create(self, validated_data):
        return self.Meta.model.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password1'],
        )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        data = {
            'user': ret,
            'token': instance.token,
        }
        return data


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = (
            'profile_image',
            'nickname',
            'preferences',
            'user',
        )


class PureProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'profile_image',
            'nickname',
        )


class ProfileImageSerializer(serializers.ModelSerializer):
    profile = PureProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            'pk',
            'profile',
        )


class PreferenceSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = (
            'preferences',
            'user',
        )


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password_confirm = serializers.CharField(required=True)


class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
    new_password_confirm = serializers.CharField(required=True)


class BasicInfoRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = (
            'pk',
            'name',
        )


class OwnerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    # restaurant = BasicInfoRestaurantSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = (
            'profile_image',
            'nickname',
            'is_owner',
            'user'
            # 'restaurant',
        )
