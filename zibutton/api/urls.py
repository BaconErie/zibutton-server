from rest_framework import routers
from .views import ListViewSet

urlpatterns = []

router = routers.DefaultRouter()
router.register(r'lists', ListViewSet, basename='list')

urlpatterns += router.urls