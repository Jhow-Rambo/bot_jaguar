#from index import *
from typing import List
import telebot

class AdminBot():
  def __init__(self, token_admin: str, admin_id):
    self.token_admin = token_admin
    self.admin_id = admin_id
    self.bot = telebot.TeleBot(token_admin)  # creating a instance
    bot = self.bot

    @bot.message_handler(commands=['log'])
    def send_log(message):
      bot.reply_to(message, "Em desenvolvimento...")

    @bot.message_handler(commands=['commands'])
    def send_commands(message):
      bot.reply_to(message, "/log\n/commands")

  def send_alert(self, detection, accuracy, img):
    self.bot.send_message(
        self.admin_id, '⚠️⚠️⚠️⚠️ ALERTA ⚠️⚠️⚠️⚠️\n\n' f'Detectado: {detection}\n'f'Acurácia: {accuracy}%\n')
    self.bot.send_photo(self.admin_id, img)
    
  def alive(self):
    self.bot.polling()
