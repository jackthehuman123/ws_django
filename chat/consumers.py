from channels.generic.websocket import WebsocketConsumer
import json

class EchoConsumer(WebsocketConsumer):
    def connect(self):
        print("[connect]", self.scope["client"])
        self.accept()

    def receive(self, text_data):
        data = json.loads(text_data)
        print("[receive]", data)
        self.send(text_data=text_data)

    def disconnect(self, close_code):
        print("[disconnect]", close_code)