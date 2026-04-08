print("--- ORGANIZADOR ALFABÉTICO ---")

# 1. Recebe os nomes separados por vírgula
entrada = input("Digite os nomes separados por vírgula (ex: Aline, Jose, Pedro): ")

# 2. Transforma o texto em uma lista e remove espaços vazios
lista_nomes = [nome.strip() for nome in entrada.split(",")]

# 3. Organiza a lista em ordem alfabética (A-Z)
lista_nomes.sort()

print("\n--- Nomes em Ordem Alfabética ---")
for nome in lista_nomes:
    print(f"-> {nome}")