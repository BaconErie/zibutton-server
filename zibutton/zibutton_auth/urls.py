from django.urls import path

from rest_framework.routers import DefaultRouter

from knox import views as knox_views
from .views import LoginView, UserViewSet

urlpatterns = [
    path(r'login/', LoginView.as_view(), name='knox_login'),
    path(r'logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path(r'logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns += router.urls