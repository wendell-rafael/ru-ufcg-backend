import os
import sys
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Configurar as credenciais da conta de serviço
SCOPES = ['https://www.googleapis.com/auth/drive']
CREDENTIALS_PATH = os.getenv("GOOGLE_CREDENTIALS_PATH")

# Carregar credenciais
credentials = Credentials.from_service_account_file(CREDENTIALS_PATH, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)


def get_file_id_by_name(file_name: str):
    """
    Busca o ID de um arquivo no Google Drive pelo nome.
    """
    results = service.files().list(
        q=f"name='{file_name}'",
        spaces='drive',
        fields="files(id, name)"
    ).execute()
    files = results.get('files', [])
    if not files:
        raise Exception(f"Arquivo '{file_name}' não encontrado no Google Drive.")
    return files[0]['id']


def download_file(file_id: str, destination: str):
    """
    Faz o download de um arquivo do Google Drive usando o ID.
    """
    request = service.files().get_media(fileId=file_id)
    with open(destination, 'wb') as file:
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
            print(f"Progresso do download: {int(status.progress() * 100)}%")
    print(f"Arquivo baixado com sucesso: {destination}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python download_menu.py <nome_do_arquivo>")
        sys.exit(1)

    FILE_NAME = sys.argv[1]  # Nome do arquivo recebido como argumento
    DESTINATION = os.path.join("app", "scripts", FILE_NAME)
    try:
        # Buscar o ID do arquivo pelo nome
        file_id = get_file_id_by_name(FILE_NAME)
        print(f"ID do arquivo '{FILE_NAME}': {file_id}")

        # Fazer o download do arquivo
        download_file(file_id, DESTINATION)

    except Exception as e:
        print(f"Erro: {e}")
