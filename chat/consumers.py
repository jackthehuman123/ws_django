from channels.generic.websocket import AsyncWebsocketConsumer

class EchoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
    async def receive(self, text_data):
        await self.send(text_data=text_data)

    async def disconnect(self, code):
        return await super().disconnect(code)    
    

class RoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        #? Get room name
        self.room_group_name = f"chat_{self.room_name}"
        #? Add channel to group (self.channel_name belongs to the connection)
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def receive(self, text_data):
        #? Send message to the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat.message", #? calls the handler (chat_message)
                #? data to be sent
                "text": text_data,
                # "name": "alice",
                # ...
            }
        )

    #? The handler 
    async def chat_message(self, event):
        await self.send(text_data=event["text"])

    async def disconnect(self, code):
        #? remove channel from group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )
        await super().disconnect(code)