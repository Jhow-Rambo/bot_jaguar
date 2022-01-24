# import sys
# sys.path.append("..")

# from bot_jaguar.index import *
# from bot_jaguar.log.log import Log
#--------------------------------------------------------------------------------------------------#
from index import *
from log.log import Log

#--------------------------------------------------------------------------------------------------#
class AdminBot(Log):
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
    self.bot = telebot.TeleBot(token_admin)  # creating a instance
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

  def send_alert(self, detection: str, accuracy: int, img: Any, camera: str):
    """Function to send alerts to the admin when the IA detects something

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
    
      if self.log:
        super().update_inference(detection, accuracy, camera)

      self.bot.send_message(
          self.admin_id, '⚠️⚠️⚠️⚠️ ALERTA ⚠️⚠️⚠️⚠️\n\n' f'Camêra: {camera}\n\n' f'Detecções:\n\n {sendDetection}')
      self.bot.send_photo(self.admin_id, img)
    except:
      pass

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
  
  def send_isAlive(self, camera: str):
    """Funtion to test if the bot is alive
    """
    self.bot.send_message(self.admin_id, f'Câmera: {camera} - Serviço ativo!')
