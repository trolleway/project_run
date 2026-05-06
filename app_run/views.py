from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets

from .models import Run
from .serializers import RunSerializer

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

from django.shortcuts import render

# Create your views here.
