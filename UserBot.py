# import sys
# sys.path.append("..")

# from bot_jaguar.index import *
from index import *

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

  def send_alert(self, detection: str, accuracy: int, img: Any, camera: str):
    """Function to send alerts to the user when the IA detects something

    Args:
        detection (str): String with the detection
        accuracy (int): Accuracy of the detection
        img (Any): Image with the detection
        camera (str): Name of the camera
    """
    sendDetection = ''

    try:
      for i in range(len(detection)):
        sendDetection += '  + ' + detection[i] + ' - ' + str(accuracy[i]) + '%' + '\n '

      self.bot.send_message(
          self.user_id, '⚠️⚠️⚠️⚠️ ALERTA ⚠️⚠️⚠️⚠️\n\n' f'Camêra: {camera}\n\n' f'Detecções:\n\n {sendDetection}')
      
      self.bot.send_photo(self.user_id, img)
    except:
      pass
  
  def send_isAlive(self, camera: str):
    """Funtion to test if the bot is alive
    """
    self.bot.send_message(self.user_id, f'Câmera: {camera} - Serviço ativo!')

