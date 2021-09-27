from src.helpers.environment_helper import get_env_by_name

API_TOKEN = get_env_by_name('api_token')
API_TELEGRAM_URL = "https://api.telegram.org"
API_TELEGRAM_FULL_URL = f"{API_TELEGRAM_URL}/bot{API_TOKEN}"
SEND_MESSAGE_METHOD = "sendMessage"
SEND_PHOTO_METHOD = "sendPhoto"
GET_ME_METHOD = "getMe"
