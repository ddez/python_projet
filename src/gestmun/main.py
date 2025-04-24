import data
import menus

def afficher_stock():
    """
    Affiche le stock de munitions.
    """
    print("\n----- STOCK DE MUNITIONS -----")
    munitions = data.get_data()
    if data:
        for munition in munitions:
            #répeter un nombre de caratères
            
            print(f"{munition['munition']:<20} {munition['quantity']:<10}")
    else:
        print("Aucune donnée disponible.")
    print("------------------------------")

def ajouter_munitions():
    """
    Ajoute des munitions au stock.
    """
    print("Ajout de munitions...")
    # Implémentez la logique pour ajouter des munitions ici
def retirer_munitions():
    """
    Retire des munitions du stock.
    """
    print("Retrait de munitions...")
    # Implémentez la logique pour retirer des munitions ici
def changer_chemin():
    """
    Change le chemin du fichier de données.
    """
    print("Changement du chemin du fichier de données...")
    # Implémentez la logique pour changer le chemin ici
def changer_qte_max():
    """
    Change la quantité maximale par article.
    """
    print("Changement de la quantité maximale par article...")
    # Implémentez la logique pour changer la quantité maximale ici
def changer_ratio():
    """
    Change le ratio de munitions.
    """
    print("Changement du ratio de munitions...")
    # Implémentez la logique pour changer le ratio ici  

def main():
    data.manage_data()  # Vérifie et gère le fichier de données
    choix = menus.main_menu()
    

    match choix:
        case "afficher_stock":
            afficher_stock()
        case "ajouter_munitions":
            ajouter_munitions()
        case "retirer_munitions":
            retirer_munitions()
        case "changer_chemin":
            changer_chemin()
        case "changer_qte_max":
            changer_qte_max()
        case "changer_ratio":
            changer_ratio()
        case 0:
            print("Au revoir !")
        case _:
            pass # C'est le menu qui gere les erreurs de choix
        
if __name__ == '__main__':
    main()