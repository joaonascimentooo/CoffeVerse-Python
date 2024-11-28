from flask import render_template
from db import get_db_connection  # Importa a função de conexão do banco

def register_routes(app):
    @app.route('/empresas')
    def index():
        # Recupera as empresas do banco de dados
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tb_empresa")
        empresas = cursor.fetchall()
        cursor.close()
        connection.close()

        # Renderiza o template com as empresas
        return render_template('empresas.html', empresas=empresas)
    
    @app.route('/')
    def home():
        return render_template('home.html')
