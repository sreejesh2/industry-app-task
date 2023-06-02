from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from django.shortcuts import redirect

from .serializers import TaskSerializer
from .models import Task



class TaskViewSet(ModelViewSet):
    serializer_class=TaskSerializer
    queryset=Task.objects.all()
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]


