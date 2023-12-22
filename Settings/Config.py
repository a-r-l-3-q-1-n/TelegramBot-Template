import os

from dotenv import load_dotenv


load_dotenv()


# =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
BOT_TOKEN = os.getenv('BOT_TOKEN')
# =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=

ADMIN_ID = os.getenv('ADMIN_ID')
SUPPORT_CHAT_ID = os.getenv('SUPPORT_CHAT_ID')

# =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
DATABASE = os.getenv('DATABASE')
LOG = os.getenv('LOG')
