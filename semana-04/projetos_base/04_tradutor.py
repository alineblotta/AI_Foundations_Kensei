from openai import OpenAI
from dotenv import load_dotenv

# Inicializa as credenciais do ambiente
load_dotenv()
client = OpenAI()

print("=== PROJETO 4: TRADUTOR INTELIGENTE ===")

def traduzir(texto, dest="pt-BR"):
    # Prompt estruturado para detecção e tradução conforme a ementa
    prompt = f"""Detecte o idioma original e traduza para {dest} o seguinte texto:
    
    {texto}
    
    Retorne estritamente neste formato:
    Idioma Detectado: [Nome do Idioma]
    Tradução: [Texto Traduzido]"""
    
    resp = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.choices[0].message.content

# Ajustado para ler 'artigo_en.txt', mantendo o padrão fiel à lógica da apostila
with open("artigo_en.txt", "r", encoding="utf-8") as f:
    conteudo_para_traduzir = f.read()
    
    print("\n[PROCESSANDO...] Detectando idioma e traduzindo o arquivo 'artigo_en.txt'...\n")
    print(traduzir(conteudo_para_traduzir))