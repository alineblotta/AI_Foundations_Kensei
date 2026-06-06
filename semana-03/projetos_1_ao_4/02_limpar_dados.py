import pandas as pd

dados = {
    'data': ['2026-06-01', '2026-06-02', '2026-06-02', '2026-06-03', '2026-06-04', '2026-06-04', '2026-06-05', '2026-06-05'],
    'setor': ['TI', 'Financeiro', 'TI', 'Pronto Socorro', 'TI', 'RH', 'Financeiro', 'TI'],
    'tipo': ['DDoS', 'Login Falho', 'SQLi', 'Acesso OK', 'DDoS', 'Login Falho', 'Login Falho', 'DDoS'],
    'pais_origem': ['Brasil', 'EUA', 'China', 'Brasil', 'EUA', 'Brasil', 'China', 'Brasil'],
    'ip_origem': ['192.168.1.50', '10.0.0.15', None, '192.168.2.100', '172.16.0.5', '192.168.1.60', '10.0.0.16', '192.168.1.50'],
    'duracao': [1200, 30, 450, 0, 3600, 45, 20, 1800]
}
df = pd.DataFrame(dados)

print("=== PROJETO 2: LIMPENDO DADOS SUJOS ===")
# Verificar
print(df.isnull().sum())
print(df.duplicated().sum())

# Limpar
df = df.drop_duplicates()
df["tipo"].fillna("desconhecido", inplace=True)
df["data"] = pd.to_datetime(df["data"])
df = df.dropna(subset=["ip_origem"])

print("\n--- Dataset Após a Limpeza ---")
print(df)