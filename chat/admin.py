from django.contrib import admin
from .models import Room, Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["room", "sender", "body", "timestamp"]
    list_filter = ["room"]
    search_fields = ["body", "sender__username"]

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("sender", "room")
    
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    search_fields = ["name"]