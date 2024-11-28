import mysql.connector

def get_db_connection():
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',  # Altere conforme necessário
        'database': 'coffeverse'
    }
    connection = mysql.connector.connect(**db_config)
    return connection
