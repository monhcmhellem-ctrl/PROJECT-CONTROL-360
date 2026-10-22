
from pathlib import Path
import pandas as pd

# Identificar a pasta principal do projeto
RAIZ = Path(__file__).resolve().parent.parent
PASTA_DADOS = RAIZ / "data" / "raw"

# Criar a pasta de destino, caso necessário
PASTA_DADOS.mkdir(parents=True, exist_ok=True)

# 1. Base de projetos
projetos = pd.DataFrame([
    {
        "id_projeto": "P001",
        "nome_projeto": "Implantacao Sistema de Gestao",
        "responsavel": "Ana",
        "area": "Tecnologia",
        "data_inicio": "2026-09-01",
        "data_fim_planejada": "2026-12-15",
        "orcamento_aprovado": 80000,
        "custo_realizado": 42000,
        "status": "Em andamento",
        "avanco_planejado_pct": 60,
        "avanco_realizado_pct": 50
    },
    {
        "id_projeto": "P002",
        "nome_projeto": "Melhoria de Processos",
        "responsavel": "Carlos",
        "area": "Operacoes",
        "data_inicio": "2026-08-01",
        "data_fim_planejada": "2026-11-30",
        "orcamento_aprovado": 45000,
        "custo_realizado": 30000,
        "status": "Em andamento",
        "avanco_planejado_pct": 75,
        "avanco_realizado_pct": 80
    },
    {
        "id_projeto": "P003",
        "nome_projeto": "Implantacao de Indicadores",
        "responsavel": "Mariana",
        "area": "Qualidade",
        "data_inicio": "2026-07-01",
        "data_fim_planejada": "2026-10-15",
        "orcamento_aprovado": 30000,
        "custo_realizado": 32000,
        "status": "Em andamento",
        "avanco_planejado_pct": 100,
        "avanco_realizado_pct": 85
    },
    {
        "id_projeto": "P004",
        "nome_projeto": "Automacao de Relatorios",
        "responsavel": "Joao",
        "area": "Tecnologia",
        "data_inicio": "2026-09-15",
        "data_fim_planejada": "2027-01-30",
        "orcamento_aprovado": 60000,
        "custo_realizado": 12000,
        "status": "Em andamento",
        "avanco_planejado_pct": 25,
        "avanco_realizado_pct": 20
    },
    {
        "id_projeto": "P005",
        "nome_projeto": "Padronizacao Operacional",
        "responsavel": "Beatriz",
        "area": "Operacoes",
        "data_inicio": "2026-06-01",
        "data_fim_planejada": "2026-09-30",
        "orcamento_aprovado": 25000,
        "custo_realizado": 24000,
        "status": "Concluido",
        "avanco_planejado_pct": 100,
        "avanco_realizado_pct": 100
    }
])

# 2. Base de atividades
atividades = pd.DataFrame([
    ["A001", "P001", "Mapear requisitos", "Ana", "2026-09-10", "2026-09-20", "Concluida"],
    ["A002", "P001", "Configurar sistema", "Ana", "2026-09-21", "2026-10-25", "Em andamento"],
    ["A003", "P001", "Realizar testes", "Carlos", "2026-10-20", "2026-11-20", "Pendente"],
    ["A004", "P002", "Mapear processos", "Carlos", "2026-08-05", "2026-08-25", "Concluida"],
    ["A005", "P002", "Implementar melhorias", "Carlos", "2026-09-01", "2026-10-30", "Em andamento"],
    ["A006", "P003", "Definir indicadores", "Mariana", "2026-07-05", "2026-08-15", "Concluida"],
    ["A007", "P003", "Validar resultados", "Mariana", "2026-08-16", "2026-10-15", "Em andamento"],
    ["A008", "P004", "Desenvolver automacao", "Joao", "2026-09-20", "2026-12-15", "Em andamento"],
    ["A009", "P004", "Validar relatorios", "Joao", "2026-12-16", "2027-01-20", "Pendente"],
    ["A010", "P005", "Documentar processos", "Beatriz", "2026-06-05", "2026-09-15", "Concluida"],
    ["A011", "P005", "Treinar equipe", "Beatriz", "2026-09-16", "2026-09-30", "Concluida"],
], columns=[
    "id_atividade", "id_projeto", "atividade", "responsavel",
    "data_inicio", "data_fim_planejada", "status"
])

# 3. Base de riscos
riscos = pd.DataFrame([
    ["R001", "P001", "Atraso na configuracao", 4, 4, "Ana", "2026-11-05", "Em tratamento"],
    ["R002", "P001", "Falha nos testes", 3, 5, "Carlos", "2026-11-10", "Aberto"],
    ["R003", "P002", "Resistencia da equipe", 3, 3, "Carlos", "2026-10-25", "Em tratamento"],
    ["R004", "P003", "Indicadores inconsistentes", 4, 5, "Mariana", "2026-10-10", "Aberto"],
    ["R005", "P004", "Atraso no desenvolvimento", 3, 4, "Joao", "2026-12-01", "Aberto"],
    ["R006", "P005", "Baixa adesao ao processo", 2, 3, "Beatriz", "2026-09-20", "Encerrado"],
], columns=[
    "id_risco", "id_projeto", "descricao_risco",
    "probabilidade", "impacto", "responsavel",
    "data_limite", "status"
])

# Salvar as três bases em Excel
projetos.to_excel(PASTA_DADOS / "projetos.xlsx", index=False)
atividades.to_excel(PASTA_DADOS / "atividades.xlsx", index=False)
riscos.to_excel(PASTA_DADOS / "riscos.xlsx", index=False)

print("Bases criadas com sucesso!")
print(f"Local dos arquivos: {PASTA_DADOS}")
print(f"Projetos: {len(projetos)}")
print(f"Atividades: {len(atividades)}")
print(f"Riscos: {len(riscos)}")
