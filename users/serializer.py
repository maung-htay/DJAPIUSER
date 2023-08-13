from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from .models import UserProfile
# from django.contrib.auth import get_user_model

# UserProfile = get_user_model()


# class GroupSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = UserProfile.groups.through  # Access the ManyToMany through relationship
#         fields = ['group']


# class PermissionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile.user_permissions.related.model
#         fields = ['name']


class UserProfileSerializer(serializers.ModelSerializer):

    # groups = GroupSerializer(many=True, read_only=True)
    # user_permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'username', 'password',
                  'avatar', 'groups', "user_permissions")
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print("Reach Here")
        user = UserProfile.objects.create_user(**validated_data)
        return user
