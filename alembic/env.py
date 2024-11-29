from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from app.core.database import Base  # Importa a Base dos modelos
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv()

# Configuração do Alembic
config = context.config

# Adicionar a URL do banco de dados do .env ao arquivo de configuração
database_url = os.getenv("DATABASE_URL", "")
if not database_url:
    raise ValueError("A variável de ambiente 'DATABASE_URL' não está definida.")
config.set_main_option('sqlalchemy.url', database_url)


# Configurar logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Define o metadata do SQLAlchemy para autogenerate
from app.models.menu import Menu  # Importe todos os modelos necessários
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Executar migrações no modo 'offline'."""

    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Executar migrações no modo 'online'."""

    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True  # Permite detectar mudanças no tipo de coluna
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
