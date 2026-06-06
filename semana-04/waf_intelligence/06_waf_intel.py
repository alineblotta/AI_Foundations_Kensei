import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

# Conecta com as suas chaves do ambiente
load_dotenv()
client = OpenAI()

print("🛡️ === FERRAMENTA PRÓPRIA: WAF THREAT INTELLIGENCE REPORTER ===")

# O Pandas lê o arquivo que o simulador acabou de preencher
try:
    df = pd.read_csv("logs_waf.csv")
    
    # Resumo estatístico dos logs para a IA
    total_ataques = len(df)
    ataques_por_tipo = df['tipo_ataque'].value_counts().to_string()
    principais_ofensores = df['ip_origem'].value_counts().head(3).to_string()
    payloads_criticos = df[df['criticidade'].isin(['Alta', 'Critica'])][['tipo_ataque', 'payload']].to_string(index=False)

except FileNotFoundError:
    print("Erro: O arquivo 'logs_waf.csv' não foi encontrado!")
    exit()

# Instrução para a inteligência da IA
prompt_sistema = """Você é um Engenheiro de Detecção e Threat Intelligence Sênior especialista em WAF.
Analise o resumo de blocos fornecido pelo usuário e gere um Boletim de Inteligência de Ameaças técnico para o Blue Team."""

dados_para_ia = f"""
[MÉTRICAS DO WAF]
Total de Bloqueios Recentes: {total_ataques}

Volume por Tipo de Ataque:
{ataques_por_tipo}

Principais IPs Ofensores:
{principais_ofensores}

Payloads Críticos Identificados:
{payloads_criticos}
"""

print("\n[ANALISANDO LOGS VIVOS...] Cruzando dados com a IA...\n")

# Chamada do modelo Llama
resposta = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": prompt_sistema},
        {"role": "user", "content": dados_para_ia}
    ]
)

print("📊 BOLETIM DE THREAT INTELLIGENCE GERADO:")
print("=" * 70)
print(resposta.choices[0].message.content)
print("=" * 70)