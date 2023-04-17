from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import signup, auth_token, UsersViewSet

v1_router = DefaultRouter()

v1_router.register(r'users', UsersViewSet, basename='users')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/signup/', signup),
    path('v1/auth/token/', auth_token),
]
