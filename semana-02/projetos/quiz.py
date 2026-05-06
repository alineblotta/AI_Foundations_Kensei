
# --- QUIZ DE CIBERSEGURANÇA PROFISSIONAL ---
print("="*30)
print("SISTEMA DE AVALIAÇÃO KENSEI")
print(f"Analista: Aline Blotta")
print("="*30)
print("Instruções: Escolha a letra correta (A, B, C ou D).\n")

acertos = 0

# Pergunta 1
print("1. O que é phishing?")
print("A) Um método de criptografia de ponta a ponta.")
print("B) Técnica de fraude para enganar usuários e obter dados confidenciais.")
print("C) Um protocolo de transferência de arquivos pesados.")
print("D) Uma ferramenta de varredura de vulnerabilidades em bancos de dados.")
resp1 = input("Sua resposta: ").upper()
if resp1 == "B":
    print("✅ Correto!")
    acertos += 1
else:
    print("❌ Errado. A resposta correta era B.")
print("🔍 EXPLICAÇÃO: Criptografia (A) e Varredura (D) são processos técnicos de proteção/auditoria. O Phishing foca no engano humano.")

# Pergunta 2
print("\n2. O que significa autenticação de dois fatores (2FA)?")
print("A) É um método que exige duas formas de verificação para acessar uma conta.")
print("B) É a necessidade de dois administradores para aprovar uma senha.")
print("C) Um sistema que duplica os dados para evitar perda de arquivos.")
print("D) Uma técnica de invasão que usa dois servidores ao mesmo tempo.")
resp2 = input("Sua resposta: ").upper()
if resp2 == "A":
    print("✅ Correto!")
    acertos += 1
else:
    print("❌ Errado. A resposta correta era A.")
print("🔍 EXPLICAÇÃO: A opção B descreve aprovação múltipla, e a C descreve redundância/backup. 2FA é sobre camadas de identidade.")

# Pergunta 3
print("\n3. O que é um malware?")
print("A) Um componente físico do computador, como a memória RAM.")
print("B) Um programa de otimização de sistemas operacionais.")
print("C) Software malicioso criado para danificar ou roubar informações.")
print("D) Um tipo de firewall focado em aplicações web.")
resp3 = input("Sua resposta: ").upper()
if resp3 == "C":
    print("✅ Correto!")
    acertos += 1
else:
    print("❌ Errado. A resposta correta era C.")
print("🔍 EXPLICAÇÃO: RAM (A) é Hardware. Firewall (D) é defesa. Malware é o termo genérico para qualquer software nocivo.")

# Pergunta 4
print("\n4. Por que é importante manter softwares atualizados?")
print("A) Para garantir que o software nunca expire.")
print("B) Para corrigir vulnerabilidades de segurança e proteger o sistema.")
print("C) Para aumentar a velocidade da internet local.")
print("D) Apenas para remover arquivos antigos do usuário.")
resp4 = input("Sua resposta: ").upper()
if resp4 == "B":
    print("✅ Correto!")
    acertos += 1
else:
    print("❌ Errado. A resposta correta era B.")
print("🔍 EXPLICAÇÃO: Atualizações trazem 'patches' de segurança. Elas não removem arquivos do usuário (D) nem afetam o plano de internet (C).")

# Pergunta 5
print("\n5. O que é um firewall?")
print("A) Um sistema que monitora e controla o tráfego de rede.")
print("B) Um vírus que se espalha por redes Wi-Fi.")
print("C) Uma técnica de backup em nuvem.")
print("D) Um algoritmo de compressão de dados.")
resp5 = input("Sua resposta: ").upper()
if resp5 == "A":
    print("✅ Correto!")
    acertos += 1
else:
    print("❌ Errado. A resposta correta era A.")
print("🔍 EXPLICAÇÃO: Firewall é o 'porteiro' da rede. Vírus (B) é ameaça e Backup (C) é recuperação. Ele atua no controle de tráfego.")

# RESULTADO FINAL
print("\n" + "="*40)
print(f"RELATÓRIO FINAL: {acertos} de 5 acertos.")
if acertos == 5:
    print("Desempenho: Excelente! Pronta para o Incident Response.")
elif acertos >= 3:
    print("Desempenho: Bom, mas revise os conceitos básicos.")
else:
    print("Desempenho: Alerta! Estude mais os fundamentos de segurança.")
print("="*40)