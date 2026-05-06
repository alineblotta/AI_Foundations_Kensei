# --- 1. O LOOP 'FOR' (Para cada item na lista) ---
print("--- Escaneando Ferramentas ---")
ferramentas = ["Nmap", "Burp Suite", "Wireshark"]

for item in ferramentas:
    print("Verificando instalação de:", item)

# --- DESAFIO 1: Imprimir números de 1 a 10 ---
print("--- Números de 1 a 10 ---")
for i in range(1, 11): # Começa em 1 e para antes do 11
    print(i)

# --- DESAFIO 2: Percorrer uma lista de nomes ---
print("\n--- Lista de Analistas ---")
nomes = ["Aline", "Jose", "Pedro", "Araujo", "Everton"]
for pessoa in nomes:
    print("Analista logado:", pessoa)

# --- DESAFIO 3 (BÔNUS): Tabuada ---
print("\n--- Tabuada do 5 ---")
numero = 5
for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")