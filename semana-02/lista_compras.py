lista = []
while True:
    item = input("Digite um item para a lista (ou 'sair' para finalizar): ")
    if item.lower() == 'sair':
        break
    lista.append(item)

print("\n--- Sua Lista Final ---")
for i in lista:
    print(f"- {i}")