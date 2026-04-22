import os
import shutil

print("--- ORGANIZADOR DE ARQUIVOS E TRIAGEM ---")

# 1. Recebe os nomes dos arquivos (ex: foto.jpg, virus.exe, nota.pdf)
entrada = input("Digite os nomes dos arquivos com extensão, separados por vírgula: ")

# 2. Transforma em lista e remove espaços
arquivos = [arq.strip() for arq in entrada.split(",")]

# 3. Organiza a lista em ordem alfabética (A-Z) para a exibição ficar bonita
arquivos.sort()

# Criar a pasta de quarentena por segurança se ela não existir
if not os.path.exists("quarentena"):
    os.makedirs("quarentena")

print("\n--- Processando Arquivos ---")

for arquivo in arquivos:
    # Identifica o que é malicioso (extensão .exe ou .bat)
    if arquivo.endswith(".exe") or arquivo.endswith(".bat"):
        print(f"⚠️  ALERTA: {arquivo} é potencialmente malicioso! Movendo para QUARENTENA.")
        # Aqui o Python tentaria mover o arquivo real se ele existir na pasta
        if os.path.exists(arquivo):
            shutil.move(arquivo, "quarentena/" + arquivo)
    
    # Identifica o que é documento ou imagem
    elif arquivo.endswith(".pdf") or arquivo.endswith(".jpg"):
        print(f"✅ {arquivo} identificado como arquivo seguro.")
    
    # Se for outra coisa
    else:
        print(f"-> {arquivo} adicionado à lista de processamento.")

print("\n--- Organização Concluída! ---")