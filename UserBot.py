import sys
sys.path.append("..")

from bot_jaguar.index import *
#--------------------------------------------------------------------------------------------------#
class UserBot():
  def __init__(self, user_token: str, user_id: str):
    """Class used to send receive comands, send alerts and log for
    the user

    Args:
        user_token (str): User bot token
        user_id (str): Id of the user
    """
    self.user_token = user_token
    self.user_id = user_id
    self.bot = telebot.TeleBot(user_token)
    bot = self.bot

    @bot.message_handler(commands=['help'])
    def send_commands(message):
      bot.reply_to(message, "/help\nAinda não há comandos")

  def send_alert(self, detection: str, accuracy: int, img: Any):
    """Function to send alerts to the user when the IA detects something

    Args:
        detection (str): String with the detection
        accuracy (int): Accuracy of the detection
        img (Any): Image with the detection
    """
    try:
      self.bot.send_message(
          self.user_id, '⚠️⚠️⚠️⚠️ ALERTA ⚠️⚠️⚠️⚠️\n\n' f'Detectado: {detection}\n'f'Acurácia: {accuracy}%\n')
      self.bot.send_photo(self.user_id, img)
    except:
      pass
  
  def send_isAlive(self):
    """Funtion to test if the bot is alive
    """
    self.bot.send_message(self.user_id, 'Serviço ativo')

