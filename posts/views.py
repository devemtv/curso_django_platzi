""" Posts views."""

# Django
from django.http import HttpResponse

#Utilities
from datetime import datetime

POSTS = [
    {
        'name': 'Mont Blanc',
        'user': 'Miguel Torrealba',
        'timestamp': datetime.now().strftime('%d-%m-%Y %H:%M'),
        'picture': 'https://i.picsum.photos/id/942/200/200.jpg',
    },
    {
        'name': 'Mont Blanc',
        'user': 'Miguel Torrealba',
        'timestamp': datetime.now().strftime('%d-%m-%Y %H:%M'),
        'picture': 'https://i.picsum.photos/id/942/200/200.jpg',
    },
    {
        'name': 'Mont Blanc',
        'user': 'Miguel Torrealba',
        'timestamp': datetime.now().strftime('%d-%m-%Y %H:%M'),
        'picture': 'https://i.picsum.photos/id/942/200/200.jpg',
    }
]


def list_posts(request):
    """Lis existing posts."""
    content = []
    for post in POSTS:
        content.append("""
          <p><strong>{name}</strong></p>
          <p><small>{user} - <i>{timestamp}</i></small></p>
          <figure><img src="{picture}"></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))
