from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as auth_views
from api.urls import router as api_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', auth_views.obtain_auth_token),  # POST: username, password => TOKEN
    path('api/', include(api_router.urls)),
]
