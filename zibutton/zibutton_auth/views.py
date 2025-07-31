from django.contrib.auth import login
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import viewsets, mixins
from knox.views import LoginView as KnoxLoginView
from .serializers import UserSerializer
from .permissions import UserPermission
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.reverse import reverse


# We use Knox for token-based authentication
# See https://jazzband.github.io/django-rest-knox/auth/ for info

class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)

class UserViewSet(viewsets.GenericViewSet,
                 mixins.RetrieveModelMixin,):
    serializer_class = UserSerializer
    permission_classes = [UserPermission]

    def get_permissions(self):
        if self.action == 'create_user':
            return [AllowAny()]
        return super().get_permissions()

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
    
    @action(methods=['post'], detail=False, url_path='create-user', url_name='create_user')
    def create_user(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=400)
        
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Duplicate username'}, status=409)
        
        user = User.objects.create_user(username=username, password=password)
        return Response({'status': 'User created', 'url': reverse('user-detail', kwargs={'pk': user.pk}, request=request)}, status=201)
        
    
    @action(methods=['post'], detail=False, url_path='change-password', url_name='change_password')
    def change_password(self, request):
        user = request.user

        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')

        print(user.username)

        if not old_password or not user.check_password(old_password):
            return Response({'error': 'Old password is incorrect'}, status=400)

        if new_password:
            user.set_password(new_password)
            user.save()
            return Response({'status': 'Password set'})
        else:
            return Response({'error': 'New password not provided'}, status=400)
    
    @action(methods=['post'], detail=False, url_path='delete-user', url_name='delete_user')
    def delete_user(self, request):
        user = request.user

        password = request.data.get('password')

        if not password or not user.check_password(password):
            return Response({'error': 'Password is incorrect'}, status=400)

        user.delete()
        return Response({'status': 'Account deleted'}, status=204)