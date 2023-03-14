import json
import telepot
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.conf import settings
from .models import User

class TelegramBotConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'telegram_bot'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        bot = telepot.Bot(settings.TELEGRAM_BOT_TOKEN)
        chat_id = message['chat']['id']
        command = message['text']

        keyboard = {'keyboard': [['stupid', 'fat', 'dumb']]}
        response = "Please choose one:"
        bot.sendMessage(chat_id, response, reply_markup=keyboard)

        if command == 'stupid':
            button = 'stupid'
        elif command == 'fat':
            button = 'fat'
        elif command == 'dumb':
            button = 'dumb'
        else:
            button = None

        if button is not None:
            user_id = message['from']['id']
            await self.record_button_click(user_id, button)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_response',
                'response': response
            }
        )

    @sync_to_async
    def record_button_click(self, user_id, button):
        try:
            user = User.objects.get(telegram_id=user_id)
        except User.DoesNotExist:
            user = User(telegram_id=user_id)
        setattr(user, button + '_clicks', getattr(user, button + '_clicks') + 1)
        user.save()

    async def send_response(self, event):
        response = event['response']
        await self.send(text_data=json.dumps({
            'response': response
        }))
