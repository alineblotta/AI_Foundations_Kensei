import csv
import random
import time
from datetime import datetime

# Dados fictícios baseados em ataques web reais (OWASP Top 10)
ips_suspeitos = ["185.220.101.5", "45.132.22.41", "198.51.100.45", "91.240.118.12", "172.56.21.9"]
ataques = [
    ("SQL Injection", "1' OR '1'='1", "Alta"),
    ("SQL Injection", "UNION SELECT null, username, password FROM users", "Critica"),
    ("Cross-Site Scripting (XSS)", "<script>alert(1)</script>", "Media"),
    ("Cross-Site Scripting (XSS)", "<img src=x onerror=bf()>", "Media"),
    ("Path Traversal", "../../../../etc/passwd", "Critica"),
    ("Command Injection", "; rm -rf /", "Critica"),
    ("Brute Force", "Tentativa de login invalida com usuario 'admin'", "Baixa")
]

print("🚀 [WAF SIMULATOR] Iniciando geracao de telemetria de seguranca...")

# Cria o arquivo do zero e escreve os cabeçalhos das colunas
with open("logs_waf.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "ip_origem", "tipo_ataque", "payload", "criticidade"])

# Loop contínuo que adiciona um ataque novo a cada poucos segundos
while True:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = random.choice(ips_suspeitos)
    tipo, payload, criticidade = random.choice(ataques)
    
    # Abre o arquivo em modo 'a' (append) para apenas adicionar a linha no final
    with open("logs_waf.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, ip, tipo, payload, criticidade])
        
    print(f"🛡️ [{timestamp}] WAF Bloqueou: {tipo} vindo de {ip}")
    
    # Sorteia um tempo de espera aleatório entre 2 e 5 segundos para o próximo ataque
    time.sleep(random.randint(2, 5))