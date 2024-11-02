import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 21538384
API_HASH = "9b8e9b10a5c34b67054aceca02bf423e"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "8110646197:AAEUW0IiLFjU61Pi8LO_tGk4QRKg8Y61BOg"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://Avii12:Avii12@avii12.rvyxw.mongodb.net/?retryWrites=true&w=majority&appName=Avii12"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1001979385764

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 6484788124

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/GiftCodelooots"
SUPPORT_GROUP = "https://t.me/THExNIGHTxCLUBbb"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQFIplAADcy-OEOqXjHftAtyLUHOUvFyIuVpUtVhLd7jb89BkQMVr-sujdA7fbG5SFm7_f4CFowNU_LZm2MGHSZnJymKGsD73yqOQaPfGhZQEGkRabHzeIecZvCR2ed0Bw_ipfDYTyquxjcIsU6A-XEXuq9t4TbUrXMw3TlVe_0OoTDQr11FZg7H1ylrU0VyDoGhWa_dHiAB3u5yqCIv2fDwW75JZjnj64ka1CJKc9n-m7Cg-BU94oSBzO4fQ2SkB9QtNezAk3vk6-1QhBKxxe1RZ7pw8pjuPr5mvjMnxHm0NLtPaF1l14MKTDDzSm6ij0JSEl0s1bo8w74HmXdp5OQHis9HSQAAAAGSxN52AA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://envs.sh/p3W.jpg"

PING_IMG_URL = "https://envs.sh/p3W.jpg"

PLAYLIST_IMG_URL = "https://envs.sh/p3W.jpg"
STATS_IMG_URL = "https://envs.sh/p3W.jpg"
TELEGRAM_AUDIO_URL = "https://envs.sh/p3W.jpg"
TELEGRAM_VIDEO_URL = "https://envs.sh/p3W.jpg"
STREAM_IMG_URL = "https://envs.sh/p3W.jpg"
SOUNCLOUD_IMG_URL = "https://envs.sh/p3W.jpg"
YOUTUBE_IMG_URL = "https://envs.sh/p3W.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://envs.sh/p3W.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://envs.sh/p3W.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://envs.sh/p3W.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
