import json
from openai import OpenAI
from dotenv import load_dotenv

# Inicializa a API
load_dotenv()
client = OpenAI()

# Função principal:
def analisar(texto):
    prompt = f"""Analise: {texto}
    Retorne JSON: resumo (3 frases), sentimento, palavras_chave"""
    
    resp = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )
    return resp.choices[0].message.content

print("=== PROJETO 3: ANALISADOR DE TEXTO ===")

# Leitura direta do arquivo .txt
with open("artigo.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()

# Executa a função e recebe a string JSON
resultado_json = analisar(conteudo)

# Converte e salva diretamente no arquivo analise.json
dados = json.loads(resultado_json)
with open("analise.json", "w", encoding="utf-8") as arquivo_json:
    json.dump(dados, arquivo_json, indent=4, ensure_ascii=False)

print("\n✅ Script executado! Arquivo 'analise.json' gerado.")