from model.platine import Platine
from model.mesure import Mesure
from view.view import View

class controler:
    def __init__(self):
        self.platine = Platine()
        self.view = View()

    def demarrer(self):
        
        self.view.afficher_message("Attente de demmarrage")
        while True:
            if self.platine.bouton_demarrer.is_pressed:
                
                self.view.afficher_message("Mesure en cours...")
                
                while not self.platine.bouton_stop.is_pressed:
                    
                    
                    distance = self.platine.capteur.distance * 100
                    self.view.afficher_mesure(f"Mesure {distance}")
                    
                    
                    if self.platine.bouton_demarrer.is_pressed:
                        mes = Mesure(distance)
                        mes.sauvegarderJson()
                        break
                        
            if self.platine.bouton_stop.is_pressed:
                self.view.afficher_message("Mesure arrete.")
                break      