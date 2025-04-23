from gpiozero import Button, DistanceSensor

class Platine:
    def __init__(self):
        self.bouton_demarrer = Button(19)
        self.bouton_stop = Button(26)
        self.capteur = DistanceSensor(echo=12, trigger=13, max_distance=3)
