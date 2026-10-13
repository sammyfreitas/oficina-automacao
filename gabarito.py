"""Gabarito demonstrativo — Mundo SENAI 2026.
Use apenas na loja simulada da oficina. Ajuste POSICOES após executar pegar_posicao.py.
Execute a loja em navegador com zoom 100%, janela maximizada e resolução estável.
"""
import time
import pandas as pd
import pyautogui

ARQUIVO = "produtos.csv"
PAUSA = 0.4
pyautogui.PAUSE = PAUSA
pyautogui.FAILSAFE = True  # mover o mouse ao canto superior esquerdo interrompe a automação

# Preencher depois de medir os campos com pegar_posicao.py.
POSICOES = {
    "codigo": (0, 0),
    "modelo": (0, 0),
    "fabricante": (0, 0),
    "categoria": (0, 0),
    "cor": (0, 0),
    "ano": (0, 0),
    "descricao": (0, 0),
    "valor": (0, 0),
    "estoque": (0, 0),
    "salvar": (0, 0),
}

def preencher(campo, valor):
    pyautogui.click(*POSICOES[campo])
    pyautogui.hotkey("ctrl", "a")
    pyautogui.write(str(valor), interval=0.01)

def cadastrar(produto):
    for campo in ("codigo", "modelo", "fabricante", "categoria", "cor",
                  "ano", "descricao", "valor", "estoque"):
        preencher(campo, produto[campo])
    pyautogui.click(*POSICOES["salvar"])
    time.sleep(0.5)

def main():
    if any(x == (0, 0) for x in POSICOES.values()):
        raise ValueError("Meça e preencha as posições de todos os campos antes de executar.")
    tabela = pd.read_csv(ARQUIVO, dtype=str, keep_default_na=False)
    print(f"{len(tabela)} produtos encontrados. Abra a área administrativa da loja.")
    input("Deixe o formulário visível e pressione Enter para começar em 5 segundos...")
    time.sleep(5)
    for indice, produto in tabela.iterrows():
        cadastrar(produto)
        print(f"{indice + 1}/{len(tabela)}: {produto['modelo']}")
    print("Cadastro concluído.")

if __name__ == "__main__":
    main()
