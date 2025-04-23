from model import platine
from model import mesure
from view import view

class controler:
    def __init__(self):
        self.platine = platine()
        self.mesure = mesure()
        self.view = view()

    def demarrer(self):
        while True:
            if self.platine.bouton_demarrer.is_pressed:
                self.view.afficher_message("Mesure en cours...")
                if self.platine.boutondemarrer.is_pressed:
                    distance = self.platine.capteur.distance * 100
                    self.view.afficher_message(f"Mesure {distance}")
            if self.platine.bouton_stop.is_pressed:
                self.view.afficher_message("Mesure arrêtée.")
                break        