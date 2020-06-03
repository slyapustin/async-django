from django.http import HttpResponse
from django.shortcuts import render


async def index(request):
    return HttpResponse("I'm Async Now!")
