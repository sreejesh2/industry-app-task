from django.urls import path
from .views import TaskViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router=DefaultRouter()

router.register('task',TaskViewSet,basename='task')

urlpatterns = [
    path('v1/token/', TokenObtainPairView.as_view(), name='two_jwt'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='refresh_token')
]+router.urls