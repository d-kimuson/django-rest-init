from rest_framework import routers

from user.views import UserViewSet
from .views import SampleViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('samples', SampleViewSet)
