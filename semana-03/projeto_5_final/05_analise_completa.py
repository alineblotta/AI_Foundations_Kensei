import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. CARREGAR 
df = pd.read_csv('cyber_attacks_simulated.csv')

# 2. EXPLORAR E LIMPAR
print("=== PROJETO 5: ANALISE COMPLETA E INTEGRADA ===")
print("\n--- Primeiras 5 linhas do Dataset ---")
print(df.head())
print("\n--- Informações Gerais ---")
df.info()

# 3. ANALISAR
media_pais = df.groupby('Country')['Severity_Score'].mean()
print("\n--- Severidade Média por País ---")
print(media_pais)

# 4. VISUALIZAR (3 Gráficos com Tema Clean)
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

# Gráfico 3: Distribuição de Pontuação de Severidade
plt.subplot(1, 3, 3)
sns.histplot(df['Severity_Score'], kde=True, color='teal')
plt.title('Distribuição de Severidade')

plt.tight_layout()

# AUTOMAÇÃO DE INFRAESTRUTURA: Pasta 'graficos' local
pasta_destino = 'graficos'
os.makedirs(pasta_destino, exist_ok=True)

# SALVANDO O RESULTADO
caminho_salvamento = os.path.join(pasta_destino, 'dashboard_cyber.png')
plt.savefig(caminho_salvamento)
print(f"\n[SUCESSO] Dashboard avançado gerado e salvo em: {caminho_salvamento}")

# EXIBE O DASHBOARD NA TELA
plt.show()