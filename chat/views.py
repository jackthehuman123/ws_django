from django.shortcuts import render
from django.http import JsonResponse
from .models import Message

def room_history(request, room_name):
    messages = Message.objects.filter(room=room_name).order_by("-timestamp")[:50]
    data = [{"content": m.content, "timestamp": m.timestamp.isoformat()} for m in reversed(list(messages))]
    return JsonResponse({"messages": data})

# Create your views here.
