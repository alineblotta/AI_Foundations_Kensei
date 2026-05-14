import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. CRIANDO OS DADOS (Simulando incidentes de segurança no Hospital)
dados = {
    'setor': ['TI', 'Financeiro', 'TI', 'Pronto Socorro', 'TI', 'RH', 'Financeiro', 'TI'],
    'tipo': ['DDoS', 'Login Falho', 'SQLi', 'Acesso OK', 'DDoS', 'Login Falho', 'Login Falho', 'DDoS'],
    'severidade': [5, 2, 5, 1, 5, 2, 2, 4]
}

df = pd.DataFrame(dados)

# 2. ANÁLISE NO TERMINAL
print("--- Resumo de Ocorrências por Setor ---")
print(df['setor'].value_counts())

# 3. CRIAÇÃO DO GRÁFICO
plt.figure(figsize=(10, 6))
sns.set_theme(style="darkgrid")

# Criando um gráfico de contagem de ataques por tipo
sns.countplot(data=df, x='tipo', palette='viridis')

plt.title('Monitoramento de Incidentes - Semana 03')
plt.xlabel('Tipo de Ataque')
plt.ylabel('Quantidade')

# 4. SALVANDO E EXIBINDO
plt.savefig('semana-03/graficos/resultado_analise.png')
print("\n[SUCESSO] Gráfico salvo em: semana-03/graficos/resultado_analise.png")

plt.show()