import random

# Paramètres pour générer le stock
TOTAL_STOCK = 100000  # Le nombre total d'unités de munitions à générer
MAX_QUANTITY_PER_ITEM = 1000  # Le nombre maximum d'unités pour chaque type de munition

# Liste des munitions avec leurs PUR (Prix Unitaire de Référence)
munitions = {
    "9mm": 0.5,
    "5.56mm NATO": 0.8,
    "7.62mm NATO": 1.2,
    "12 Gauge": 0.6,
    "0.40 S&W": 0.7,
    "0.22 LR": 0.3,
    "10mm Auto": 1.0,
    "44 Magnum": 1.5,
    "300 Win Mag": 2.0,
    "9mm Luger": 0.55,
    "223 Remington": 0.75,
    "357 Magnum": 1.2,
    "12 Gauge Slug": 1.4,
    "40mm Grenade": 3.5,
    "RPG-7 Rocket": 6.0,
    "M72 LAW Rocket": 5.5,
    "AT4 Rocket": 7.0,
    "TOW Missile": 20.0,
    "Hellfire Missile": 25.0,
    "Javelin Missile": 30.0,
    "S-300 Missile": 100.0,
    "V2 Rocket": 50.0,
    "SCUD Missile": 70.0,
    "Tomahawk Missile": 60.0,
    "Nuclear Warhead": 1000.0
}

# Calcul du stock total disponible en fonction des prix unitaires de référence (nommé ratio)
# On va multiplier le PUR inverse pour avoir des stocks cohérents
def generate_stock(total_stock):
    stock = []  # Liste pour stocker les munitions et leurs quantités
    total_ratio = sum(1 / ratio for ratio in munitions.values())
    
    for i, (munition, ratio) in enumerate(munitions.items()):
        # Calculer le "poids" de chaque munition basé sur son ratio inverse
        poids = (1 / ratio) / total_ratio
        
        # Déterminer la quantité en fonction du poids
        quantity = int(poids * total_stock)
        
        # S'assurer que la quantité ne dépasse pas une limite raisonnable
        quantity = min(quantity, MAX_QUANTITY_PER_ITEM)
        
        # Ajouter l'élément au stock sous forme de dictionnaire
        stock.append({
            "id": str(i),
            "munition": munition,
            "quantity": quantity,
            "PUR": ratio  # Prix Unitaire de Référence
        })
        
    return stock

# # Générer un stock réaliste
# stock_munitions = generate_stock(TOTAL_STOCK)

# # Afficher le stock généré
# for munition in stock_munitions:
#     print(f"{munition['id']} \t {munition['munition']} \t\t\t QTE: {munition['quantity']}")
