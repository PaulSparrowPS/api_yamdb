from django.db import IntegrityError
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from api.permissions import IsAdmin
from .models import User
from .serializers import (
    ConfirmationCodeSerializer,
    SignupSerializer,
    UserMeSerializer,
    UserSerializer,
)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    try:
        user, _ = User.objects.get_or_create(**serializer.validated_data)
    except IntegrityError:
        raise ValidationError(
            'username или email заняты.', status.HTTP_400_BAD_REQUEST
        )
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        subject='Код подтверждения',
        message=f'Ваш код подтверждения для регистрации: {confirmation_code}',
        from_email=settings.FROM_EMAIL,
        recipient_list=[
            user.email,
        ],
    )
    return Response(serializer.data, status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def auth_token(request):
    serializer = ConfirmationCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    confirmation_code = serializer.validated_data.get('confirmation_code')
    username = serializer.validated_data.get('username')
    user = get_object_or_404(User, username=username)
    if not confirmation_code:
        return Response(
            'Введите confirmation_code.', status=status.HTTP_400_BAD_REQUEST
        )
    if not username:
        return Response(
            'Введите имя пользователя.', status=status.HTTP_400_BAD_REQUEST
        )
    conf_code_check = default_token_generator.check_token(user,
                                                          confirmation_code)
    if conf_code_check:
        refresh = RefreshToken.for_user(user)
        return Response(
            f'Токен для авторизации: {refresh.access_token}',
            status=status.HTTP_200_OK
        )
    return Response(
        'Неправильный confirmation_code.', status=status.HTTP_400_BAD_REQUEST
    )


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    permission_classes = [IsAdmin]
    lookup_field = 'username'
    queryset = User.objects.all()
    search_fields = ['username']
    ordering = ['username']
    http_method_names = ['get', 'post', 'patch', 'delete']

    @action(
        detail=False,
        methods=[
            'GET',
            'PATCH',
        ],
        serializer_class=UserMeSerializer,
        permission_classes=[permissions.IsAuthenticated],
    )
    def me(self, request):
        user = self.request.user
        serializer = self.get_serializer(user)
        if request.method == 'PATCH':
            serializer = self.get_serializer(
                user, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
