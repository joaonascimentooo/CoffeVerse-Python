from flask import render_template, request, flash, redirect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models.cliente import Cliente
from db import get_db_connection  
#Empresas
def register_routes(app):
    @app.route('/empresas')
    def index():
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tb_empresa")
        empresas = cursor.fetchall()
        cursor.close()
        connection.close()

        return render_template('empresas.html', empresas=empresas)
    
    @app.route('/')
    def home():
        return render_template('home.html')
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            senha = request.form['senha']
            cliente = Cliente.authenticate(email, senha)

            if cliente:
                login_user(cliente)
                flash('Login realizado com sucesso!', 'success')
                return redirect('/empresas')
            else:
                flash('Credenciais inválidas!', 'danger')

        return render_template('login.html')

    @app.route('/empresa/<int:empresa_id>')
    def empresa_detalhes(empresa_id):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM tb_empresa WHERE id = %s", (empresa_id,))
        empresa = cursor.fetchone()
        
        cursor.execute("SELECT * FROM tb_produto WHERE empresa_id = %s", (empresa_id,))
        produtos = cursor.fetchall()
        
        cursor.close()
        connection.close()

        if empresa is None:
            return "Empresa não encontrada", 404

        return render_template('empresa_detalhes.html', empresa=empresa, produtos=produtos)
    
    @app.route('/compra/<int:produto_id>', methods=['GET'])
    def compra(produto_id):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tb_produto WHERE id = %s", (produto_id,))
        produto = cursor.fetchone()  
        cursor.close()
        connection.close()

        if produto is None:
            return "Produto não encontrado", 404  

        return render_template('compra.html', produto=produto)  
    
    @app.route('/finalizar_compra/<int:produto_id>', methods=['POST'])
    def finalizar_compra(produto_id):
        quantidade = request.form['quantidade']
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tb_produto WHERE id = %s", (produto_id,))
        produto = cursor.fetchone()  
        cursor.close()
        connection.close()

        if produto is None:
            return "Produto não encontrado", 404  

        total = produto['preco'] * int(quantidade)

        return render_template('compra_finalizada.html', produto=produto, quantidade=quantidade, total=total)

    
    





