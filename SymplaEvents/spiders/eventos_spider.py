import requests
from bs4 import BeautifulSoup
import json
import time
import logging
import os

# Configurações de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Definindo a URL base e as cidades
url_base = "https://www.sympla.com.br/"
cidades = ['cariacica-es', 'fundao-es', 'guarapari-es', 'serra-es', 'viana-es', 'vila-velha-es', 'vitoria-es']

# Dicionário para armazenar os eventos
eventos = []

# Função para buscar eventos em uma cidade específica
def buscar_eventos(cidade):
    url = f"{url_base}eventos/{cidade}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro para códigos de status 4xx ou 5xx
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontrar todos os cartões de evento
        cards = soup.find_all('a', class_='EventCardstyle__CardLink-sc-1rkzctc-3')

        for card in cards:
            # Extrair os dados necessários
            nome = card.get('data-name', 'Nome não disponível')
            local_evento = card.get('aria-label', '').split(", em ")[-1]  # pega o local do aria-label
            
            # Coletando data e hora
            data_hora_div = card.find('div', class_='EventCardstyle__EventDate-sc-1rkzctc-6')
            data_hora = data_hora_div.find('div', class_='sc-1sp59be-1 fZlvlB').text.strip() if data_hora_div else 'Data não disponível'
            
            # Pegar o link do evento
            link = card.get('href', 'Link não disponível')

            # Adiciona ao dicionário
            eventos.append({
                "Nome": nome,
                "Local do Evento": local_evento,
                "Data e Hora": data_hora,
                "Link": link
            })

    except requests.RequestException as e:
        logging.error(f"Erro ao acessar a página {url}: {e}")

# Executa a busca para cada cidade
for cidade in cidades:
    print(f"Coletando dados {cidade.replace('-es', '').title()}")  # Exibe a cidade formatada
    buscar_eventos(cidade)
    time.sleep(2)  # Espera 2 segundos entre as requisições

# Salvando os eventos em um arquivo JSON dentro da pasta data
with open('data/eventos.json', 'w', encoding='utf-8') as f:
    json.dump(eventos, f, ensure_ascii=False, indent=4)

logging.info("Eventos coletados com sucesso!")
