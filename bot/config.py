from bot.get_cfg import get_config

class Config(object):from bot.get_cfg import get_config

class Config(object):

    # You can keep this default

    SESSION_NAME = get_config("SESSION_NAME", "SJCompressorBot")

    # AHCompressBot....

    # sucks Dude

    APP_ID = get_config("APP_ID", "19099900")

    API_HASH = get_config("API_HASH", "2b445de78e5baf012a0793e60bd4fbf5")

    LOG_CHANNEL = get_config("LOG_CHANNEL", "CompressorBotLogAC")

    UPDATES_CHANNEL = get_config("UPDATES_CHANNEL", None) # Without @ LOL

     # Get these values from my.telegram.org

    AUTH_USERS = set(

        int(x) for x in get_config(

            "AUTH_USERS", "6198858059 6265459491"

        ).split()

    )

# array , simplest method was AUTH_USERS = [] ; AUTH_USERS.append(your telegram id) 🤣

    # array to store the channel ID who are authorized to use the bot

    # dont u fucking remove this id 😤

    TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", "6000215739:AAH9N3HsUgkpZhwVYq2HB8Bm6S67-3lzcg0")

    # the download location, where the HTTP Server runs

    DOWNLOAD_LOCATION = get_config("DOWNLOAD_LOCATION", "downloads/")

    # Telegram maximum file upload size

    BOT_USERNAME = get_config("BOT_USERNAME", "VideoCompressXBot")

    MAX_FILE_SIZE = 2097152000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 2097152000

    # default thumbnail to be used in the videos

    DEF_THUMB_NAIL_VID_S = get_config("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    # proxy for accessing youtube-dl in GeoRestricted Areas

    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061

    HTTP_PROXY = get_config("HTTP_PROXY", None)

    # maximum message length in Telegram

    MAX_MESSAGE_LENGTH = 4096

    # add config vars for the display progress

    FINISHED_PROGRESS_STR = get_config("FINISHED_PROGRESS_STR", "◻️")

    UN_FINISHED_PROGRESS_STR = get_config("UN_FINISHED_PROGRESS_STR", "◼️")

    LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "Log.txt")

      # because, https://t.me/c/1494623325/5603
