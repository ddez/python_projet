import data, menus, settings
from logger_config import setup_logger
import logging

# Initialize logging system at the very start
root_logger = setup_logger()
logger = logging.getLogger(__name__)


def afficher_stock(id=False, nom=True, qte=False, pur=False):
    """
    Affiche le stock de munitions avec les informations sélectionnées.

    Args:
        id (bool): Affiche l'identifiant si True
        nom (bool): Affiche le nom de la munition si True
        qte (bool): Affiche la quantité si True
        pur (bool): Affiche le Prix Unitaire de Référence si True

    Note:
        Les colonnes sont formatées avec une largeur fixe pour un alignement propre
    """
    print("\n----- STOCK DE MUNITIONS -----")
    munitions = data.get_data()
    if data:
        for munition in munitions:
            message = ""
            if id:
                message = f"{munition['id']:<5}"
            if nom:
                message += f"{munition['munition']:<20}"
            if qte:
                message += f"{munition['quantity']:<10}"
            if pur:
                message += f"{munition['PUR']:<10}"
            print(message)
    else:
        print("Aucune donnée disponible.")
    print("------------------------------")

def ajouter_munitions():
    """
    Ajoute des munitions au stock ou met à jour la quantité existante.

    Le processus suit ces étapes:
    1. Récupération du prochain ID disponible
    2. Saisie du nom de la munition
    3. Si la munition existe:
       - Met à jour la quantité existante
    4. Si nouvelle munition:
       - Crée une nouvelle entrée avec ID, nom, quantité et PUR
    5. Sauvegarde les modifications

    Logs:
        INFO: Création ou mise à jour de munitions
    """
    print("\n----- Ajout de munitions... -----")
    munitions = data.get_data()
    next_id = max([int(munition['id']) for munition in munitions]) + 1
    
    nom_munition = input("Entrez le nom de la munition : ")
    
    # Recherche si la munition existe déjà
    for munition in munitions:
        if munition['munition'] == nom_munition:
            print(f"La munition {munition['munition']} existe déjà.")
            print(f"Quantité actuelle : {munition['quantity']}")
            qte_munition = int(input("Entrez la quantité à ajouter : "))
            munition['quantity'] += qte_munition
            logger.info(f"Ajout de {qte_munition} munitions au stock existant de {nom_munition}")
            break
    else:
        qte_munition = int(input("Entrez la quantité pour cette munition : "))
        new_munition = {
            "id": str(next_id),
            "munition": nom_munition,
            "quantity": qte_munition,
            "PUR": float(input("Entrez le PUR (Prix Unitaire de Référence) en € : "))
        }
        munitions.append(new_munition)
        logger.info(f"Création nouveau type munition: {nom_munition} avec quantité initiale: {qte_munition}")

    data.push_data(munitions)
    print(f"Ajout de {qte_munition} munitions de type {nom_munition} au stock.")
    print("------------------------------")

def retirer_munitions():
    """
    Retire des munitions du stock.

    Le processus suit ces étapes:
    1. Affichage du stock actuel
    2. Saisie de l'ID de la munition à retirer
    3. Vérification de l'existence de la munition
    4. Saisie de la quantité à retirer
    5. Vérification de la quantité disponible
    6. Mise à jour du stock
    7. Sauvegarde des modifications

    Logs:
        WARNING: Tentative de retrait excessive
        INFO: Retrait de munitions
        ERROR: Tentative de retrait d'une munition inexistante
    """
    print("\n----- Retrait de munitions... -----")
    munitions = data.get_data()
    afficher_stock(id=True, nom=True, qte=True, pur=True) 
    id_munition = input("Entrez l'ID de la munition à retirer : ")
    
    for munition in munitions:
        if munition['id'] == id_munition:
            qte_munition = int(input("Entrez la quantité à retirer : "))
            if qte_munition > munition['quantity']:
                logger.warning(f"Tentative de retrait excessive pour {munition['munition']} - Demandé: {qte_munition}, Disponible: {munition['quantity']}")
                print(f"Quantité insuffisante. Quantité actuelle : {munition['quantity']}")
                break
            else:
                ancienne_qte = munition['quantity']
                munition['quantity'] -= qte_munition
                logger.info(f"Retrait de {qte_munition} munitions de {munition['munition']} (Stock: {ancienne_qte}->{munition['quantity']})")
                break
    else:
        logger.error(f"Tentative de retrait d'une munition inexistante (ID: {id_munition})")
        print("Munition non trouvée.")
    
    data.push_data(munitions)
    print("------------------------------")
    verifier_stocks_faibles()

def verifier_stocks_faibles():
    """
    Vérifie si des munitions sont en quantité faible en tenant compte de leur PUR (prix unitaire de référence).
    Les seuils sont calculés comme suit:
    - Munitions à PUR très élevé (>500€) : seuil = 1
    - Munitions à PUR élevé (50-500€) : seuil = 4
    - Munitions à PUR moyen (5-50€) : seuil = 10
    - Munitions à PUR faible (<5€) : seuil = 100

    Affiche une alerte pour chaque munition en dessous du seuil et indique le seuil minimal requis.

    Logs:
        WARNING: Stock critique
    """
    print("\n----- ALERTE STOCKS FAIBLES -----")
    munitions = data.get_data()
    stocks_faibles = False
    
    for munition in munitions:
        pur = float(munition.get('PUR', 0))
        
        if pur >= 500:
            seuil = 1  
        elif 50 <= pur < 500:
            seuil = 4
        elif 5 <= pur < 50:
            seuil = 10
        else:
            seuil = 100
            
        if munition['quantity'] <= seuil:
            stocks_faibles = True
            logger.warning(f"Stock critique pour {munition['munition']}: {munition['quantity']} (PUR: {pur}€)")
            print(f"⚠️ ATTENTION: {munition['munition']} - Quantité: {munition['quantity']}")
            print(f"    Seuil minimal: {seuil} (PU.ref: {pur}€)")
    
    if not stocks_faibles:
        print("Aucun stock faible détecté.")
    print("--------------------------------")


def prevision(munition):
    """
    Fonction "prevision" pour proposer de recommander des munitions si le stock est faible.
    Cette fonction est appelée dans verifier_stocks_faibles();
    Elle prend en paramètre une munition.
    Elle analyse les logs et propose de commander du stock en fonction des retraits récents et des stocks actuels;       
    """
    pass # En construction...
  

def main():
    """
    Point d'entrée principal du programme de gestion des munitions.

    Fonctionnalités:
    - Initialisation du système de logging
    - Vérification des données au démarrage
    - Contrôle des stocks faibles
    - Gestion du menu principal et des actions utilisateur
    - Journalisation des connexions/déconnexions

    Returns:
        None
    """
    logger.info("Connecté")
    data.manage_data()
    verifier_stocks_faibles()

    choix = -1
    while choix != 0:
        choix = menus.main_menu()
        match choix:
            case "afficher_stock":
                afficher_stock(id=False, nom=True, qte=True)
            case "ajouter_munitions":
                ajouter_munitions()
            case "retirer_munitions":
                retirer_munitions()
            case "changer_chemin":
                settings.changer_chemin()
            case "changer_qte_max":
                settings.changer_qte_max()
            case "changer_ratio":
                settings.changer_ratio()
            case 0:
                print("Au revoir !")
            case _:
                pass # C'est le menu qui gere les erreurs de choix
    
    logger.info("Déconnexion")
        
if __name__ == '__main__':
    main()