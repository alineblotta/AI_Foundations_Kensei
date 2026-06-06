import pandas as pd
import matplotlib.pyplot as plt

# Criando o DataFrame com os dados do monitoramento
dados = {
    'data': ['2026-06-01', '2026-06-02', '2026-06-02', '2026-06-03', '2026-06-04', '2026-06-04', '2026-06-05', '2026-06-05'],
    'setor': ['TI', 'Financeiro', 'TI', 'Pronto Socorro', 'TI', 'RH', 'Financeiro', 'TI'],
    'tipo': ['DDoS', 'Login Falho', 'SQLi', 'Acesso OK', 'DDoS', 'Login Falho', 'Login Falho', 'DDoS'],
    'pais_origem': ['Brasil', 'EUA', 'China', 'Brasil', 'EUA', 'Brasil', 'China', 'Brasil'],
    'ip_origem': ['192.168.1.50', '10.0.0.15', None, '192.168.2.100', '172.16.0.5', '192.168.1.60', '10.0.0.16', '192.168.1.50'],
    'duracao': [1200, 30, 450, 0, 3600, 45, 20, 1800]
}
df = pd.DataFrame(dados)

print("=== PROJETO 1: CARREGANDO E EXPLORANDO DADOS ===")
print(df.head())          # 5 primeiras linhas
print(df.shape)         # (linhas, cols)
print(df.info())          # tipos de dados
print(df.describe())      # estatísticas
print(df.columns)       # nomes das colunas
print(df.isnull().sum())  # contagem de nulos