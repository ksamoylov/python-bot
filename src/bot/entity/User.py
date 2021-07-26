class User:
    id: int
    is_bot: bool
    first_name: str
    last_name: str
    username: str
    language_code: str

    def __init__(self, id: int, is_bot: bool, first_name: str, last_name: str, username: str, language_code: str):
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code

    def get_id(self) -> int:
        return self.id

    def get_first_name(self) -> str:
        return self.first_name

    def get_last_name(self) -> str:
        return self.last_name

    def get_username(self) -> str:
        return self.username

    def get_language_code(self) -> str:
        return self.language_code
