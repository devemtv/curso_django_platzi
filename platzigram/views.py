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


def sorted_number_list(request):
    """Hi."""
    _numbers = [int(value) for value in request.GET['numbers'].split(',')]
    _numbers.sort()
    return JsonResponse(_numbers, safe=False)


def say_hi(request, name, age):
    if age < 18:
        message = f'Sorry {name}, you are not allowed here'
    else:
        message = f'Hello {name}, Welcome to Platzigram'

    response = {
        'message': message,
        'data': {
            'name': name,
            'age': age,
        },
        'status_code': 200,
    }
    return JsonResponse(response)
