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
    print("\n----- Ajout de munitions... -----")
    # charger le stock
    
    munitions = data.get_data()
    # obtenir le prochain id
    next_id  = max([int(munition['id']) for munition in munitions]) + 1
    print(f"Prochain ID : {next_id}")
    # obtenir le nom de la munition
    nom_munition = input("Entrez le nom de la munition : ")
    # vérifier si la munition existe déjà:
        # si oui : on met à jour la quantité
        # si non : on ajoute la munition
    # vérifier si la munition existe déjà
    for munition in munitions:
        if munition['munition'] == nom_munition:
            # mettre à jour la quantité
            print(f"La munition {munition['munition']} existe déjà.")
            print(f"Quantité actuelle : {munition['quantity']}")
            qte_munition = int(input("Entrez la quantité à ajouter : "))
            munition['quantity'] += qte_munition
            break
    else:
        # ajouter la munition
        qte_munition = int(input("Entrez la quantité pour cette munition : "))
        new_munition = {
            "id": str(next_id),
            "munition": nom_munition,
            "quantity": qte_munition
        }
        munitions.append(new_munition)  
    # sauvegarder le stock
    data.push_data(munitions)
    print(f"Ajout de {qte_munition} munitions de type {nom_munition} au stock.")
    print("------------------------------")
    
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