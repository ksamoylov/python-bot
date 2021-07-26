from src.bot.entity.User import User
from src.bot.entity.Chat import Chat


class Message:
    message_id: int
    user: User
    chat: Chat

    def __init__(self, message_id: int, user: User, chat: Chat):
        self.message_id = message_id
        self.user = user
        self.chat = chat

    def get_message_id(self) -> int:
        return self.message_id

    def get_user(self) -> User:
        return self.user

    def get_chat(self) -> Chat:
        return self.chat

