from typing import Any
from datetime import datetime

class Log():
  def __init__(self) -> None:
      pass
  
  def verify_txt(self):
    """[Function to verify if the file exists]
    """
    try:                                                                    
        open("relatorio.txt", "r")                                     
    except:
        now = datetime.now()
        date = now.strftime("%d/%m/%Y")
        with open("relatorio.txt", "w") as f:
          f.write(f'|------------------------------------------------|\n')
          f.write(f'|                                                |\n')
          f.write(f'|            Relátorio de Inferências            |\n')
          f.write(f'|                                                |\n')
          f.write(f'|------------------------------------------------|')

          f.write(f'\n|------------------------------------------------|\n')
          f.write(f'|                 DIA {date}                 |\n')
          f.write(f'|------------------------------------------------|')

  def update_inference(self, detection: str, accuracy: int, camera: str):
    """Function to update the log with the new inference

    Args:
        detection (str): String with the detection
        accuracy (int): Integer with the accuracy of the detection
        camera (str): String with the name of the camera
    """
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")

    with open("relatorio.txt", "a") as f:
      f.write(f'\n\n------------------------------------------------\n')
      f.write(f'                Última detecção: {detection}\n')
      f.write(f'------------------------------------------------\n')
      f.write(f'\n    Data: {date}  -  Horário: {time}\n\n')
      f.write(f'    Câmera: {camera}\n\n')
      f.write(f'    Detectado(s): {detection}\n\n')
      f.write(f'    Acurácia(s): {accuracy}\n')
  
  def update_date(self):
    """Function to update the date of the log
    """
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    with open("relatorio.txt", "a") as f:
      f.write(f'\n|------------------------------------------------|\n')
      f.write(f'|                 DIA {date}                 |\n')
      f.write(f'|------------------------------------------------|')
  
  def send_log(self):
    """Function to send the log to the admin
    """
    with open("relatorio.txt", "rb") as f:
      return f.read()