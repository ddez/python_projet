import sqlite3

DATAPATH = 'assets/data.db'

def create_table():
    """
    Creates the munitions table in the SQLite database if it doesn't exist.
    """
    try:
        con = sqlite3.connect(DATAPATH)
        cur = con.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS munitions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                munition TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                PUR REAL NOT NULL
            )
        ''')
        con.commit()
        print("Table 'munitions' créée avec succès.")
    except sqlite3.Error as e:
        print(f"Erreur lors de la création de la table : {e}")
    finally:
        con.close()
        
def insert_data(munitions):
    """
    Inserts data into the munitions table.

    Args:
        munitions (list): List of dictionaries containing munition data.
    """
    try:
        con = sqlite3.connect(DATAPATH)
        cur = con.cursor()
        for munition in munitions:
            cur.execute('''
                INSERT INTO munitions (munition, quantity, PUR)
                VALUES (?, ?, ?)
            ''', (munition['munition'], munition['quantity'], munition['PUR']))
        con.commit()
        print("Données insérées avec succès.")
    except sqlite3.Error as e:
        print(f"Erreur lors de l'insertion des données : {e}")
    finally:
        con.close()


def fetch_data():
    """
    Fetches all data from the munitions table.

    Returns:
        list: List of dictionaries containing munition data.
    """
    try:
        con = sqlite3.connect(DATAPATH)
        cur = con.cursor()
        cur.execute('SELECT * FROM munitions')
        rows = cur.fetchall()
        columns = [column[0] for column in cur.description]
        data = [dict(zip(columns, row)) for row in rows]
        return data
    except sqlite3.Error as e:
        print(f"Erreur lors de la récupération des données : {e}")
        return []
    finally:
        con.close()
        print("Données récupérées avec succès.")
        print("Fermeture de la connexion à la base de données.")
# if __name__ == '__main__':
#     create_table()
#     # Example data to insert
#     example_data = [
#         {'munition': '9mm', 'quantity': 100, 'PUR': 0.20},
#         {'munition': '5.56mm', 'quantity': 200, 'PUR': 0.30},
#         {'munition': '7.62mm', 'quantity': 150, 'PUR': 0.40}
#     ]
#     insert_data(example_data)

