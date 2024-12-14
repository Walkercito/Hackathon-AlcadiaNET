import reflex as rx
import asyncio

class State(rx.State):
    @rx.event
    def change_page(self, url: str):
        return rx.redirect(url)

class ChatState(rx.State):
    user_name: str = ""        
    messages: list[str] = []     
    current_message: str = ""     
    is_connected: bool = False    

    @rx.event(background=True)
    async def connect_websocket(self):
        try:
            await self.ws_connect()
            self.is_connected = True

            while True:
                message = await self.ws_receive() 
                if message:
                    self.messages.append(message)
        
        except Exception as e:
            print(f"Error en WebSocket: {e}")
            self.is_connected = False


    @rx.event
    async def send_message(self):

        if self.current_message.strip():
            message = f"{self.user_name}: {self.current_message}"
            
            await self.ws_send(message)
            self.current_message = ""


    @rx.event
    def on_mount(self):
        return self.connect_websocket()
