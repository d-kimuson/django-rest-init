from rest_framework import routers

from user.views import UserViewSet
from .views import SampleViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('sample', SampleViewSet)
