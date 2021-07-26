import requests
import src.enums.bot_enum as bot_enum
from src.bot.entity.User import User
from src.bot.entity.Message import Message
from src.bot.entity.Chat import Chat


def handle_hook_event(data: dict):
    user, chat, message = create_entities(data)
    send_message(message)


def create_entities(data: dict) -> set:
    message_data = data["message"]
    user = User(**message_data["from"])
    chat = Chat(message_data["chat"]["id"], message_data["chat"]["type"], user)
    message = Message(message_data["message_id"], user, chat)

    return user, chat, message


def send_message(received_message: Message):
    r = requests.post(
        f"{bot_enum.API_TELEGRAM_FULL_URL}/{bot_enum.SEND_MESSAGE_METHOD}",
        {
            "chat_id": received_message.chat.get_id(),
            "text": f"Hey, {received_message.user.get_first_name()}!",
        }
    )

    print(r.text)
