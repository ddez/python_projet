import data
import menus



def main():
    data.manage_data()  # Vérifie et gère le fichier de données
    choix = menus.main_menu()
    
    match choix:
        case "afficher_stock":
            print("Affichage du stock...")
        case "ajouter_munitions":
            print("Ajout de munitions...")
        case "retirer_munitions":
            print("Retrait de munitions...")
        case "settings":
            print("Paramètres...")
        case 0:
            print("Au revoir !")
        case _:
            pass # C'est le menu qui gere les erreurs de choix
        
if __name__ == '__main__':
    main()