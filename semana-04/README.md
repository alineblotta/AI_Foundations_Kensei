# Semana 04: Integração de APIs de IA (LLMs)

Nesta semana, evoluímos a capacidade dos nossos scripts, conectando-os diretamente a modelos de linguagem (LLMs) via API. O objetivo foi transformar código estático em agentes inteligentes capazes de analisar, traduzir e gerar relatórios autônomos.

## 📂 Estrutura da Pasta
* **`/projetos_base`**: Exercícios fundamentais de integração (Hello API, Assistente com Memória, Analisador de Texto e Tradutor).
* **`/waf_intelligence`**: Projeto Extra de alta complexidade.
    * `gerador_waf.py`: Simulador de telemetria de ataques (OWASP Top 10).
    * `waf_intelligence.py`: Reporter de Inteligência baseado em IA.
* **Segurança**: Arquivos `.env` (variáveis de ambiente) e `.gitignore` para proteção das credenciais.

---

## 🛠️ Trilha de Aprendizado (Projetos Base)

| Script | Foco Técnico | Funcionalidade |
| :--- | :--- | :--- |
| `01_hello_api.py` | Conexão API | Primeira chamada direta ao modelo (OpenAI/Anthropic). |
| `02_assistente.py` | Gestão de Histórico | Chatbot de terminal com memória e *system prompt* personalizado. |
| `03_analisador.py` | Extração Estruturada | Análise de texto com retorno em formato `JSON`. |
| `04_tradutor.py` | Processamento Contextual | Tradução inteligente com suporte a glossário técnico. |

---

## 🚀 Projeto Extra: WAF Threat Intelligence Reporter (`/waf_intelligence`)

Este projeto simula um ambiente real de segurança de borda, onde um **WAF (Web Application Firewall)** atua como primeira barreira de defesa, gerando telemetria que é processada por uma IA para triagem de incidentes.

### 🧠 Arquitetura do Sistema
1. **Gerador de Telemetria (`gerador_waf.py`):**
    * Simula ataques reais (**OWASP Top 10**) em tempo real.
    * Insere registros em `logs_waf.csv` a cada 2 a 5 segundos, simulando tráfego de rede sob ataque.
    * Registra: `timestamp`, `ip_origem`, `tipo_ataque`, `payload` e `criticidade`.

2. **Reporter de Inteligência (`waf_intelligence.py`):**
    * **Processamento (Pandas):** Lê o CSV e consolida estatísticas como volume de ataques e principais IPs ofensores.
    * **Inteligência (LLM/IA):** Atua como um Engenheiro de Detecção Sênior, enviando o resumo dos dados para o modelo `llama-3.3-70b-versatile` via API.
    * **Output:** Gera um **Boletim de Threat Intelligence** técnico para o *Blue Team*.

### 📊 O que o Boletim entrega?
A IA analisa o contexto e entrega um relatório com:
* **Sumário Executivo:** Saúde da segurança de borda.
* **Análise de Ameaças:** Avaliação técnica dos payloads perigosos.
* **Recomendações:** Direcionamento prático para mitigação.

---

## 🔐 Configuração e Segurança (Obrigatório)
* **`.env`**: Armazena as chaves de API. **Nunca deve ser enviado ao GitHub.**
* **`.gitignore`**: Configurado para ignorar o arquivo `.env`. Verifique sempre seu `git status`.

---

## 📚 Aprendizados da Semana
* **Arquitetura API:** Entendimento do fluxo "Pedido > Garçom (API) > Servidor IA > Resposta".
* **System Prompt:** Definição de personalidade técnica (Engenheiro de Detecção).
* **Automação de Inteligência:** Processamento de logs em escala com Pandas + LLMs.
* **Boas Práticas:** Monitoramento de custos, gestão de limites (Rate Limits) e privacidade de dados.

---
*Kensei Cyber AI Academy 2026 | Foco: Conectando Python ao Cérebro da IA*