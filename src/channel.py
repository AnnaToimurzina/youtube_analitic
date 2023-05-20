import json
import os

# необходимо установить через: pip install google-api-python-client
from google-api-client.discovery import build

import isodate

from helper.youtube_api_manual import printj


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.getenv('YT_API_KEY')

        # создать специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=api_key)

    def print_info(self) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

        ''' получить данные о канале по его id docs: https://developers.google.com/youtube/v3/docs/channels/list 
        сервис для быстрого получения id канала: https://commentpicker.com/youtube-channel-id.php'''
        # channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'  # MoscowPython

        channel_id = 'UCwHL6WHUarjGfUM_586me8w'  # HighLoad Channel
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        printj(channel)


        '''получить данные по play-листам канала
docs: https://developers.google.com/youtube/v3/docs/playlists/list'''

        playlists = youtube.playlists().list(channelId=channel_id,
                                             part='contentDetails,snippet',
                                             maxResults=50,
                                             ).execute()
        for playlist in playlists['items']:
            print(playlist)
            print()




