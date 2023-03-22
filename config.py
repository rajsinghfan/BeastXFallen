from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = 29246486
API_HASH = "efe2cb9686e634555dc1d91edb705822"

BOT_TOKEN = "6025282942:AAE3uC0yeutbmcBK642i1bEMUW4ljmnUh64"
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = 657176088

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
