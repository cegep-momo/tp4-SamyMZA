from time import sleep
from view import LCD1602

LCD1602.init(0x27,1)

class View:
    def afficher_message(self, message):
        LCD1602.clear()
        LCD1602.write(1,1,message)
        sleep(1)
        LCD1602.clear()

    def afficher_mesure(self, mesure):
        LCD1602.clear()
        LCD1602.write(1,1,mesure)
        sleep(5)
        LCD1602.clear()