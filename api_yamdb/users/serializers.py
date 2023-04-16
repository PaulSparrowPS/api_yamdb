from rest_framework import serializers
from .models import User
from django.core.validators import RegexValidator


class SignupSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
        max_length=150,
        validators=[
            RegexValidator(
                r'^[\w.@+-]+',
                ('Введите корректное имя пользователя'
                 'без запрещенных символов')
            )
        ],
    )
    email = serializers.EmailField(required=True, max_length=254)

    def validate(self, data):
        if data.get('username') == 'me':
            raise serializers.ValidationError(
                'Использовать имя пользоватея <me> запрещено'
            )
        return data


class ConfirmationCodeSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'role',
            'bio',
            'first_name',
            'last_name',
        )


class UserMeSerializer(UserSerializer):
    role = serializers.CharField(read_only=True)
