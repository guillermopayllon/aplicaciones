import requests
from bs4 import BeautifulSoup

def buscar_stackoverflow(error_text):
    query = error_text.replace(" ", "+")
    url = f"https://stackoverflow.com/search?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    enlaces = soup.select('.question-summary .result-link a')
    resultados = [f"https://stackoverflow.com{link['href']}" for link in enlaces[:5]]
    return resultados
