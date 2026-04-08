import random
import string

print("--- GERADOR DE SENHAS SEGURAS ---")

# 1. Pergunta o tamanho da senha
tamanho = int(input("Digite a quantidade de caracteres para a senha: "))

# 2. Define o que pode ter na senha (letras, números e símbolos)
caracteres = string.ascii_letters + string.digits + string.punctuation

# 3. Sorteia os caracteres aleatoriamente e junta tudo
senha = "".join(random.choice(caracteres) for i in range(tamanho))

print("\n" + "="*30)
print(f"SENHA GERADA: {senha}")
print("="*30)