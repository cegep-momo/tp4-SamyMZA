class Controleur:
    def __init__(self, platine):
        """
        Initialise le contr�leur avec une instance de Platine.
        :param platine: Une instance de la classe Platine.
        """
        self.platine = platine
        self.running = True  # Indique si le programme est en cours d'ex�cution
        self.mesures = []  # Liste pour stocker les mesures

    def gerer_boutons(self):
        """
        G�re les interactions avec les boutons.
        """
        if self.platine.read_button_start():
            print("Bouton START appuy�. D�marrage de la mesure.")
            self.demarrer_mesure()

        if self.platine.read_button_measure():
            print("Bouton MESURE appuy�. Une mesure est effectu�e.")
            self.enregistrer_mesure()

    def demarrer_mesure(self):
        """
        D�marre une s�quence de mesures r�p�t�es.
        """
        for _ in range(3):  # Exemple de 3 mesures
            self.enregistrer_mesure()
            time.sleep(1)  # Pause entre les mesures

    def enregistrer_mesure(self):
        """
        Effectue une mesure et l'enregistre dans la liste des mesures.
        """
        distance = self.platine.measure_distance()
        mesure = Mesure(distance)
        self.mesures.append(mesure)
        print(mesure)

    def boucle_principale(self):
        """
        Boucle principale du contr�leur.
        """
        try:
            print("Appuyez sur CTRL+C pour arr�ter.")
            while self.running:
                self.gerer_boutons()
        except KeyboardInterrupt:
            print("\nArr�t demand� par l'utilisateur.")
        finally:
            self.terminer()

    def terminer(self):
        """
        Nettoie les ressources et termine le programme.
        """
        print("Nettoyage des ressources...")
        self.platine.cleanup()
        print("Programme termin�.")
