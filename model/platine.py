from gpiozero import Button, DistanceSensor

bouton_demarrer = Button(19)

bouton_stop = Button(26)

capteur = DistanceSensor(echo=12, trigger=13)

import RPi.GPIO as GPIO
import time

class Platine:
    def __init__(self):
        """
        Initialise les composants de la platine : les boutons et le capteur ultrason.
        """
        # Configuration des broches GPIO
        self.button_start = 12  # Broche du bouton START
        self.button_measure = 16  # Broche du bouton MESURE
        self.trigger = 18  # Broche TRIG du capteur ultrason
        self.echo = 24  # Broche ECHO du capteur ultrason

        # Initialisation des GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.button_start, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.button_measure, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def read_button_start(self):
        """
        V�rifie si le bouton START est appuy�.
        :return: True si le bouton est appuy�, False sinon.
        """
        return GPIO.input(self.button_start) == GPIO.LOW

    def read_button_measure(self):
        """
        V�rifie si le bouton MESURE est appuy�.
        :return: True si le bouton est appuy�, False sinon.
        """
        return GPIO.input(self.button_measure) == GPIO.LOW

    def measure_distance(self):
        """
        Mesure la distance � l'aide du capteur ultrason.
        :return: Distance mesur�e en centim�tres.
        """
        # Envoi d'une impulsion TRIG
        GPIO.output(self.trigger, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger, False)

        # Lecture de l'impulsion ECHO
        while GPIO.input(self.echo) == 0:
            start_time = time.time()

        while GPIO.input(self.echo) == 1:
            stop_time = time.time()

        # Calcul de la distance
        elapsed_time = stop_time - start_time
        distance = (elapsed_time * 34300) / 2  # 34300 cm/s : vitesse du son
        return round(distance, 2)

