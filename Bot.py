# import sys
# sys.path.append("..")

# from bot_jaguar.index import *
from index import *
from log.log import Log

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

  def send_alert(self, detection: Any, accuracy: Any, img: Any, camera: str):
    """Function to send alerts to the user when the IA detects something

    Args:
        detection (str): String with the detection
        accuracy (int): Accuracy of the detection
        img (Any): Image with the detection
        camera (str): Name of the camera
    """
    sendDetection = ''
    print(self.user_id, self.user_token)
    try:
      for i in range(len(detection)):
        sendDetection += '  + ' + detection[i] + ' - ' + str(accuracy[i]) + '%' + '\n '

      self.bot.send_message(
          self.user_id, '⚠️⚠️⚠️⚠️ ALERTA ⚠️⚠️⚠️⚠️\n\n' f'Camêra: {camera}\n\n' f'Detecções:\n\n {sendDetection}')
      
      self.bot.send_photo(self.user_id, img)
    except Exception as e:
      print(e)
      pass
  
  def send_isAlive(self, camera: str):
    """Funtion to test if the bot is alive
    """
    self.bot.send_message(self.user_id, f'Câmera: {camera} - Serviço ativo!')

class AdminBot(UserBot, Log):
  def __init__(self, token_admin: str, admin_id: str, log=False):
    """Class used to send receive comands, send alerts and log for
    the admin

    Args:
        token_admin (str): Admin bot token
        admin_id (str): Id of the admin
        log (bool, optional): If you want to update the log
        when sending new messages send True. Defaults to False.
    """
    self.token_admin = token_admin
    self.admin_id = admin_id
    self.log = log
    super(AdminBot, self).__init__(token_admin, admin_id)

    bot = self.bot

    if self.log:
      super().verify_txt()

    @bot.message_handler(commands=['log'])
    def send_log(message):
      try:
        bot.send_document(self.admin_id, self.send_log())
        # bot.send_message(self.admin_id, self.send_log())
      except:
        pass

    @bot.message_handler(commands=['help'])
    def send_commands(message):
      bot.reply_to(message, "/log\n/help")

  def alive(self):
    """This function is used to keep listening admin requests to bot
    """
    self.bot.polling()

  def send_log(self):
    """Funtion to send the log to the admin
    """
    return super().send_log()

  def update_log_date(self):
    """Funtion to update the date in the log
    """
    return super().update_date()

