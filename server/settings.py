import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

load_dotenv()
# load_dotenv(os.path.join(BASE_DIR, '.env'))

DEBUG = True
ASYNC_DATABASE_URL = os.getenv("ASYNC_DATABASE_URL")
DATABASE_URL = os.getenv("DATABASE_URL")

REDIS_DB_URL = os.getenv("REDIS_DB_URL")

# 短信验证码过期秒数
SMS_EXPIRED_SECONDS = 300
