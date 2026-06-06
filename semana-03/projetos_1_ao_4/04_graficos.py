
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. DADOS ORIGINAIS DO MONITORAMENTO DO HOSPITAL
dados = {
    'data': ['2026-06-01', '2026-06-02', '2026-06-02', '2026-06-03', '2026-06-04', '2026-06-04', '2026-06-05', '2026-06-05'],
    'setor': ['TI', 'Financeiro', 'TI', 'Pronto Socorro', 'TI', 'RH', 'Financeiro', 'TI'],
    'tipo': ['DDoS', 'Login Falho', 'SQLi', 'Acesso OK', 'DDoS', 'Login Falho', 'Login Falho', 'DDoS'],
    'pais_origem': ['Brasil', 'EUA', 'China', 'Brasil', 'EUA', 'Brasil', 'China', 'Brasil'],
    'ip_origem': ['192.168.1.50', '10.0.0.15', '10.0.0.30', '192.168.2.100', '172.16.0.5', '192.168.1.60', '10.0.0.16', '192.168.1.50'],
    'duracao': [1200, 30, 450, 0, 3600, 45, 20, 1800]
}
df = pd.DataFrame(dados)
df["data"] = pd.to_datetime(df["data"])

print("=== PROJETO 4: GRÁFICOS COM SEABORN (TEMA DARK) ===")

# Aplicando a Dica Pro do material: Tema Dark do Seaborn
sns.set_theme(style="darkgrid")
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 1. Gráfico de Barras: Top Países - DDoS
ddos = df[df["tipo"] == "DDoS"]
top10 = ddos["pais_origem"].value_counts().head(10)
top10.plot(kind="bar", color="#16C79A", ax=axes[0])
axes[0].set_title("Top Paises - DDoS")
axes[0].set_xlabel("Pais")
axes[0].set_ylabel("Ataques")

# 2. Gráfico de Linha: Ataques por Dia/Mês
df.set_index('data').resample('D').size().plot(kind="line", marker='o', color="#FF6B6B", ax=axes[1])
axes[1].set_title("Ataques por Dia")

# 3. Gráfico de Pizza: Tipos de Ataque (Usando paleta limpa do Matplotlib para evitar avisos)
df["tipo"].value_counts().plot(kind="pie", autopct='%1.1f%%', colors=plt.cm.Pastel1.colors, ax=axes[2])
axes[2].set_title("Tipos de Ataque")
axes[2].set_ylabel("")

plt.tight_layout()

# AUTOMAÇÃO: Garante que a pasta física exista antes de salvar para evitar o FileNotFoundError
pasta_destino = "semana-03/projetos_1_ao_4/graficos"
os.makedirs(pasta_destino, exist_ok=True)

# Salvando a imagem com segurança
caminho_final = os.path.join(pasta_destino, "resultado_analise.png")
plt.savefig(caminho_final)
print(f"[SUCESSO] Gráficos salvos em: {caminho_final}")

# Exibe os gráficos na tela
plt.show()