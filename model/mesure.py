from datetime import datetime

class Mesure:
    def __init__(self, distance):
        self.date_heure = datetime.now()
        self.distance = distance 

    def __repr__(self):
        return f"Mesure(date_heure={self.date_heure}, distance={self.distance} cm)"

    def afficher_mesure(self):
        return f"Mesure prise le {self.date_heure.strftime('%Y-%m-%d %H:%M:%S')} : {self.distance} cm"
