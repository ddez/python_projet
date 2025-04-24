import json
import generateur # Pour générer un jeu de données réaliste

DATAPATH = 'assets/data.json'

def get_data():
    try:
        with open(DATAPATH, 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier de données : {e}")
        return None
    
def push_data(data):
    try:
        with open(DATAPATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)  # ensure_ascii=False pour conserver les accents
        print("Données mises à jour avec succès.")
        return True
    except Exception as e:
        print(f"Erreur lors de l'écriture dans le fichier de données : {e}")  
        return False 

def check_data():
    """
    Checks if the data file exists and is a valid JSON.

    Returns:
        bool: True if the file exists and is valid JSON, False otherwise.
    """

    try:
        with open(DATAPATH, 'r') as f:
            data = json.load(f)
        return True
    except FileNotFoundError:
        return False
    except json.JSONDecodeError:
        return False

def manage_data():
    """
    Manages the data file. If the file does not exist or is not valid JSON,
    it creates a new file with default data.
    """
    if not check_data():
        recreer_fichier = int(input("Le fichier de données n'existe pas ou est corrompu. Voulez-vous le réinitialiser ? (1: Oui, 0: Non) ") or 1)
        if recreer_fichier == 1:
            qte_stock = int(input("Entrez la quantité de stock à générer (par défaut 10000) : ") or 10000)
            default_data = generateur.generate_stock(qte_stock)  # Exemple de stock total
        else:
            print("Le fichier de données n'a pas été recréé.")
            return
        push_data(default_data)