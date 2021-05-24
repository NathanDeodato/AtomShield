# LIBS
import PySimpleGUI as sg
from time import sleep

# START
def AtomShield():
    ## LAYOUT
    sg.theme("DarkPurple6")
    layout = [
        [sg.Text(" " * 29), sg.Text("-> ⚛ <-"), sg.Text(" " * 29)],
        
        [sg.Text("° Limpeza de memória ROM")],
        [sg.Text("° Limpeza de memória RAM")],
        [sg.Text("° Detecta arquivos maliciosos")],
        [sg.Text("° Remove malwares e ransowares")],
        [sg.Text("° Proteção ao navegar na internet")],
        
        [sg.Text(" " * 25), sg.Button("ACTIVE"), sg.Text(" " * 25)],

        [sg.Text(" " * 30), sg.Text("(c) NT")]
    ]
    return sg.Window("AtomShield", layout=layout)


window = AtomShield()

while True:
    event, values = window.Read()

    ## CLOSE WINDOW
    if event == sg.WIN_CLOSED:
        break

    ## START SHIELD
    if event == "ACTIVE":
        sg.popup("")

