from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'

    USER_ROLES = (
        (ADMIN, 'Администратор'),
        (MODERATOR, 'Модератор'),
        (USER, 'Пользователь'),
    )
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
    # first_name = models.CharField('Имя', max_length=150)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ('id',)
        verbose_name = 'пользователь'
        # constraints = (
        #     models.UniqueConstraint(
        #         fields=('username', 'email'),
        #         name='unique_username_email'
        #     ),
        # )

    def __str__(self):
        return self.username