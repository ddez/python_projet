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

def main():
    data.manage_data()  # Vérifie et gère le fichier de données
    choix = menus.main_menu()
    

    match choix:
        case "afficher_stock":
            afficher_stock()
        case "ajouter_munitions":
            print("Ajout de munitions...")
        case "retirer_munitions":
            print("Retrait de munitions...")
        case "changer_chemin":
            print("Changement du chemin du fichier de données...")
        case "changer_qte_max":
            print("Changement de la quantité maximale par article...")
        case "changer_ratio":
            print("Changement du ratio de munitions...")
        case 0:
            print("Au revoir !")
        case _:
            pass # C'est le menu qui gere les erreurs de choix
        
if __name__ == '__main__':
    main()