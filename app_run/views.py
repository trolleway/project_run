from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.contrib.auth import get_user_model

from .models import Run
from .serializers import RunSerializer
from .serializers import UserSerializer

from django.conf import settings

@api_view(['GET'])
def company_details(request):
    COMPANY_NAME = settings.COMPANY_NAME
    SLOGAN = settings.SLOGAN
    CONTACTS = settings.CONTACTS
    return JsonResponse({'company_name': COMPANY_NAME,'slogan':SLOGAN,'contacts':CONTACTS})

class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.all()
    serializer_class = RunSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        qs = self.queryset  # Используем базовый queryset определенный выше, на уровне класса
        qs = qs.filter(is_superuser=False)
        type = self.request.query_params.get('type', None)
        if type == 'coach':
            qs = qs.filter(is_staff=True)
        elif type == 'athlete':
            qs = qs.filter(is_staff=False)
        else:
            pass
        return qs



from django.shortcuts import render

# Create your views here.
