
from pathlib import Path
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
RAW = RAIZ / "data" / "raw"
PROCESSED = RAIZ / "data" / "processed"

print("=" * 55)
print("VALIDAÇÃO DOS INDICADORES - PROJECT CONTROL 360")
print("=" * 55)

# Ler as bases originais e os resultados processados
projetos = pd.read_excel(RAW / "projetos.xlsx")
atividades = pd.read_excel(RAW / "atividades.xlsx")
riscos = pd.read_excel(RAW / "riscos.xlsx")

indicadores = pd.read_csv(
    PROCESSED / "indicadores_projetos.csv",
    encoding="utf-8-sig"
)
atividades_status = pd.read_csv(
    PROCESSED / "atividades_por_status.csv",
    encoding="utf-8-sig"
)
riscos_classificados = pd.read_csv(
    PROCESSED / "riscos_classificados.csv",
    encoding="utf-8-sig"
)

erros = []

def verificar(descricao, condicao):
    if condicao:
        print(f"[OK] {descricao}")
    else:
        print(f"[ERRO] {descricao}")
        erros.append(descricao)

# 1. Conferir quantidades
verificar(
    "Quantidade de projetos preservada",
    len(indicadores) == len(projetos)
)
verificar(
    "Quantidade de atividades preservada",
    int(atividades_status["quantidade_atividades"].sum())
    == len(atividades)
)
verificar(
    "Quantidade de riscos preservada",
    len(riscos_classificados) == len(riscos)
)

# 2. Conferir identificadores dos projetos
verificar(
    "Todos os projetos originais estão nos indicadores",
    set(projetos["id_projeto"]) == set(indicadores["id_projeto"])
)

verificar(
    "Não há projetos duplicados nos indicadores",
    indicadores["id_projeto"].is_unique
)

# 3. Conferir cálculo do saldo do orçamento
saldo_calculado = (
    indicadores["orcamento_aprovado"]
    - indicadores["custo_realizado"]
)

verificar(
    "Saldo de orçamento calculado corretamente",
    (saldo_calculado - indicadores["saldo_orcamento"])
    .abs().fillna(0).lt(0.01).all()
)

# 4. Conferir desvio do cronograma
desvio_calculado = (
    indicadores["avanco_realizado_pct"]
    - indicadores["avanco_planejado_pct"]
)

verificar(
    "Desvio de cronograma calculado corretamente",
    (desvio_calculado - indicadores["desvio_cronograma_pp"])
    .abs().fillna(0).lt(0.01).all()
)

# 5. Verificar valores ausentes nos arquivos processados
verificar(
    "Indicadores sem células vazias",
    not indicadores.isnull().any().any()
)
verificar(
    "Atividades por status sem células vazias",
    not atividades_status.isnull().any().any()
)
verificar(
    "Riscos classificados sem células vazias",
    not riscos_classificados.isnull().any().any()
)

# 6. Conferir vínculos entre atividades/riscos e projetos
ids_projetos = set(projetos["id_projeto"])

verificar(
    "Todas as atividades estão vinculadas a projetos existentes",
    set(atividades["id_projeto"]).issubset(ids_projetos)
)
verificar(
    "Todos os riscos estão vinculados a projetos existentes",
    set(riscos["id_projeto"]).issubset(ids_projetos)
)

print("\n" + "=" * 55)
if erros:
    print(f"VALIDAÇÃO COM PENDÊNCIAS: {len(erros)}")
    for erro in erros:
        print(f"- {erro}")
else:
    print("VALIDAÇÃO CONCLUÍDA: todos os testes passaram.")

print("=" * 55)
