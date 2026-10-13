"""Mostra a posição do cursor para calibrar a automação."""
import time
import pyautogui

print("Passe o mouse sobre cada campo. Pressione Ctrl+C para encerrar.")
try:
    while True:
        x, y = pyautogui.position()
        print(f"X={x:4} Y={y:4}", end="\r", flush=True)
        time.sleep(0.2)
except KeyboardInterrupt:
    print("\nFinalizado.")
