from src.bot.entity.User import User


class Chat:
    id: int
    type: str
    user: User

    def __init__(self, id: int, type: str, user: User):
        self.id = id
        self.type = type
        self.user = user

    def get_id(self):
        return self.id

    def get_type(self):
        return self.type

    def get_user(self):
        return self.user
