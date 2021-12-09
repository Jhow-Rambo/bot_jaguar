from .bot import Bot
from threading import Thread
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('AUTH_TOKEN')
user_id = os.getenv('USER_ID')

tb = Bot(token, user_id, 1)

tb.send_message('Init Bot')

t1 = Thread(target=tb.alive)
t1.start()