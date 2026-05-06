# --- LAB DE CONDICIONAIS ---

# Pedindo uma nota para o usuário (convertendo para número decimal)
nota = float(input("Digite a nota do laboratório (0 a 10): "))

# Tomando a decisão com base na nota
if nota >= 7:
    print("Aprovado! Precisão de Samurai.")
    print("Status: Acesso concedido ao próximo nível.")
elif nota >= 5:
    print("Recuperação. Hora de revisar os logs e praticar mais.")
else:
    print("Reprovado. Precisa refazer o treinamento de base.")