from openai import OpenAI
from dotenv import load_dotenv

# 1. Inicializa o cofre de chaves
load_dotenv()
client = OpenAI()

# CONFIGURAÇÃO DE CORES (Códigos ANSI para o terminal)
VERDE = "\033[92m"
BRANCO = "\033[97m"
RESET = "\033[0m"

print("=== PROJETO 2: ASSISTENTE DE SEGURANÇA OPERACIONAL ===")
print("Digite 'sair' a qualquer momento para encerrar o chat.\n")

# CONCEITO: role system -> Define a personalidade e as diretrizes de comportamento da IA
historico = [
    {
        "role": "system", 
        "content": """Você é um especialista em Segurança da Informação, com foco em Defesa Cibernética (Blue Team), Resposta a Incidentes e Proteção de Dados. Seu tom deve ser profissional, direto, analítico e focado em engenharia de segurança. 

Diretrizes:
1. Forneça respostas técnicas, mas práticas, priorizando os principais frameworks de mercado (como MITRE ATT&CK, NIST, CIS Controls).
2. Sempre que sugerir uma correção, explique brevemente o risco associado (impacto de segurança).
3. Evite respostas genéricas. Seja consultiva e sugira comandos, configurações ou lógicas de código aplicáveis quando relevante."""
    }
]

# CONCEITO: while True -> Loop contínuo para manter o chat aberto
while True:
    # DESAFIO: Usuário digita em Branco
    msg_usuario = input(f"{BRANCO}Você: {RESET}")
    
    # Condição de parada do loop
    if msg_usuario.strip().lower() == "sair":
        print("\nEncerrando sessão do assistente. Até logo!")
        break
        
    if msg_usuario.strip() == "":
        continue
        
    # CONCEITO: .append() -> Adiciona a fala do usuário na memória para a IA saber o contexto
    historico.append({"role": "user", "content": msg_usuario})
    
    print(f"\n[PROCESSANDO...] O assistente está analisando...")
    
    try:
        # Envia todo o histórico (contexto acumulado) para a API
        resp = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=historico
        )
        
        resposta_ia = resp.choices[0].message.content
        
        # DESAFIO: Exibir a resposta da IA na cor Verde
        print(f"\n{VERDE}IA: {resposta_ia}{RESET}\n")
        
        # CONCEITO: Adiciona a resposta da própria IA no histórico para ela lembrar do que ela mesma disse
        historico.append({"role": "assistant", "content": resposta_ia})
        
    except Exception as e:
        print(f"\n[ERRO] Falha na comunicação: {e}\n")