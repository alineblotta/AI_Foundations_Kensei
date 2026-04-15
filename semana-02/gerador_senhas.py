import random
import string

# Configuração de segurança
PIN_MESTRE = "2026" # O "Token" que libera a visualização

print("--- 🛡️ KENSEI CYBERSEC: GERADOR SEGURO ---")

# 1. Pergunta o tamanho da senha
tamanho = int(input("Digite a quantidade de caracteres para a senha: "))

# 2. Define o que pode ter na senha (letras, números e símbolos/pontuação)
# Aqui mantemos os caracteres especiais conforme sua solicitação inicial
caracteres = string.ascii_letters + string.digits + string.punctuation

# 3. Sorteia os caracteres aleatoriamente e junta tudo
senha = "".join(random.choice(caracteres) for i in range(tamanho))

print("\n" + "="*35)
print("🔒 STATUS: SENHA GERADA E CRIPTOGRAFADA")
print("="*35)

# MELHORIA DE CYBER: Reautenticação antes de revelar
token = input("Digite seu PIN de 4 dígitos para revelar a senha: ")

if token == PIN_MESTRE:
    print("\n" + "="*30)
    print(f"SENHA REVELADA: {senha}")
    print("="*30)
    print("\n[!] DICA: Use 'cls' para limpar o terminal e proteger sua senha.")
else:
    print("\n❌ ACESSO NEGADO! O PIN está incorreto.")
    print("Por segurança, a senha não será exibida.")