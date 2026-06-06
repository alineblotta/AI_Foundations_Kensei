from openai import OpenAI
from dotenv import load_dotenv

# Inicializa as credenciais do ambiente
load_dotenv()
client = OpenAI()

print("=== PROJETO 5: GERADOR DE RELATÓRIOS ===")

# Dados simulados de incidentes/vulnerabilidades para o relatório
dados_seguranca = """
- Total de varreduras de portas bloqueadas: 1.420
- Tentativas de SQL Injection barradas pelo WAF: 342
- Alertas de Brute Force em APIs mitigados: 89
- Tempo médio de reação automatizada (SOAR): 22 segundos
- Status geral do ambiente: Estável / Sob Monitoramento
"""

# Prompt que instrui a IA a criar um Sumário Executivo corporativo
prompt_sistema = """Você é um Analista de Cyber Defense Sênior. 
Transforme as métricas brutas fornecidas pelo usuário em um Relatório Executivo de Segurança Cibernética profissional.
Use uma estrutura limpa com introdução, destaques técnicos, análise de risco e conclusão."""

# Chamada da API
resposta = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": prompt_sistema},
        {"role": "user", "content": dados_seguranca}
    ]
)

print("\n📊 Relatório Gerado com Sucesso:")
print("=" * 60)
print(resposta.choices[0].message.content)
print("=" * 60)