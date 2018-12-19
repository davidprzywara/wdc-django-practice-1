from datetime import datetime, timedelta

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest


# Use /hello-world URL
def hello_world(request):
    return HttpResponse('Hello World')


# Use /date URL
def current_date(request):
    return HttpResponse(datetime.today().strftime('%Y-%m-%d'))


# Use URL with format /my-age/<year>/<month>/<day>
def my_age(request, year, month, day):
    bday = datetime(year=int(year), month=int(month), day=int(day))
    delta = datetime.now() - bday
    return HttpResponse('Your age is {} years old'.format(int(delta.days / 365)))


# Use URL with format /next-birthday/<birthday>
def next_birthday(request, birthday):
    bday = datetime.strptime(birthday, '%Y-%m-%d')
    next_bday = datetime(year=datetime.now().year + 1, month=bday.month, day=bday.day)
    delta = next_bday - datetime.now()
    return HttpResponse('Days until next birthday: {}'.format(int(delta.days)))


# Use /profile URL
def profile(request):
    return render(request, 'profile.html', {
        'my_name': 'Dave P',
        'my_age': 36,
    })
    
"""
    This view should render the template 'profile.html'. Make sure you return
    the correct context to make it work.
"""

"""
    The goal for next task is to practice routing between two URLs.
    You will have:
        - /authors --> contains a list of Authors (template is provided to you)
        - /author/<authors_last_name> --> contains the detail for given author,
        using the AUTHORS_INFO provided below.

    First view just have to render the given 'authors.html' template sending the
    AUTHORS_INFO as context.

    Second view has to take the authors_last_name provided in the URL, look for
    for the proper author info in the dictionary, and send it as context while
    rendering the 'author.html' template. Make sure to complete the given
    'author.html' template with the data that you send.
"""
AUTHORS_INFO = {
    'poe': {
        'full_name': 'Edgar Allan Poe',
        'nationality': 'US',
        'notable_work': 'The Raven',
        'born': 'January 19, 1809',
    },
    'borges': {
        'full_name': 'Jorge Luis Borges',
        'nationality': 'Argentine',
        'notable_work': 'The Aleph',
        'born': 'August 24, 1899',
    }
}

# Use provided URLs, don't change them
def authors(request):
    return render(request, 'authors.html')


def author(request, authors_last_name):
    return render(request, 'author.html', {
        'full_name': AUTHORS_INFO[authors_last_name]['full_name'],
        'nationality': AUTHORS_INFO[authors_last_name]['nationality'],
        'notable_work': AUTHORS_INFO[authors_last_name]['notable_work'],
        'born': AUTHORS_INFO[authors_last_name]['born']
    })
