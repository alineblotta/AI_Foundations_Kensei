import pandas as pd

dados = {
    'data': ['2026-06-01', '2026-06-02', '2026-06-02', '2026-06-03', '2026-06-04', '2026-06-04', '2026-06-05', '2026-06-05'],
    'setor': ['TI', 'Financeiro', 'TI', 'Pronto Socorro', 'TI', 'RH', 'Financeiro', 'TI'],
    'tipo': ['DDoS', 'Login Falho', 'SQLi', 'Acesso OK', 'DDoS', 'Login Falho', 'Login Falho', 'DDoS'],
    'pais_origem': ['Brasil', 'EUA', 'China', 'Brasil', 'EUA', 'Brasil', 'China', 'Brasil'],
    'ip_origem': ['192.168.1.50', '10.0.0.15', '10.0.0.22', '192.168.2.100', '172.16.0.5', '192.168.1.60', '10.0.0.16', '192.168.1.50'],
    'duracao': [1200, 30, 450, 0, 3600, 45, 20, 1800]
}
df = pd.DataFrame(dados)

print("=== PROJETO 3: FILTRANDO E AGRUPANDO ===")
ddos = df[df["tipo"] == "DDoS"]
recentes = ddos[ddos["data"] > "2024-01-01"]
por_pais = recentes.groupby("pais_origem")
contagem = por_pais.size()
top10 = contagem.sort_values(ascending=False).head(10)
print("--- Top Países DDoS ---")
print(top10)

# Pergunta bônus: média de duração
print("\n--- Média de Duração dos Ataques por País ---")
print(recentes.groupby("pais_origem")["duracao"].mean())