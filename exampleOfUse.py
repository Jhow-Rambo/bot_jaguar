from logging import log
from AdminBot import AdminBot
from dotenv import load_dotenv
from threading import Thread
import os

#---------- Load the variables ----------#
load_dotenv()
token_admin = os.getenv('ADMIN_TOKEN')
admin_id = os.getenv('ADMIN_ID')

#---------- Create the bot ----------#
tb = AdminBot(token_admin, admin_id, log=True)

#---------- Create the thread to listen user request ----------#
# t1 = Thread(target=tb.alive)
# t1.start()

#---------- Update the date log ----------#
# tb.update_log_date()

#----------      Send Alert   ------------#
tb.send_alert(detection=['pessoa', 'pessoa', 'carro', 'casa'], accuracy=['23', '43', '31', '90'], img=None)

#----------      Send Alive   ------------#
# tb.send_isAlive()

