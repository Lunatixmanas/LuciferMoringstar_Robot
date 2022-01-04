import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
BOT_USERNAME = environ.get('BOT_USERNAME', 'LuciferMoringstar_Robot')

SESSION = environ.get('SESSION', 'LuciferMoringstar_Robot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

BROADCAST_CHANNEL = int(os.environ.get("BROADCAST_CHANNEL", ""))
ADMIN_ID = set(int(x) for x in os.environ.get("ADMIN_ID", "").split())
DB_URL = os.environ.get("DATABASE_1", "")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST", True))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('FORCES_SUB')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]
TUTORIAL = "https://youtu.be/-xDQbsF-wek"
# MongoDB information
DATABASE_URI = environ['DATABASE_2']
DATABASE_NAME = environ['BOT_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
**𝗜 𝗔𝗠 𝗦𝗨𝗣𝗘𝗥 𝗔𝗨𝗧𝗢 𝗙𝗜𝗟𝗧𝗘𝗥 𝗕𝗢𝗧..𝗜 𝗖𝗔𝗡 𝗣𝗿𝗼𝘃𝗶𝗱𝗲 𝗠𝗼𝘃𝗶𝗲𝘀 𝗜𝗻 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗚𝗿𝗼𝘂𝗽𝘀....

𝗝𝗨𝗦𝗧 𝗔𝗗𝗗 𝗠𝗘 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 𝗪𝗜𝗧𝗛 𝗔𝗗𝗠𝗜𝗡 𝗥𝗜𝗚𝗛𝗧𝗦 𝗔𝗡𝗗 𝗘𝗡𝗝𝗢𝗬 .
"""
START_MSG = environ.get('START_MSG', default_start_msg)

FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
OMDB_API_KEY = environ.get("OMDB_API_KEY", "http://www.omdbapi.com/?i=tt3896198&apikey=4f08a979")
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY
