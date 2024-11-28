from flask_login import UserMixin
import db


class Cliente(UserMixin):
    def __init__(self, id, nome, email, senha, telefone=None, endereco=None,):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.senha = senha

    @staticmethod
    def get_cliente_by_id(cliente_id):
        connection = db.get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tb_cliente WHERE id = %s", (cliente_id,))
        cliente = cursor.fetchone()
        connection.close()

        if cliente:
            return Cliente(
                cliente['id'], cliente['nome'], cliente['email'],
                cliente['telefone'], cliente['endereco'], cliente['senha']
            )
        return None

    @staticmethod
    def authenticate(email, senha):
        connection = db.get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tb_cliente WHERE email = %s AND senha = %s", (email, senha))
        cliente = cursor.fetchone()
        connection.close()

        if cliente:
            return Cliente(
                cliente['id'], cliente['nome'], cliente['email'],
                cliente['telefone'], cliente['endereco'], cliente['senha']
            )
        return None
