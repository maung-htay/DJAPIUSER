from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from .models import UserProfile


class GroupNameField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name


class PermissionNameField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name


class UserProfileSerializer(serializers.ModelSerializer):
    groups = GroupNameField(many=True, queryset=Group.objects.all())
    user_permissions = PermissionNameField(
        many=True, queryset=Permission.objects.all())

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'username', 'password',
                  'avatar', 'groups', "user_permissions")
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print("Reach Here")
        user = UserProfile.objects.create_user(**validated_data)
        return user
