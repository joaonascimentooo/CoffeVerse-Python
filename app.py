from flask import Flask
from views.routes import register_routes  # Função para registrar rotas
from flask_login import LoginManager
from models.cliente import Cliente

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Necessário para sessões no Flask-Login

# Configuração do Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Cliente.get_cliente_by_id(user_id)

# Registro das rotas
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
