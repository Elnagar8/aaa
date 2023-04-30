 from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = int(getenv("API_ID", "25285918"))
API_HASH = getenv("API_HASH", "b8325224911adaa952aee661d7ac0810")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "10"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://dream:dream@cluster0.pm3y5me.mongodb.net/dream?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1970797144").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "1970797144").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001817954059"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Shadow")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = "https://github.com/Elnagar8/aaa"
UPSTREAM_BRANCH = "main"

SUPPORT_CHANNEL = "https://t.me/FA9SH"
SUPPORT_GROUP = "https://t.me/S150D"

THUMBNAIL = getenv("THUMB_LINK", "https://telegra.ph/file/74047a1ba4804eddc787e.jpg") 

botusername = str(getenv("BOT_USERNAME", "fn1bot"))

if str(getenv("STRING_SESSION1")).strip() == "":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("-1001817954059"))

if str(getenv("LIMIT")).strip().upper() == "FALSE":
    PL_LIMIT = "FALSE"
else:
    PL_LIMIT = "TRUE"

if str(getenv("PM_PERMIT")).strip().upper() == "FALSE":
    PM_PERMIT = "FALSE"
else:
    PM_PERMIT = "TRUE"
