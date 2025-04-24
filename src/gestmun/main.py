import data
import menus

def main():
    data.manage_data()  # Vérifie et gère le fichier de données
    choix = menus.main_menu()
    
if __name__ == '__main__':
    main()