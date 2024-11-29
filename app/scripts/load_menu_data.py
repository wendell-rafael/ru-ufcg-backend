import pandas as pd
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from app.core.database import engine  # Certifique-se de que o SQLAlchemy está configurado
from app.models.menu import Menu  # Substitua "Menu" pelo nome do seu modelo


def load_menu_data(file_path: str):
    """
    Carrega os dados de um arquivo CSV e insere no banco de dados.

    Args:
        file_path (str): Caminho do arquivo CSV a ser carregado.
    """
    try:
        # Passo 1: Ler o CSV
        print(f"Lendo arquivo CSV: {file_path}")
        df = pd.read_csv(file_path)

        # Passo 2: Validar os Dados
        # Verificar se todas as colunas necessárias estão presentes
        required_columns = [
            "Refeição", "Data", "Opção 1", "Opção 2", "Opção Vegana",
            "Opção Vegetariana", "Salada 1", "Salada 2", "Guarnição",
            "Acompanhamento 1", "Acompanhamento 2", "Acompanhamento 3",
            "Suco", "Sobremesa", "Café", "Pão"
        ]
        for column in required_columns:
            if column not in df.columns:
                raise ValueError(f"Coluna obrigatória '{column}' está ausente no arquivo CSV.")

        # Converter a coluna 'Data' para o formato de data
        df['Data'] = pd.to_datetime(df['Data'], format='%d', errors='coerce')

        # Passo 3: Processar os Dados
        # Remover linhas com valores nulos na coluna 'Data'
        df = df.dropna(subset=['Data'])

        # Passo 4: Inserir no Banco de Dados
        print("Inserindo os dados no banco de dados...")
        with Session(engine) as session:
            for _, row in df.iterrows():
                menu_entry = Menu(
                    meal=row["Refeição"],
                    date=row["Data"],
                    option_1=row["Opção 1"],
                    option_2=row["Opção 2"],
                    vegan_option=row["Opção Vegana"],
                    vegetarian_option=row["Opção Vegetariana"],
                    salad_1=row["Salada 1"],
                    salad_2=row["Salada 2"],
                    garnish=row["Guarnição"],
                    side_1=row["Acompanhamento 1"],
                    side_2=row["Acompanhamento 2"],
                    side_3=row["Acompanhamento 3"],
                    juice=row["Suco"],
                    dessert=row["Sobremesa"],
                    coffee=row["Café"],
                    bread=row["Pão"]
                )
                session.add(menu_entry)
            session.commit()
        print("Dados inseridos com sucesso!")

    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
