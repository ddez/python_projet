def main_menu():
    """
    Affiche le menu principal et gère les choix de l'utilisateur.
    """

    while True:
        print("\nMenu Principal :")
        
        print("1. Afficher le stock")
        print("2. Ajouter des munitions")
        print("3. Retirer des munitions")
        print("9. Paramètres")
        print("0. Quitter")

        choix = input("Veuillez entrer votre choix : ") or '0'

        match choix:
            case '1':
                return "afficher_stock"
            case '2':
                return "ajouter_munitions"
            case '3':
                return "retirer_munitions"
            case '9':
                settings_page = settings_menu()
                if settings_page == 0:
                    continue
                else:
                    return settings_page
            case '0':
                print("Au revoir !")
                return 0
            case _:
                print("Choix invalide, veuillez réessayer.")

def settings_menu():
    """
    Affiche le menu des paramètres et gère les choix de l'utilisateur.
    """

    while True:
        print("\nMenu des Paramètres :")
        
        print("1. Changer le chemin du fichier de données")
        print("2. Changer la quantité maximale par article")
        print("3. Changer le ratio de munitions")
        print("0. Retour au menu principal")

        choix = input("Veuillez entrer votre choix : ") or '0'

        match choix:
            case '1':
                return "changer_chemin"
            case '2':
                return "changer_qte_max"
            case '3':
                return "changer_ratio"
            case '0':
                return 0
            case _:
                print("Choix invalide, veuillez réessayer.")