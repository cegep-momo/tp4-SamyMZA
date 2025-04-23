from model import platine
from model import mesure
from controler import controler
from view import view

# Initialisation des composants
platine = platine()
view = view()
controleur = controler(platine, view)

