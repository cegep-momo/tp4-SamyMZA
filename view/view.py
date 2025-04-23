from time import sleep
import LCD1602

class View:
    def afficher_message(self, message):
        LCD1602.clear()
        LCD1602.write(message)
        sleep(5)
