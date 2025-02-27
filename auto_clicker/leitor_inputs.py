import pyautogui
from pynput import keyboard
from pynput import mouse
import time

write_lines = []
stop_running = False
ultimo_press = 0

with open("autoclick_saves/teste.py", "w") as script:
    write_lines.append(f"import pyautogui\n")
    write_lines.append(f"import time\n")
    write_lines.append("\n")

def on_press(key):
    global ultimo_press

    try:
        if ultimo_press == 0:
            timer = 0
        else:
            timer = round(time.time() - ultimo_press)

        print(f'Tecla pressionada: {key.char}')
        write_lines.append(f"time.sleep({timer})\n")
        write_lines.append(f"pyautogui.press('{key.char}')\n")
        ultimo_press = time.time()

    except AttributeError:
        print(f'Tecla especial pressionada: {key}')
        if key == keyboard.Key.enter:
            write_lines.append(f"time.sleep({timer})\n")
            write_lines.append(f"pyautogui.press('enter')\n")
            ultimo_press = time.time()
        if key == keyboard.Key.backspace:
            write_lines.append(f"time.sleep({timer})\n")
            write_lines.append(f"pyautogui.press('backspace')\n")
            ultimo_press = time.time()
        if key == keyboard.Key.space:
            write_lines.append(f"time.sleep({timer})\n")
            write_lines.append(f"pyautogui.press('spaced')\n")
            ultimo_press = time.time()

def on_release(key):
    global stop_running

    print(f'Tecla liberada: {key}')
    if key == keyboard.Key.esc:
        # Para o listener
        stop_running = True
        return False

def on_click(x, y, button, pressed):
    global ultimo_press

    if ultimo_press == 0:
        timer = 0
    else:
        timer = round(time.time() - ultimo_press)

    if stop_running:
        return False

    if pressed:
        print(f'Botão {button} pressionado em {x}, {y}')
        write_lines.append(f"time.sleep({timer})\n")
        write_lines.append(f"pyautogui.moveTo({x}, {y})\n")
        write_lines.append(f"time.sleep({0.5})\n")
        write_lines.append(f"pyautogui.click()\n")
        ultimo_press = time.time()
    else:
        print(f'Botão {button} liberado em {x}, {y}')

# Coleta eventos de teclado
with keyboard.Listener(on_press=on_press, on_release=on_release, on_click=on_click) as listener_keyboard:  
    with mouse.Listener(on_click=on_click) as listener_mouse:
        listener_mouse.join()
    listener_keyboard.join()


def write_in_script():

    with open("autoclick_saves/teste.py", "w") as script:
            for i in write_lines:
                script.write(f"{i}")

write_in_script()

