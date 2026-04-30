# PROJETO: Auditoria de Segurança (Origem: Exercício Lista de Compras)
# Descrição: Evolução da lógica de listas para um contexto de conformidade técnica.

# 1. Definição do Tipo de Host
tipo_host = input("O host é uma Estação de Trabalho ou Servidor? (E/S): ").upper()

# 2. Lista base de requisitos
requisitos = [
    "EDR Instalado",
    "Patch de Segurança Atualizado",
    "Criptografia de Disco (BitLocker)",
    "Firewall Local Habilitado"
]

# 3. Regra condicional para DLP
if tipo_host == "E":
    requisitos.append("DLP Ativo (Proteção de Dados)")

pendencias = []

print(f"\n--- 🛡️ AUDITORIA DE PRÉ-ADMISSÃO: {'ESTAÇÃO' if tipo_host == 'E' else 'SERVIDOR'} ---")

for item in requisitos:
    status = input(f"{item} está OK? (S/N): ").upper()
    if status != 'S':
        pendencias.append(item)

# 4. Resultado Final
print("\n" + "="*40)
if not pendencias:
    print("✅ STATUS: APROVADO PARA REDE")
else:
    print("❌ STATUS: BLOQUEADO")
    print("Pendências encontradas:")
    for p in pendencias:
        print(f"  - {p}")
print("="*40)