import os
import telebot
from dotenv import load_dotenv
from threading import Thread

load_dotenv()
token = os.getenv('AUTH_TOKEN')
user_id = os.getenv('USER_ID')

class Bot():
  def __init__(self, token, user_id, hierarchy):
    self.token = token
    self.user_id = user_id
    self.bot = telebot.TeleBot(token)  # creating a instance
    self.hierarchy = hierarchy
    bot = self.bot

    @bot.message_handler(commands=['log'])
    def send_log(message):
      bot.reply_to(message, "Em desenvolvimento...")
    
    @bot.message_handler(commands=['commands'])
    def send_commands(message):
      bot.reply_to(message, "/log\n/commands")

  def send_message(self, msg):
    self.bot.send_message(self.user_id, msg)
  
  def alive(self):
    if self.hierarchy == 0:
      return
    else:
      self.bot.polling()


tb = Bot(token, user_id, 1)

tb.send_message('Init Bot')

t1 = Thread(target=tb.alive)
t1.start()
