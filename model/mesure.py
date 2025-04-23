import codecs
from datetime import datetime
import json

class Mesure:
    def __init__(self, distance):
        self.date_heure = datetime.now()
        self.distance = distance 

    def __repr__(self):
        return f"Mesure(date_heure={self.date_heure}, distance={self.distance} cm)"

    def afficher_mesure(self):
        return f"Mesure prise le {self.date_heure.strftime('%Y-%m-%d %H:%M:%S')} : {self.distance} cm"

    def sauvegarderJson(self):
        try:
            with open("donnes.json", "r") as file:
                liste = json.load(file).get("resultats", [])
        except (FileNotFoundError, json.JSONDecodeError):
            liste = []
    

        donnees = {
                "date donne": str(self.date_heure),
                "mesure donee":self.distance,
                }
        
        with codecs.open("donnes.json","w",encoding='utf-8') as json_fichier:
            liste.append(donnees)
            json.dump({"resultats":liste}, json_fichier, ensure_ascii=False, indent=4, sort_keys=False)