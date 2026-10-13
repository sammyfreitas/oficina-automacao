"""Mundo SENAI 2026 — GABARITO COMENTADO: cadastro automatizado na TecStore.

Pré-requisitos:
    python -m pip install pyautogui pandas
Abra loja.html no navegador, faça login Admin / senai@123,
deixe o formulário visível, janela maximizada e zoom 100%.
Use pegar_posicao.py para medir o centro do campo CÓDIGO.
Execute apenas depois de concluir e revisar o código.
"""
import time                       # tempos de espera entre ações
import pandas as pd               # leitura de arquivos CSV
import pyautogui                  # mouse e teclado do computador

# Altere para produtos_lote_2.csv, 3 ou 4 nas próximas rodadas.
ARQUIVO = "produtos_lote_1.csv"
POSICAO_CODIGO = (0, 0)          # SUBSTITUIR pelas coordenadas medidas
TEMPO_ESPERA = 0.35              # aumente se o PC estiver lento
TEMPO_INICIAL = 5                # tempo para posicionar a janela da loja

# Se levar o cursor ao canto superior esquerdo, PyAutoGUI interrompe.
pyautogui.FAILSAFE = True
pyautogui.PAUSE = TEMPO_ESPERA

# Mesma ordem dos campos do formulário HTML, do Código ao Estoque.
CAMPOS = ["codigo", "modelo", "fabricante", "categoria", "cor",
          "ano", "descricao", "valor", "estoque"]

def digitar_produto(produto):
    """Preenche um cadastro usando TAB para mudar de campo."""
    pyautogui.click(*POSICAO_CODIGO)     # clica no campo Código
    for indice, campo in enumerate(CAMPOS):
        valor = str(produto[campo])
        pyautogui.write(valor, interval=0.01)  # digita o valor do CSV
        if indice < len(CAMPOS) - 1:
            pyautogui.press("tab")       # avança para o próximo campo
    pyautogui.press("tab")               # sai de Estoque para Salvar produto
    pyautogui.press("enter")             # aciona Salvar
    time.sleep(0.7)                      # aguarda o formulário limpar

def main():
    if POSICAO_CODIGO == (0, 0):
        raise ValueError("Preencha POSICAO_CODIGO usando pegar_posicao.py")
    # dtype=str preserva códigos, zeros iniciais e conteúdo textual.
    tabela = pd.read_csv(ARQUIVO, dtype=str, keep_default_na=False)
    print("Produtos encontrados:", len(tabela))
    print("Confira se o formulário da TecStore está visível.")
    input("Pressione ENTER para começar a contagem regressiva...")
    time.sleep(TEMPO_INICIAL)

    # LOOP: repete o cadastro para cada linha do arquivo.
    for numero, produto in tabela.iterrows():
        digitar_produto(produto)
        print(f"Produto {numero + 1}/{len(tabela)}: {produto['modelo']}")
    print("Fim! Confira a tabela na área administrativa.")

if __name__ == "__main__":
    main()
