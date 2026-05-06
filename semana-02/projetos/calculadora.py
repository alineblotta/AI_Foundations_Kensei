import time

print("--- 🛡️ ANALISADOR DE IMPACTO DE SEGURANÇA (CIA) ---")

# 1. Avaliação dos Pilares (Escala de 1 a 5 para facilitar)
print("\nAvalie o impacto nos pilares (1-Baixo a 5-Crítico):")
c = int(input("Confidencialidade (Vazamento de dados): "))
i = int(input("Integridade (Alteração de informações): "))
a = int(input("Disponibilidade (Sistema fora do ar): "))

# 2. Cálculo da Severidade (Média Ponderada)
# No mercado, se um pilar é 5, o risco já tende a ser crítico.
score_cia = (c + i + a) / 3

print("\n--- Processando Matriz de Risco... ---")
time.sleep(1)

# 3. Classificação Profissional
print(f"Score Médio de Impacto: {score_cia:.1f}")

if score_cia >= 4.5 or (c == 5 or i == 5 or a == 5):
    print("CLASSIFICAÇÃO: 🔴 CRÍTICA (Ação Imediata)")
elif 3 <= score_cia < 4.5:
    print("CLASSIFICAÇÃO: 🟠 ALTA (Correção Prioritária)")
elif 1.5 <= score_cia < 3:
    print("CLASSIFICAÇÃO: 🟡 MÉDIA (Planejar Mitigação)")
else:
    print("CLASSIFICAÇÃO: 🟢 BAIXA (Apenas Monitorar)")

print("-" * 50)