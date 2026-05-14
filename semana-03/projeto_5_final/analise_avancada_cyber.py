import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. CARREGAR (Passo 2 do material)
# AJUSTADO: Agora aponta para projeto_5_final
df = pd.read_csv('semana-03/projeto_5_final/cyber_attacks_simulated.csv')

# 2. EXPLORAR E LIMPAR (Passo 3 do material)
print("--- Primeiras 5 linhas do Dataset ---")
print(df.head())
print("\n--- Informações Gerais ---")
df.info()

# 3. ANALISAR (Passo 4 do material)
media_pais = df.groupby('Country')['Severity_Score'].mean()
print("\n--- Severidade Média por País ---")
print(media_pais)

# 4. VISUALIZAR (Passo 5 do material - 3 Gráficos)
sns.set_theme(style="whitegrid")
plt.figure(figsize=(15, 5))

# Gráfico 1: Volume de Ataques por Tipo
plt.subplot(1, 3, 1)
sns.countplot(data=df, x='Attack_Type', palette='viridis', hue='Attack_Type', legend=False)
plt.title('Volume por Tipo')

# Gráfico 2: Severidade por País
plt.subplot(1, 3, 2)
sns.barplot(data=df, x='Country', y='Severity_Score', palette='magma', hue='Country', legend=False)
plt.title('Severidade Média')

# Gráfico 3: Distribuição de Pontuação
plt.subplot(1, 3, 3)
sns.histplot(df['Severity_Score'], kde=True, color='teal')
plt.title('Distribuição de Severidade')

# SALVANDO O RESULTADO
# AJUSTADO: Salvando na nova estrutura de pastas
plt.tight_layout()
plt.savefig('semana-03/projeto_5_final/graficos/dashboard_cyber.png')
print("\n[SUCESSO] Gráfico salvo em: semana-03/projeto_5_final/graficos/dashboard_cyber.png")

plt.show()