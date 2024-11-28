from flask import Flask
from views.routes import register_routes  # Importa função para registrar as rotas

app = Flask(__name__)

# Registra as rotas no app
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
