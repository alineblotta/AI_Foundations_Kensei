# 1) Criando uma lista com 5 ferramentas de cyber
ferramentas = ["Burp Suite", "Metasploit", "Wireshark", "Nmap", "ModSecurity"]

print("--- Minha Lista de Ferramentas ---")
print("A ferramenta principal é:", ferramentas[0]) # Mostra Burp Suite
print("Total de ferramentas:", len(ferramentas))

# 2) Criando um dicionário com seus dados pessoais
meu_perfil = {
    "nome": "Aline Blotta",
    "cargo": "Analista de Segurança",
    "empresa": "Hospital Sírio-Libanês",
    "especialidade": "Cyber Defense"
}

print("\n--- Meus Dados Pessoais ---")
print("Nome:", meu_perfil["nome"])
print("Trabalho no:", meu_perfil["empresa"])

# Adicionando uma nova informação
meu_perfil["status"] = "Estudando IA"
print("Ficha completa atualizada:", meu_perfil)