# PROJETO EXTRA: Kensei CyberSec Lab - Pathfinder 2026

carreiras = {
    "1": {"nome": "Defesa (Blue Team)", "foco": "Monitorar e defender infraestrutura.", "skills": ["SIEM", "Logs", "Firewalls"], "certs": ["Security+", "BTL1"]},
    "2": {"nome": "Ofensivo (Red Team)", "foco": "Simular ataques e achar falhas.", "skills": ["Nmap", "Metasploit", "Web"], "certs": ["eJPT", "OSCP"]},
    "3": {"nome": "Governança (GRC)", "foco": "Leis (LGPD) e gestão de riscos.", "skills": ["ISO 27001", "LGPD", "Auditoria"], "certs": ["ISC2 CC", "CISM"]},
    "4": {"nome": "Cloud Security", "foco": "Proteger AWS, Azure e Google Cloud.", "skills": ["IAM", "Containers", "Terraform"], "certs": ["AWS Security", "AZ-500"]},
    "5": {"nome": "AppSec & DevSecOps", "foco": "Segurança no desenvolvimento de software.", "skills": ["OWASP", "CI/CD", "Python"], "certs": ["CASE", "CSSLP"]},
    "6": {"nome": "Forense (DFIR)", "foco": "Investigar invasões e malwares.", "skills": ["Memória", "Forensics", "Malware"], "certs": ["CHFI", "GCIH"]}
}


while True:
    print("\n" + "="*50)
    print("       KENSEI CYBERSEC PATHFINDER 2026")
    print("="*50)
    
    for numero, info in carreiras.items():
        print(f"{numero} - {info['nome']}")
    
    print("0 - ENCERRAR PROGRAMA") # Nova opção para sair
    
    escolha = input("\nEscolha uma opção (ou 0 para sair): ")

    if escolha == "0":
        print("\nObrigado por usar o Pathfinder! Até a próxima, Samurai.")
        break  # O comando 'break' interrompe o loop e fecha o programa
    
    if escolha in carreiras:
        dados = carreiras[escolha]
        print(f"\n🎯 TRILHA: {dados['nome']}")
        print(f"✅ FOCO: {dados['foco']}")
        print(f"🛠️ SKILLS: {', '.join(dados['skills'])}")
        print(f"📜 CERTS: {', '.join(dados['certs'])}")
        
        # Pausa para o usuário conseguir ler antes do menu reaparecer
        input("\nPressione ENTER para voltar ao menu...")
    else:
        print("\n[!] Opção inválida! Tente novamente.")