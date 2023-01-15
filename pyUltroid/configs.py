# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

import sys

from decouple import config

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class Var:
    # mandatory
    API_ID = (
        int(sys.argv[1]) if len(sys.argv) > 1 else config("17674920", default=6, cast=int)
    )
    API_HASH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else config("API_HASH", default="4c55df5c8d646c88aa4bbe177761117c")
    )
    SESSION = sys.argv[3] if len(sys.argv) > 3 else config("BQBQeqhDKj0Afpt9cH4u_C48Ken7lfgi3HyJnszr-aASSkvEDXRWRIhO1FqKJhJb11B7kOykAJyIH7ghFbYIVP82He38DmgRu7qN-wUYexJ3p-HR62mT7DWGs_UfS1-lpPUjofRxQ3B5xwiqj9nNr5I_q_uB0vbPD5WuKbvt15TpvQzDrS0UdKEITphs_YDDI25T0gdS-TstZyBUPk7LlmVOjyjBx_VLO8cqfhif1P5oeSZnfpcir6Dd32x7boWGEZS5w9EKufqrJjoc2-2-9c2q0cU9cFPZaRGhn4bsy5qxtMl9_A1JKCSJpOh9mlo09sUb3LAFUngS1nxU3NX7wb6eAAAAAUAyzEEA", default=None)
    REDIS_URI = (
        sys.argv[4]
        if len(sys.argv) > 4
        else (config("REDIS_URI", default=None) or config("redis-15158.c273.us-east-1-2.ec2.cloud.redislabs.com:15158", default=None))
    )
    REDIS_PASSWORD = (
        sys.argv[5] if len(sys.argv) > 5 else config("bcHxIJLL86YxXZL5AJWB2o9BYs1cSIdI", default=None)
    )
    # extras
    BOT_TOKEN = config("5856053493:AAHpbSwhYWHsTPkyOWnx4QSPqGVn5fsDibE", default=None)
    LOG_CHANNEL = config("-1001761877962", default=0, cast=int)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
    HEROKU_API = config("HEROKU_API", default=None)
    VC_SESSION = config("VC_SESSION", default=None)
    ADDONS = config("ADDONS", default=False, cast=bool)
    VCBOT = config("VCBOT", default=False, cast=bool)
    # for railway
    REDISPASSWORD = config("REDISPASSWORD", default=None)
    REDISHOST = config("REDISHOST", default=None)
    REDISPORT = config("REDISPORT", default=None)
    REDISUSER = config("REDISUSER", default=None)
    # for sql
    DATABASE_URL = config("DATABASE_URL", default=None)
    # for MONGODB users
    MONGO_URI = config("MONGO_URI", default=None)
