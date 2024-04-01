from rest_framework import serializers
from users.models import TeachGroup, StudentProfile, Room, User, LearningCenter, TeacherProfile


class LearningCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningCenter
        fields = ['id', 'info', 'active', 'created', 'updated']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'phone_number', 'is_active', 'is_staff', 'date_joined']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'title', 'learning_center']


# class TeacherProfileSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#     groups = TeachGroupSerializer()
#     learning_center = LearningCenterSerializer()
#
#     class Meta:
#         model = TeacherProfile
#         fields = ['id', 'user', 'first_name', 'last_name', 'info', 'learning_center', 'groups', 'created', 'updated']


class TeachGroupSerializer(serializers.ModelSerializer):
    room = RoomSerializer()
    # teachers = TeacherProfileSerializer()

    class Meta:
        model = TeachGroup
        fields = ['id', 'title', 'info', 'specialty', 'room', 'price', 'active']
        read_only_field = ['created', 'updated']


class StudentsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    groups = TeachGroupSerializer()
    learning_center = LearningCenterSerializer()

    class Meta:
        model = StudentProfile
        fields = ['id', 'user', 'first_name', 'last_name', 'fathers_name', 'birthday', 'image',
                  'learning_center', 'groups']
        read_only_field = ['created', 'updated']
