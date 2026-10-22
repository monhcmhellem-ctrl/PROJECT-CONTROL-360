# 📊 PROJECT CONTROL 360
### Gestão de Projetos orientada por dados | Python • Pandas • Power BI

O **PROJECT CONTROL 360** é um projeto de portfólio desenvolvido para demonstrar como dados podem apoiar a gestão de projetos, proporcionando uma visão executiva de prazos, orçamento, atividades e riscos.

A proposta é transformar dados operacionais em indicadores claros e objetivos, facilitando o acompanhamento do desempenho dos projetos e contribuindo para decisões mais assertivas.

> **Minha filosofia em Business Intelligence: menos pode ser mais.**
>
> Acredito que um bom BI não é aquele que apresenta a maior quantidade de informações, mas aquele que consegue comunicar o que realmente importa. Prefiro dashboards limpos, intuitivos e objetivos, que permitam identificar desvios, compreender resultados e direcionar ações sem sobrecarregar o usuário com informações que não geram valor.
>
> Para mim, a qualidade de um dashboard está na sua capacidade de transformar dados em entendimento e entendimento em decisão.

---

## 🎯 Objetivo do projeto

Desenvolver uma solução de acompanhamento gerencial que centralize indicadores essenciais para a gestão de projetos, permitindo analisar:

- Desempenho dos projetos em relação ao cronograma planejado;
- Orçamento aprovado versus custo realizado;
- Saldo orçamentário disponível;
- Situação das atividades por status;
- Distribuição de riscos por criticidade;
- Indicadores executivos para apoiar a priorização e a tomada de decisão.

## 📈 Dashboard executivo

O dashboard foi desenvolvido com foco em **clareza visual, hierarquia das informações e facilidade de interpretação**.

A proposta é permitir que gestores identifiquem rapidamente os principais pontos de atenção, sem precisar percorrer diversas telas ou analisar gráficos desnecessariamente complexos.

### Indicadores acompanhados

- Total de projetos;
- Orçamento aprovado;
- Custo realizado;
- Saldo orçamentário;
- Projetos com desempenho abaixo do planejado;
- Percentual do orçamento consumido;
- Atividades por status;
- Riscos classificados por criticidade.

Os indicadores e resultados apresentados utilizam dados fictícios, criados exclusivamente para fins de demonstração e portfólio.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python | Criação e processamento das bases de dados |
| Pandas | Tratamento, organização e consolidação dos dados |
| Excel | Estruturação das bases de entrada |
| Power BI | Modelagem, criação de medidas DAX e visualização dos indicadores |
| Git e GitHub | Versionamento e documentação do projeto |

## ⚙️ Etapas do desenvolvimento

**1. Estruturação dos dados**

Criação de bases fictícias para representar projetos, atividades e riscos.

**2. Processamento com Python**

Desenvolvimento de scripts para gerar as bases e consolidar indicadores gerenciais.

**3. Validação dos dados**

Verificação da integridade das bases e dos indicadores calculados, incluindo testes automatizados por script.

**4. Modelagem e análise no Power BI**

Importação dos dados, criação dos relacionamentos e desenvolvimento de medidas DAX para acompanhamento dos indicadores.

**5. Construção do dashboard**

Organização dos elementos visuais com foco em leitura rápida, objetividade e identificação dos principais pontos de atenção.

## 💡 Conceito de BI aplicado ao projeto

A construção deste dashboard parte de uma premissa: **informação em excesso não significa necessariamente mais conhecimento**.

Um dashboard eficiente deve responder às perguntas certas:

- O projeto está evoluindo conforme o planejado?
- O orçamento está sendo consumido de forma compatível com o andamento?
- Quais atividades exigem atenção?
- Quais riscos demandam prioridade?
- Onde a gestão precisa atuar?

A intenção é reduzir o esforço necessário para interpretar os dados e facilitar a identificação de oportunidades de melhoria.

**Menos poluição visual. Mais clareza. Menos volume sem propósito. Mais informação útil para decidir.**

## 📂 Estrutura do projeto

```text
PROJECT_CONTROL_360/
├── data/
│   ├── raw/
│   │   ├── projetos.xlsx
│   │   ├── atividades.xlsx
│   │   └── riscos.xlsx
│   └── processed/
│       ├── indicadores_projetos.csv
│       ├── atividades_por_status.csv
│       └── riscos_classificados.csv
├── python/
│   ├── 00_criar_bases.py
│   ├── 01_validar_bases.py
│   ├── 02_indicadores_projetos.py
│   └── 03_validar_indicadores.py
├── PROJECT_CONTROL_360.pbix
└── .gitignore
```

## 🚀 Competências demonstradas

- Gestão e acompanhamento de projetos;
- Construção e análise de indicadores de desempenho;
- Análise de cronograma, orçamento, atividades e riscos;
- Automação do processamento de dados com Python e Pandas;
- Modelagem de dados e criação de medidas DAX;
- Validação de dados e indicadores;
- Visualização de dados orientada à tomada de decisão;
- Organização, documentação e versionamento de projetos.

## 📌 Considerações finais

O PROJECT CONTROL 360 representa minha visão de como tecnologia, gestão e análise de dados podem trabalhar juntas para gerar valor.

Mais do que construir dashboards, busco desenvolver soluções que ajudem as pessoas a compreender cenários, identificar prioridades e agir com mais segurança.

**Acredito que um bom BI não precisa dizer tudo. Precisa mostrar, com clareza, aquilo que realmente importa.**

---

*Projeto de portfólio desenvolvido com dados fictícios para fins de estudo e demonstração de competências em Business Intelligence, automação e gestão de projetos.*
