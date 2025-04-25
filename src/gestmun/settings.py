import logging

# Get logger for this module - no need to setup again
logger = logging.getLogger(__name__)

def changer_chemin():
    """
    Change le chemin du fichier de données.
    """
    print("Changement du chemin du fichier de données...")

    # logger le message "Tentative de changement du chemin... en construction..."
    logger.info("Tentative de changement du chemin... en construction...")

def changer_qte_max():
    """
    Change la quantité maximale par article.
    """
    print("Changement de la quantité maximale par article...")
    logger.info("Tentative de changement de la quantité maximale... en construction...")
def changer_ratio():
    """
    Change le ratio de munitions.
    """
    print("Changement du ratio de munitions...")
    logger.info("Tentative de changement du ratio... en construction...")
