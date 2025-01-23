import requests

API_KEY = '68d5abdef9aad4d2f29aa68b'


def converter_moeda(valor, moeda_origem, moeda_destino):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{moeda_origem}"
    response = requests.get(url)
    dados = response.json()
    if dados["result"] == "success":
        taxa_conversao = dados["conversion_rates"].get(moeda_destino)
        return valor * taxa_conversao
    else:
        return "Erro"


def listar_moedas():
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
    response = requests.get(url)
    dados = response.json()
    if dados["result"] == "success":
        return list(dados["conversion_rates"].keys())
    else:
        return "Erro"
