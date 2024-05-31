from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Welcome to the main page</h1>')
