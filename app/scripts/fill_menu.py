import os
import sys
import pandas as pd
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.menu import Menu

# Garantir que o diretório raiz esteja no PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

def load_menu_data():
    """
    Lê os dados do arquivo CSV na mesma pasta e insere no banco de dados.
    """
    try:
        # Caminho para o arquivo na mesma pasta do script
        file_path = os.path.join(os.path.dirname(__file__), "menu.csv")

        # Verificar se o arquivo existe
        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"Arquivo '{file_path}' não encontrado. Certifique-se de que ele está na mesma pasta que este script."
            )

        # Ler o arquivo CSV
        print(f"Lendo arquivo: {file_path}")
        df = pd.read_csv(file_path)

        # Verificar se as colunas necessárias estão no CSV
        required_columns = [
            "Refeição", "Data", "Opção 1", "Opção 2", "Opção Vegana",
            "Opção Vegetariana", "Salada 1", "Salada 2", "Guarnição",
            "Acompanhamento 1", "Acompanhamento 2", "Acompanhamento 3",
            "Suco", "Sobremesa", "Café", "Pão"
        ]
        for column in required_columns:
            if column not in df.columns:
                raise ValueError(f"Coluna obrigatória '{column}' não encontrada no arquivo CSV.")

        # Conectar ao banco de dados
        db: Session = SessionLocal()

        # Inserir dados no banco
        print("Inserindo dados no banco...")
        for _, row in df.iterrows():
            try:
                menu_entry = Menu(
                    meal=row["Refeição"],
                    date=pd.to_datetime(row["Data"], format="%d").date(),
                    option_1=row.get("Opção 1", None),
                    option_2=row.get("Opção 2", None),
                    vegan_option=row.get("Opção Vegana", None),
                    vegetarian_option=row.get("Opção Vegetariana", None),
                    salad_1=row.get("Salada 1", None),
                    salad_2=row.get("Salada 2", None),
                    garnish=row.get("Guarnição", None),
                    side_1=row.get("Acompanhamento 1", None),
                    side_2=row.get("Acompanhamento 2", None),
                    side_3=row.get("Acompanhamento 3", None),
                    juice=row.get("Suco", None),
                    dessert=row.get("Sobremesa", None),
                    coffee=row.get("Café", None),
                    bread=row.get("Pão", None),
                )
                db.add(menu_entry)
            except Exception as row_error:
                print(f"Erro ao processar linha {row}: {row_error}")

        db.commit()
        print("Dados inseridos com sucesso!")

    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")

    finally:
        db.close()
        print("Conexão com o banco de dados fechada.")


if __name__ == "__main__":
    # Executa o carregamento dos dados
    load_menu_data()
