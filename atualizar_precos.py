"""Desafio extra: reajustar preços em uma cópia do CSV.
Exemplo: 10% de aumento significa multiplicar cada valor por 1.10.
Não altera diretamente o navegador; gera outro CSV para nova rodada.
"""
import pandas as pd

ARQUIVO_ENTRADA = "produtos_lote_1.csv"
ARQUIVO_SAIDA = "produtos_reajustados.csv"
AUMENTO_PERCENTUAL = 10

tabela = pd.read_csv(ARQUIVO_ENTRADA, dtype=str, keep_default_na=False)
for indice, produto in tabela.iterrows():
    preco_atual = float(produto["valor"])
    novo_preco = round(preco_atual * (1 + AUMENTO_PERCENTUAL / 100), 2)
    tabela.at[indice, "valor"] = f"{novo_preco:.2f}"
    print(produto["modelo"], ":", preco_atual, "->", novo_preco)
tabela.to_csv(ARQUIVO_SAIDA, index=False)
print("Arquivo gerado:", ARQUIVO_SAIDA)
