from django.http import HttpResponse
from django.shortcuts import render


def view_counter(request):
    request.session['counter'] = request.session.get('counter', 0) + 1

    return HttpResponse(f"The account is {request.session.get('counter')}")
