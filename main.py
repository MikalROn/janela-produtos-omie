import PySimpleGUI as sg
from eventos import eventos
from pysimpleevent import EventSimpleGUI
from omieapi import Omie
from carregar_client import API_KEY, API_SECREET


# iniciando api

meu_app = Omie(API_KEY, API_SECREET)

# Carregando eventos

loop = EventSimpleGUI()
eventos(loop, meu_app)

# Configurações

sg.set_options(element_padding=(10, 10), scaling=4, font='comic-sans')
lista_temas = sg.theme_list()
sg.theme(lista_temas[0])

# importando layouts

from layouts import main_layout

# Rodar janela

win = sg.Window('Produtos', main_layout, resizable=True,)

if __name__ == '__main__':
    loop.run_window(win, window_log=True)



