
from pathlib import Path
import pandas as pd

# Identifica a pasta principal do projeto
RAIZ = Path(__file__).resolve().parent.parent
PASTA_DADOS = RAIZ / "data" / "raw"

arquivos = {
    "Projetos": PASTA_DADOS / "projetos.xlsx",
    "Atividades": PASTA_DADOS / "atividades.xlsx",
    "Riscos": PASTA_DADOS / "riscos.xlsx",
}

print("=" * 50)
print("VALIDAÇÃO DAS BASES - PROJECT CONTROL 360")
print("=" * 50)

for nome, caminho in arquivos.items():
    print(f"\n--- {nome} ---")

    if not caminho.exists():
        print(f"ERRO: arquivo não encontrado: {caminho.name}")
        continue

    try:
        df = pd.read_excel(caminho)

        print(f"Arquivo: {caminho.name}")
        print(f"Quantidade de registros: {len(df)}")
        print(f"Quantidade de colunas: {len(df.columns)}")
        print(f"Colunas: {', '.join(df.columns)}")

        ausentes = int(df.isnull().sum().sum())
        print(f"Células vazias: {ausentes}")

        if ausentes > 0:
            print("ATENÇÃO: existem células vazias para analisar.")
        else:
            print("OK: nenhuma célula vazia encontrada.")

    except Exception as erro:
        print(f"ERRO ao ler o arquivo: {erro}")

print("\nValidação concluída.")
