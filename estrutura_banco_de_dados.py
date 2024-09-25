from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Criar a API Flask
app = Flask(__name__)

# Configurações da aplicação e conexão com o banco de dados
app.config['SECRET_KEY'] = 'FSD2323f#$!SAH'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.wvjhtgndchihgsqcmqhj:171157Bia%40endrick@aws-0-us-west-1.pooler.supabase.com:6543/postgres'


db = SQLAlchemy(app)

# Definir a estrutura da tabela Postagem
class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))

# Definir a estrutura da tabela Autor
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')

# Inicializar o banco de dados
def inicializar_banco():
    with app.app_context():
        db.drop_all()  # Limpa o banco de dados (opcional)
        db.create_all()  # Cria as tabelas
        autor = Autor(nome='elvis', email='elvismsouza18@gmail.com', senha='123456', admin=True)
        db.session.add(autor)
        db.session.commit()

if __name__ == '__main__':
    inicializar_banco()
