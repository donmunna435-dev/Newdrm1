import os

class Config(object):
    BOT_TOKEN = os.environ.get("8328284158:AAEklqmxjqcJgZhi6JYCpV7N1_qaxLZaIaM")
    API_ID = int(os.environ.get("24754824"))
    API_HASH = os.environ.get("e24a9c7a6aa24e1c56fa349e104ec20e")
    AUTH_USER = os.environ.get('AUTH_USERS', '968292174').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = " 𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎"

