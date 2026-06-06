# 1. Importamos as ferramentas que instalamos
from openai import OpenAI
from dotenv import load_dotenv

# 2. Comando do cofre: Lê o arquivo .env e carrega sua chave na memória do computador
load_dotenv()

# 3. Inicializa o "garçom" da API, que já pega a chave automaticamente do .env
client = OpenAI()

print("=== PROJETO 1: PRIMEIRA CONVERSA COM A API ===")

# 4. DESAFIO DO MATERIAL: Faz o analista digitar a pergunta no terminal
pergunta_usuario = input("\nDigite sua pergunta para a IA: ")

# Se você só apertar Enter sem digitar nada, o script usa a pergunta padrão da apostila
if pergunta_usuario.strip() == "":
    pergunta_usuario = "O que e phishing em 2 frases?"

print("\n[PROCESSANDO...] O garçom está levando seu pedido ao servidor...")

# 5. Enviamos a pergunta para a estrutura do chat da IA
resposta_completa = client.chat.completions.create(
    model="llama-3.3-70b-versatile",  # <-- MODELO ATUALIZADO AQUI
    messages=[
        {
            "role": "user",  # Indica que essa é a mensagem enviada por você (usuário)
            "content": pergunta_usuario
        }
    ]
)

print("\n🤖 Resposta da IA:")
# 6. O servidor devolve muita informação técnica, mas nós filtramos para mostrar só o texto da resposta
print(resposta_completa.choices[0].message.content)