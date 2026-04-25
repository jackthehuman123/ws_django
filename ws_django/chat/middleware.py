from datetime import datetime

class WebSocketLogMiddleware:
    """
    Middleware to log WebSocket connection attempts and identify the targeted room.
    """
    def __init__(self, app):
        # Store the next ASGI application in the stack (the "inner" app)
        self.app = app

    async def __call__(self, scope, receive, send):
        # Only intercept if the protocol is a WebSocket
        if scope["type"] == "websocket":
            # Extract the room name from the URL routing keyword arguments
            # Default to "unknown" if the key isn't found
            route_kwargs = scope.get("url_route", {}).get("kwargs", {})
            room = route_kwargs.get("room_name", "unknown")

            # Log the connection timestamp and destination room
            print(f"[{datetime.now().isoformat()}] WS connect to room: {room}")

        # Hand off the request to the next layer in the middleware/routing chain
        # This is where the actual Consumer will be instantiated
        await self.app(scope, receive, send)