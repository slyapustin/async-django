import asyncio
import random

import aioredis
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .connections import get_redis_connection

from project.settings import REDIS_URL

CHANNEL_NAME = 'channel:chat'


def index(request):
    return render(request, "app/index.html")


async def publish(request):
    redis = await get_redis_connection()
    await redis.publish(CHANNEL_NAME, request.body.decode())
    return HttpResponse()


async def subscribe(request):
    redis = await get_redis_connection()
    res = await redis.subscribe(CHANNEL_NAME)
    ch1 = res[0]
    if await ch1.wait_message():
        msg = await ch1.get()
        return HttpResponse(msg)
    else:
        await sub.unsubscribe(CHANNEL_NAME)   
        return HttpResponse(status=204)
