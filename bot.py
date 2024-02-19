import pyautogui as py
import time as tm

def placaBD():

    py.keyDown('ctrl')
    py.keyDown('ctrl')
    py.keyDown('c')
    py.keyUp('c')
    py.keyUp('ctrl')

    py.hotkey('alt', 'tab')
    
    py.PAUSE = 0.95
    py.press('pageup', presses=2)
    py.scroll(10000)
    """Consulta ao sistema e colocar a placa no banco BD"""
    py.click (x= -685, y = 414, duration=0.25)
    py.moveTo (x= -747, y =479, duration=0.25)
    py.click(clicks=2)
    py.hotkey('ctrl', 'v')
    tm.sleep(4)
    py.press('esc')
    py.click(x=-760,y=471)
    tm.sleep(0.65)
    py.press('esc')

    py.hotkey('alt', 'tab')
    py.press('right')
    py.hotkey('ctrl', 'c')
    py.hotkey('alt', 'tab')

    py.click(x=-680,y=562)
    py.moveTo (x=-746, y=625, duration=0.25)
    py.click(clicks=2)
    py.hotkey('ctrl', 'v')
    tm.sleep(4)

    py.press('esc')
    tm.sleep(0.65)
    py.click(x=-516,y=633)
    py.press('esc')

    py.press('left', presses=4)
    py.press('enter')
    py.hotkey('ctrl', 'v')
    tm.sleep(0.65)
    py.press('enter')
    tm.sleep(0.65)
    py.press('esc', presses=2)
    tm.sleep(0.25)
    py.press('esc', presses=2)
    
    py.hotkey('alt', 'tab')
    py.press('right')
    py.write("feito")
    py.press('down')
    py.press('left',presses=2)

    return None

def atualizacao_valor():

    py.keyDown('ctrl')
    py.keyDown('ctrl')
    py.keyDown('c')
    py.keyUp('c')
    py.keyUp('ctrl')

    py.hotkey('alt', 'tab')
    
    py.PAUSE = 0.70
    py.press('pageup', presses=2)

    """Consulta"""
    py.click (x= -477, y = 547, duration=0.25)
    py.moveTo (x= -507, y =611, duration=0.25)
    py.click(clicks=2)
    py.hotkey('ctrl', 'v')
    tm.sleep(3)

    py.click (x=-217, y=612, duration=0.25)
    py.press('esc')
    py.moveTo(x=-333, y=620)
    py.click(clicks=1)

    py.hotkey('alt', 'tab')

    py.press('right', presses=3)
    py.hotkey('ctrl', 'v')

    py.press('left', presses=3)
    py.press('down')

    return None

    
def main(y):
    
    py.alert('Começar programa')
    n = 0 
    
    
    py.displayMousePosition()

    while n < y:
        """placaBD()"""
        """atualizacao_valor()"""

        n+=1
    return py.alert("fim da execução")
        

main(1)