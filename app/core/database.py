from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar variáveis de conexão com o banco de dados
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "ru_app")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")

# Montar a URL de conexão
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Criar o engine de conexão com o banco
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Criar uma fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base (base para definir os modelos)
Base = declarative_base()

def get_db():
    """
    Gerenciador de dependência para injetar uma sessão do banco de dados.
    Retorna uma sessão ativa e a encerra ao final do uso.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
