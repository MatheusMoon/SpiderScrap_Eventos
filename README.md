# WebScraping_Eventos

Este projeto é um scraper em Python que coleta informações sobre eventos de diversas cidades do Brasil a partir do site [Sympla](https://www.sympla.com.br/). O scraper extrai dados como nome do evento, local, data, hora e link do evento, e armazena essas informações em um arquivo JSON.

## Funcionalidades

- Coleta dados de eventos em várias cidades: Cariacica, Fundão, Guarapari, Serra, Viana, Vila Velha e Vitória.
- Registra logs de erros e informações sobre o processo de coleta.
- Salva os dados coletados em um arquivo JSON estruturado.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para desenvolver o scraper.
- **Requests**: Biblioteca para fazer requisições HTTP.
- **BeautifulSoup**: Biblioteca para analisar e extrair dados de arquivos HTML e XML.
- **JSON**: Formato para armazenar os dados coletados.
- **Logging**: Módulo para registrar logs do processo.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter o Python e as bibliotecas necessárias instaladas. Você pode instalar as bibliotecas usando o arquivo `requirements.txt`.

```bash
pip install -r requirements.txt