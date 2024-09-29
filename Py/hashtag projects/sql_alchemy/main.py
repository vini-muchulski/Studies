from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

#https://www.youtube.com/watch?v=W-g6StRy1zY


db = create_engine("sqlite:///meu_db.db")
Session = sessionmaker(bind=db)
session = Session()


Base = declarative_base()

#tabelas
class Usuario(Base):
    __tablename__ = "usuarios"
    
    id =  Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    status = Column("status", Boolean)
    
    def __init__(self, nome, email, senha, status=True):
        self.nome = nome
        self.email = email
        self.senha = senha 
        self.status = status
        
        
#Livro
class Livro(Base):
    __tablename__ = "livros"
    
    id =  Column("id", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String)
    autor = Column("autor", String)
    qntd_paginas =   Column("qntd_paginas", Integer)
    dono = Column("dono", ForeignKey("usuarios.id"))
    
    
    def __init__(self, titulo, autor, qntd_paginas, dono):
        self.titulo = titulo
        self.autor = autor
        self.qntd_paginas = qntd_paginas
        self.dono = dono
      
Base.metadata.create_all(bind=db)

#CRUD
#C
"""
usuario = Usuario(nome="vini4", email="abc@gmail.com", senha="123")
session.add(usuario)
session.commit()
"""

#R
lista_usuarios = session.query(Usuario).all()
"""for usuario in lista_usuarios:
    print(usuario.nome)"""
    
usuario_vini = session.query(Usuario).filter_by(nome="vini").first()
print(usuario_vini.nome)
print(usuario_vini.email)
print(usuario_vini.senha)  
    
"""livro = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1000, usuario_vini.id)
session.add(livro)
session.commit()"""

#update
"""usuario_vini.nome = "vinicius w"
session.add(usuario_vini)
session.commit()"""

"""usuario_vini = session.query(Usuario).filter_by(nome="vinicius w").first()
print(usuario_vini.nome)"""

#delete
usuario_vini3 = session.query(Usuario).filter_by(nome="vini3").first()
session.delete(usuario_vini3)
session.commit()