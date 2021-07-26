import src.bot.entity.Message
from src.bot.entity.User import User
from src.bot.entity.Message import Message
from src.bot.entity.Chat import Chat


def handle_hook_event(data: dict):
    user, message, chat = create_entities(data)
    print(user.get_last_name(), message.get_message_id(), chat.get_id())
    pass


def create_entities(data: dict) -> set:
    message_data = data['message']
    user = User(**message_data['from'])
    chat = Chat(message_data['chat']['id'], message_data['chat']['type'], user)
    message = Message(message_data['message_id'], user, chat)

    return user, message, chat
