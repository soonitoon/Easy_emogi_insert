import pyautogui as pag
import pyperclip
import keyboard

def emogi_insert(key):
    if key == 'heart':
        pyperclip.copy('❤')
        pag.keyDown('ctrl')
        pag.keyDown('v')
        pag.keyUp('ctrl')
        pag.keyUp('v')

    elif key == 'smile':
        pyperclip.copy('☺')
        pag.keyDown('ctrl')
        pag.keyDown('v')
        pag.keyUp('ctrl')
        pag.keyUp('v')

    elif key == 'funny':
        pyperclip.copy('😆')
        pag.keyDown('ctrl')
        pag.keyDown('v')
        pag.keyUp('ctrl')
        pag.keyUp('v')

    elif key == 'sad':
        pyperclip.copy('😢')
        pag.keyDown('ctrl')
        pag.keyDown('v')
        pag.keyUp('ctrl')
        pag.keyUp('v')

    elif key == 'love':
        pyperclip.copy('🥰')
        pag.keyDown('ctrl')
        pag.keyDown('v')
        pag.keyUp('ctrl')
        pag.keyUp('v')

    elif key == 'dislike':
        pyperclip.copy('😫')
        pag.keyDown('ctrl')
        pag.keyDown('v')
        pag.keyUp('ctrl')
        pag.keyUp('v')

    elif key == 'happy':
        pyperclip.copy('😚')
        pag.keyDown('ctrl')
        pag.keyDown('v')
        pag.keyUp('ctrl')
        pag.keyUp('v')

    elif key == 'fire':
        pyperclip.copy('🔥')
        pag.keyDown('ctrl')
        pag.keyDown('v')
        pag.keyUp('ctrl')
        pag.keyUp('v')

    elif key == 'what':
        pyperclip.copy('😶')
        pag.keyDown('ctrl')
        pag.keyDown('v')
        pag.keyUp('ctrl')
        pag.keyUp('v')

    elif key == 'star':
        pyperclip.copy('⭐')
        pag.keyDown('ctrl')
        pag.keyDown('v')
        pag.keyUp('ctrl')
        pag.keyUp('v')


keyboard.add_hotkey('F1', lambda: emogi_insert('heart'))
keyboard.add_hotkey('F2', lambda: emogi_insert('smile'))
keyboard.add_hotkey('F3', lambda: emogi_insert('funny'))
keyboard.add_hotkey('F4', lambda: emogi_insert('love'))
keyboard.add_hotkey('F5', lambda: emogi_insert('happy'))
keyboard.add_hotkey('F6', lambda: emogi_insert('dislike'))
keyboard.add_hotkey('F7', lambda: emogi_insert('sad'))
keyboard.add_hotkey('F8', lambda: emogi_insert('what'))
keyboard.add_hotkey('F9', lambda: emogi_insert('fire'))
keyboard.add_hotkey('F11', lambda: emogi_insert('star'))

keyboard.wait('F12')
