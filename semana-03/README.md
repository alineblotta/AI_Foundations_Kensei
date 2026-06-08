# Semana 03: Análise de Dados com Pandas

Nesta semana, o foco foi a transição da lógica de programação para a manipulação de dados em larga escala. Utilizamos a biblioteca **Pandas** para tratar logs e datasets, aplicando técnicas de limpeza, análise estatística e visualização para gerar inteligência de segurança.

## 📂 Estrutura da Pasta
* **`/projetos_1_ao_4`**: Exercícios de fundamentação em Pandas e Matplotlib.
    * `/graficos`: Artefatos visuais gerados durante os exercícios de aprendizagem.
* **`/projeto_5_final`**: Pipeline unificado de análise de ataques cibernéticos.
    * `/graficos`: Dashboards de segurança gerados automaticamente pela análise.

---

## 🛠️ Exercícios (Projetos 1 a 4)

| Script | Foco Técnico | Conceitos Práticos |
| :--- | :--- | :--- |
| `01_explorar.py` | Carga de Dados | `read_csv`, `head`, `info`, `describe`, `isnull`. |
| `02_limpar.py` | Higienização | Tratamento de nulos, duplicados (`drop_duplicates`) e tipos de dados. |
| `03_filtrar.py` | Agrupamento | Filtragem condicional, `groupby`, contagem e ordenação. |
| `04_graficos.py` | Visualização | Criação de gráficos (barras, linhas, pizza) com `Matplotlib`. |

---

## 🚀 Projeto 5: Análise de Inteligência de Ameaças

### 🎯 Objetivo
Automatizar um pipeline de dados ponta a ponta para analisar um dataset de ataques cibernéticos simulados, identificando padrões de severidade por país, volumetria por tipo de vetor e a distribuição estatística dos incidentes.

### 🛠️ Ferramentas Utilizadas
* **Python 3.12**
* **Pandas:** Manipulação, agrupamento (`groupby`) e tratamento dos logs de segurança.
* **Seaborn & Matplotlib:** Engenharia de visualização avançada com aplicação de temas modernos (`whitegrid`) e tratamento de conformidade de código (`hue mapping`).

### 📊 Insights Obtidos
* **Severidade por Fronteira:** Identificação e cálculo exato dos países com maior média de impacto e criticidade em incidentes.
* **Volumetria de Vetores:** Mapeamento quantitativo dos tipos de ataques (ex: DDoS, SQLi, Logins Falhos) para direcionamento de regras de firewall.
* **Análise de Frequência:** Distribuição estatística do score de severidade para entender a tendência e o comportamento geral das ameaças.

### 📂 Estrutura do Projeto
* `cyber_attacks_simulated.csv`: Base de dados de telemetria e logs simulados.
* `05_analise_completa.py`: Script unificado contendo o pipeline de carga, processamento, análise e plotagem.
* `graficos/`: Diretório gerado dinamicamente para armazenamento dos artefatos visuais.

### 🖼️ Resultado da Análise
*(Aqui você pode adicionar o link ou exibir os gráficos salvos na pasta, ex: `![Dashboard](projeto_5_final/graficos/nome_do_grafico.png)`)*

---

## 📚 Aprendizados da Semana
* **O que são Dados:** Compreensão da diferença entre dados estruturados (CSV/Logs de Firewall), semi-estruturados e não-estruturados.
* **Ecossistema Python:** Domínio de Pandas para tratamento de tabelas e Matplotlib/Seaborn para relatórios visuais profissionais.
* **Fluxo de Trabalho:** A importância da limpeza de dados (processo que ocupa 80% do tempo) e da conversão de dados brutos em informações acionáveis para a tomada de decisão em segurança.

---
*Kensei Cyber AI Academy 2026 | Foco: Dados como fonte de inteligência de segurança*