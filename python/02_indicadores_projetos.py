
from pathlib import Path
import pandas as pd

# Caminhos do projeto
RAIZ = Path(__file__).resolve().parent.parent
PASTA_RAW = RAIZ / "data" / "raw"
PASTA_PROCESSED = RAIZ / "data" / "processed"
PASTA_PROCESSED.mkdir(parents=True, exist_ok=True)

# Leitura das bases
projetos = pd.read_excel(PASTA_RAW / "projetos.xlsx")
atividades = pd.read_excel(PASTA_RAW / "atividades.xlsx")
riscos = pd.read_excel(PASTA_RAW / "riscos.xlsx")

# Padronização das datas
for coluna in ["data_inicio", "data_fim_planejada"]:
    projetos[coluna] = pd.to_datetime(projetos[coluna], errors="coerce")

atividades["data_fim_planejada"] = pd.to_datetime(
    atividades["data_fim_planejada"], errors="coerce"
)

riscos["data_limite"] = pd.to_datetime(
    riscos["data_limite"], errors="coerce"
)

# 1. Indicadores financeiros e de cronograma
indicadores = projetos.copy()

indicadores["saldo_orcamento"] = (
    indicadores["orcamento_aprovado"]
    - indicadores["custo_realizado"]
)

indicadores["percentual_orcamento_consumido"] = (
    indicadores["custo_realizado"]
    .div(indicadores["orcamento_aprovado"].where(
        indicadores["orcamento_aprovado"] != 0
    ))
    .mul(100)
    .round(2)
)

indicadores["desvio_cronograma_pp"] = (
    indicadores["avanco_realizado_pct"]
    - indicadores["avanco_planejado_pct"]
)

indicadores["situacao_cronograma"] = indicadores[
    "desvio_cronograma_pp"
].apply(
    lambda x: "Atrasado" if x < 0
    else "No planejado ou adiantado"
)

# 2. Quantidade de atividades por projeto
resumo_atividades = atividades.groupby(
    "id_projeto"
).agg(
    total_atividades=("id_atividade", "count"),
    atividades_concluidas=("status", lambda s: s.astype(str).str.strip().str.lower().isin(
        ["concluída", "concluida", "concluído", "concluido", "concluído(a)", "concluída(o)"]
    ).sum()),
).reset_index()

# Quantidade por status para análise no Power BI
atividades_por_status = atividades.groupby(
    ["id_projeto", "status"]
).size().reset_index(name="quantidade_atividades")

indicadores = indicadores.merge(
    resumo_atividades, on="id_projeto", how="left"
)

# 3. Classificação de riscos
def classificar_risco(linha):
    probabilidade = str(linha["probabilidade"]).strip().lower()
    impacto = str(linha["impacto"]).strip().lower()

    niveis = {
        "muito baixa": 1, "muito baixo": 1,
        "baixa": 2, "baixo": 2,
        "média": 3, "media": 3, "médio": 3, "medio": 3,
        "alta": 4, "alto": 4,
        "muito alta": 5, "muito alto": 5,
    }

    try:
        p = int(float(probabilidade))
    except ValueError:
        p = niveis.get(probabilidade, 0)

    try:
        i = int(float(impacto))
    except ValueError:
        i = niveis.get(impacto, 0)

    pontuacao = p * i

    if pontuacao == 0:
        return "Revisar classificação"
    elif pontuacao >= 15:
        return "Crítico"
    elif pontuacao >= 8:
        return "Alto"
    elif pontuacao >= 4:
        return "Moderado"
    else:
        return "Baixo"

riscos["criticidade"] = riscos.apply(classificar_risco, axis=1)

# 4. Quantidade de riscos por projeto
resumo_riscos = riscos.groupby("id_projeto").agg(
    total_riscos=("id_risco", "count"),
    riscos_criticos=("criticidade", lambda s: (s == "Crítico").sum()),
    riscos_altos=("criticidade", lambda s: (s == "Alto").sum()),
).reset_index()

indicadores = indicadores.merge(
    resumo_riscos, on="id_projeto", how="left"
)

colunas_contagem = [
    "total_atividades", "atividades_concluidas",
    "total_riscos", "riscos_criticos", "riscos_altos"
]
indicadores[colunas_contagem] = indicadores[colunas_contagem].fillna(0).astype(int)

# 5. Exportação dos resultados
indicadores.to_csv(
    PASTA_PROCESSED / "indicadores_projetos.csv",
    index=False, encoding="utf-8-sig"
)

atividades_por_status.to_csv(
    PASTA_PROCESSED / "atividades_por_status.csv",
    index=False, encoding="utf-8-sig"
)

riscos.to_csv(
    PASTA_PROCESSED / "riscos_classificados.csv",
    index=False, encoding="utf-8-sig"
)

print("=" * 50)
print("INDICADORES DO PROJECT CONTROL 360")
print("=" * 50)
print(f"Projetos analisados: {len(indicadores)}")
print(f"Atividades analisadas: {len(atividades)}")
print(f"Riscos analisados: {len(riscos)}")
print("\nIndicadores por projeto:")
print(indicadores[[
    "nome_projeto",
    "saldo_orcamento",
    "desvio_cronograma_pp",
    "total_atividades",
    "total_riscos"
]].to_string(index=False))

print("\nArquivos gerados em data/processed:")
print("- indicadores_projetos.csv")
print("- atividades_por_status.csv")
print("- riscos_classificados.csv")
print("\nProcessamento concluído.")
