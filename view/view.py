import LCD1602

class View:
    def afficher_message(self, message):
        """
        Affiche un message � l'utilisateur.
        :param message: Message � afficher.
        """
        print(message)

    def afficher_mesure(self, mesure):
        """
        Affiche une mesure sp�cifique.
        :param mesure: Instance de la classe Mesure.
        """
        print(f"Mesure enregistr�e : {mesure}")

    def afficher_toutes_les_mesures(self, mesures):
        """
        Affiche toutes les mesures stock�es.
        :param mesures: Liste des mesures.
        """
        if not mesures:
            print("Aucune mesure n'a �t� enregistr�e.")
        else:
            print("Liste des mesures enregistr�es :")
            for i, mesure in enumerate(mesures, start=1):
                print(f"{i}. {mesure}")

    def afficher_erreur(self, erreur):
        """
        Affiche un message d'erreur.
        :param erreur: Message d'erreur.
        """
        print(f"Erreur : {erreur}")
