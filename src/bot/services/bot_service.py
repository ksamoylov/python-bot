import requests
import src.enums.bot_enum as bot_enum
from src.bot.entity.User import User
from src.bot.entity.Message import Message
from src.bot.entity.Chat import Chat
from src.etf.mutators.etf_mutator import to_html
from src.scraper.services.scraper_service import scrap_page, get_uri_by_page
from src.image.services.image_service import create_image


def handle_hook_event(data: dict):
    user, chat, message = create_entities_by_event(data)
    
    etfs = scrap_page(get_uri_by_page(1))
    html, css = to_html(etfs)
    
    file_name = create_image(html, css, 'file.png')
    send_photo(message, open(file_name, 'rb'))


def create_entities_by_event(data: dict) -> set:
    message_data = data['message']
    user = User(**message_data['from'])
    chat = Chat(message_data['chat']['id'], message_data['chat']['type'], user)
    message = Message(message_data['message_id'], user, chat, message_data['date'], message_data['text'])

    return user, chat, message


def send_message(received_message: Message, text_message: str):
    return requests.post(
        f"{bot_enum.API_TELEGRAM_FULL_URL}/{bot_enum.SEND_MESSAGE_METHOD}",
        {
            'chat_id': received_message.chat.get_id(),
            'text': text_message,
        }
    )
    
    
def send_photo(received_message: Message, opened_file):
    params = {'chat_id': received_message.chat.get_id()}
    files = {'photo': opened_file}
    
    return requests.post(
        f"{bot_enum.API_TELEGRAM_FULL_URL}/{bot_enum.SEND_PHOTO_METHOD}",
        params,
        files=files
    )


def get_info() -> str:
    r = requests.get(f"{bot_enum.API_TELEGRAM_FULL_URL}/{bot_enum.GET_ME_METHOD}")

    return r.text
