# --- DESAFIO 1: calcular_area(largura, altura) ---
def calcular_area(largura, altura):
    area = largura * altura
    return area

# --- DESAFIO 2: e_maior(idade) ---
def e_maior(idade):
    if idade >= 18:
        return True
    else:
        return False

# --- DESAFIO 3: apresentar(nome, curso) ---
def apresentar(nome, curso):
    print(f"Olá! Meu nome é {nome} e estou no curso de {curso}.")

# --- TESTANDO AS FUNÇÕES ---
print("--- Teste de Funções ---")

# Usando a função de área
resultado_area = calcular_area(5, 10)
print("A área do retângulo é:", resultado_area)

# Usando a função de idade
print("Aline é maior de idade?", e_maior(31))

# Usando a função de apresentação
apresentar("Aline", "AI Foundations")