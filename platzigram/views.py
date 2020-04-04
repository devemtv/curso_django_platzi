""" Platzigram Views"""

# Django
from django.http import (
    HttpResponse,
    JsonResponse,
)

# Utilities
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime('%d-%m-%Y %H:%M')
    return HttpResponse(f'Oh, hi! Current server time is {now}')


def hi(request):
    """Hi."""
    _numbers = [int(value) for value in request.GET['numbers'].split(',')]
    _numbers.sort()
    return JsonResponse(_numbers, safe=False)
