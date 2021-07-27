class Bot:
    id: int
    is_bot: bool
    first_name: str
    username: str
    can_join_groups: bool
    can_read_all_group_messages: bool
    supports_inline_queries: bool

    def __init__(
            self,
            id: int,
            is_bot: bool,
            first_name: str,
            username: str,
            can_join_groups: bool,
            can_read_all_group_messages: bool,
            supports_inline_queries: bool
    ):
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.username = username
        self.can_join_groups = can_join_groups
        self.can_read_all_group_messages = can_read_all_group_messages
        self.supports_inline_queries = supports_inline_queries

    def get_id(self):
        return self.id
