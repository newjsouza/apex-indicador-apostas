import requests
import json

# Exemplo: API pública de jogos de futebol
FOOTBALL_API_URL = 'https://www.thesportsdb.com/api/v1/json/1/eventsday.php?d=2025-11-26&s=Soccer'
PERPLEXITY_API_KEY = 'SUA_API_KEY_AQUI'  # Troque pela sua chave ou armazene em variável de ambiente
PERPLEXITY_API_URL = 'https://api.perplexity.ai/v1/answer'

# 1. Coleta jogos reais do dia
def coletar_jogos():
    resp = requests.get(FOOTBALL_API_URL)
    if resp.status_code != 200:
        raise Exception('Erro ao buscar jogos.')
    dados = resp.json()
    return [e['strEvent'] for e in dados.get('events', [])[:5]]  # Apenas primeiros 5 exemplos

# 2. Gera sugestão de apostas via API Perplexity
def gerar_indicacoes(jogos):
    prompt = 'Sugira as melhores apostas esportivas (simples, com base em análise de probabilidades) para os seguintes jogos de futebol:\n'
    prompt += '\n'.join(jogos)
    headers = { 'Authorization': f'Bearer {PERPLEXITY_API_KEY}', 'Content-Type': 'application/json' }
    body = {
        "model": "pplx-70b-online",
        "messages": [
            { "role": "user", "content": prompt }
        ]
    }
    r = requests.post(PERPLEXITY_API_URL, headers=headers, data=json.dumps(body))
    return r.json()

if __name__ == "__main__":
    jogos = coletar_jogos()
    print("Jogos coletados:", jogos)
    resposta = gerar_indicacoes(jogos)
    print("Sugestões da IA:", resposta)
