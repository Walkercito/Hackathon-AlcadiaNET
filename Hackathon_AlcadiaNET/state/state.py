import reflex as rx
import asyncio

class ChatState(rx.State):
    user_name: str = ""
    messages: list[str] = []
    current_message: str = ""
    is_connected: bool = False


    @rx.event(background=True)
    async def connect_websocket(self):
        async with self:
            if self._n_tasks > 0:
                return
            self._n_tasks += 1
            self.is_connected = True


    @rx.event
    async def send_message(self):
        async with self:
            if self.current_message.strip():
                message = f"{self.user_name}: {self.current_message}"
                self.messages.append(message)
                self.current_message = ""


    @rx.event
    def on_mount(self):
        return self.connect_websocket