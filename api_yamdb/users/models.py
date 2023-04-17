from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'

    USER_ROLES = [
        (ADMIN, 'Администратор'),
        (MODERATOR, 'Модератор'),
        (USER, 'Пользователь'),
    ]
    username = models.CharField(
        'Имя пользователя',
        max_length=150,
        validators=[
            RegexValidator(
                r'^[\w.@+-]+',
                ('Введите корректное имя пользователя'
                 'без запрещенных символов')
            )],
        unique=True,
        blank=False,
        null=False
    )
    email = models.EmailField('email-адрес',
                              max_length=254,
                              unique=True,
                              blank=False,
                              null=False)
    role = models.CharField(
        'Роль',
        max_length=14,
        choices=USER_ROLES, default=USER
    )
    bio = models.TextField('Биография', null=True, blank=True)

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser or self.is_staff

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ['id']
        verbose_name = 'пользователь'

    def __str__(self):
        return self.username
