from rest_framework import routers
from .views import ListViewSet, UserViewSet

urlpatterns = []

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'lists', ListViewSet, basename='list')

urlpatterns += router.urls