# Projeto 5: Análise de Inteligência de Ameaças - Semana 03

## 🎯 Objetivo
Automatizar um pipeline de dados ponta a ponta para analisar um dataset de ataques cibernéticos simulados, identificando padrões de severidade por país, volumetria por tipo de vetor e a distribuição estatística dos incidentes.

## 🛠️ Ferramentas Utilizadas
- **Python 3.12**
- **Pandas**: Manipulação, agrupamento (`groupby`) e tratamento dos logs de segurança.
- **Seaborn & Matplotlib**: Engenharia de visualização avançada com aplicação de temas modernos (`whitegrid`) e tratamento de conformidade de código (`hue` mapping).

## 📊 Insights Obtidos
- **Severidade por Fronteira:** Identificação e cálculo exato dos países com maior média de impacto e criticidade em incidentes.
- **Volumetria de Vetores:** Mapeamento quantitativo dos tipos de ataques (ex: DDoS, SQLi, Logins Falhos) para direcionamento de regras de firewall.
- **Análise de Frequência:** Distribuição estatística do score de severidade para entender a tendência e o comportamento geral das ameaças.

## 📂 Estrutura do Projeto
- `cyber_attacks_simulated.csv`: Base de dados de telemetria e logs simulados.
- `05_analise_completa.py`: Script unificado contendo o pipeline de carga, processamento, análise e plotagem.
- `graficos/`: Diretório gerado dinamicamente para armazenamento dos artefatos visuais.

### 🖼️ Resultado da Análise
![Dashboard de Segurança](graficos/dashboard_cyber.png)