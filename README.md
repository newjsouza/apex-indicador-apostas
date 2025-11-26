# Indicador de Apostas - Apex

Um projeto simples para recomendar apostas reais a partir de jogos coletados de APIs esportivas, usando sugestões via Perplexity API como orientação de IA.  

## Funcionalidade Principal
- Coleta de jogos reais (exemplo: futebol) através de uma API pública gratuita
- Utilização da API da Perplexity para analisar jogos e sugerir probabilidades e apostas
- Exemplo prático usando Python

## Como funciona
1. Busca jogos do dia em uma API pública (ex: The Sports DB, Football-Data.org)
2. Envia descrição dos jogos para a API da Perplexity para sugestões de apostas
3. Retorna as recomendações ao usuário

## Requisitos
- Python 3+
- Requests (`pip install requests`)

## Observação
Este projeto é apenas para aprendizado e demonstração. Aposte com responsabilidade!

## Próximos passos
- [ ] Adicionar exemplo prático em Python
- [ ] Documentar integração com Perplexity API
- [ ] Automatizar atualização de jogos diariamente