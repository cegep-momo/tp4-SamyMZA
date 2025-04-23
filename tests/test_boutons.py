import unittest
from gpiozero import Device
from gpiozero.pins.mock import MockFactory
from model import Platine

Device.pin_factory = MockFactory()

class TestPlatine(unittest.TestCase):
    def setUp(self):
        self.platine = Platine()

    def test_bouton_demarrer_presse(self):
        self.platine.bouton_demarrer.pin.drive_low()
        self.assertTrue(self.platine.bouton_demarrer.is_active, "bouton démarrer actif (appuyé).")

    def test_bouton_demarrer_non_presse(self):
        self.platine.bouton_demarrer.pin.drive_high()
        self.assertFalse(self.platine.bouton_demarrer.is_active, "bouton démarrer pas actif (non appuyé).")

    def test_bouton_stop_presse(self):
        self.platine.bouton_stop.pin.drive_low()
        self.assertTrue(self.platine.bouton_stop.is_active, "bouton stop actif (appuyé).")

    def test_bouton_stop_non_presse(self):
        self.platine.bouton_stop.pin.drive_high()
        self.assertFalse(self.platine.bouton_stop.is_active, "bouton stop pas actif (non appuyé).")

    def test_capteur_distance(self):
        self.platine.capteur.distance = 1.5  
        self.assertEqual(self.platine.capteur.distance, 1.5, "La distance mesurée = 1.5 m.")

if __name__ == "__main__":
    unittest.main()
