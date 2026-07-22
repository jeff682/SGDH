from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['full_name'] = user.full_name
        token['roles'] = user.get_roles()
        token['employee_id'] = user.employee_id or ''
        return token


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()
    roles = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name', 'full_name',
            'phone_number', 'employee_id', 'function', 'service',
            'is_staff', 'is_superuser', 'is_active', 'roles',
            'last_login', 'date_joined',
        ]
        read_only_fields = ['last_login', 'date_joined']

    def get_roles(self, obj):
        return obj.get_roles()


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True)
    role = serializers.CharField(max_length=100, required=False, default='Demandeur')

    class Meta:
        model = User
        fields = [
            'email', 'first_name', 'last_name', 'phone_number',
            'employee_id', 'function', 'service', 'password',
            'confirm_password', 'role',
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError('Les mots de passe ne correspondent pas.')
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        role_name = validated_data.pop('role', 'Demandeur')
        user = User.objects.create_user(**validated_data)
        group, _ = Group.objects.get_or_create(name=role_name)
        user.groups.add(group)
        return user


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'phone_number',
            'function', 'service', 'employee_id',
        ]
