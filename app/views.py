from django.http import HttpResponse
from django.shortcuts import render
import asyncio
import random


async def index(request):
    return HttpResponse("I'm Async Now!")


async def delayed(request):
    delay = random.randint(1, 10)
    await asyncio.sleep(delay)
    return HttpResponse(f"I'm a {delay} Second Delayed Async!")
