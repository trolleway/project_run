from django.http import HttpResponse
from django.http import JsonResponse

from django.conf import settings

@api_view(['GET'])
def company_details(request):
    COMPANY_NAME = settings.COMPANY_NAME
    SLOGAN = settings.SLOGAN
    CONTACTS = settings.CONTACTS
    return JsonResponse({'company_name': COMPANY_NAME,'slogan':SLOGAN,'contacts':CONTACTS})



from django.shortcuts import render

# Create your views here.
