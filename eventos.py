import PySimpleGUI as sg
from omieapi import Omie
from tools import remove_digito, remove_digito_to_float, validar_ncm
from pysimpleevent import EventSimpleGUI


def eventos(loop: EventSimpleGUI, app_omie: Omie):
    """ Função que carrega todos os eventos da página """

    @loop.event(['-IN-PAGINAS-', '-IN-REGISTROS-POR-PAGINA-', '-IN-NCM-'])
    def setar_registros_apenas_numeros(*args):
        event, values, window = args
        tabela_lista_produtos = window.find_element(event)
        tabela_lista_produtos.update(remove_digito(values[event]))

    @loop.event('-IN-VALOR-UNITARIO-')
    def setar_valor_unitario_apenas_numeros(*args):
        event, values, window = args
        campo_valor_unitario = window.find_element('-IN-VALOR-UNITARIO-')
        campo_valor_unitario.update(remove_digito_to_float(values['-IN-VALOR-UNITARIO-']))

    @loop.event('-ATUIALIZA-PRODUTOS-')
    def event_busca_produto(*args):
        event, values, window = args
        tabela_lista_produtos = window.find_element('-TABELA-LISTAR-PRODUTOS-')
        pagina = values['-IN-PAGINAS-']
        registros_por_pagina = values['-IN-REGISTROS-POR-PAGINA-']

        try:
            r = app_omie.listar_produtos_resumido(
                pagina=1 if pagina == '' else int(pagina),
                registros_por_pagina=1 if registros_por_pagina == '' else int(registros_por_pagina)
            )
            valores = [[y for y in x.values()] for x in r['produto_servico_resumido']]
            tabela_lista_produtos.update(values=valores)
        except Exception as erro:
            sg.popup_error(f'Erro ao atualizar! {erro}')

    @loop.event('-CARREGAR-FAMILIA-PRODUTO-')
    def event_carregar_familia(*args):
        event, values, window = args
        try:
            r = app_omie.pesquisar_familias(
                pagina=1,
                registros_por_pagina=1000
            )
            lista_familias = r['famCadastro']
            dict_familias = {familia['nomeFamilia']: int(familia['codigo']) for familia in lista_familias}

            input_familias = window.find_element('-IN-FAMILIA-')
            input_familias.update(values=[x for x in dict_familias.keys()])
            print(dict_familias, lista_familias)
            return dict_familias

        except Exception as erro:
            sg.popup_error(f'Erro ao buscar familia {erro}!')

    @loop.event('-INCLUIR-PRODUTO-')
    def event_inlcuir_produto(*args):
        event, values, window = args
        familias = event_carregar_familia('-CARREGAR-FAMILIA-PRODUTO-', values, window)
        try:
            r = app_omie.incluir_produto(
                codigo_produto_integracao=values['-IN-COD-PRODUTO-'],
                descricao=values['-IN-NOME-PRODUTO-'],
                codigo=values['-IN-COD-PRODUTO-'],
                ncm=values['-IN-NCM-'],
                unidade=values['-IN-UNIDADE-'],
                valor_unitario=values['-IN-VALOR-UNITARIO-'],
                codigo_familia=familias[values['-IN-FAMILIA-'][0]]
            )
            sg.popup_ok(f'Status da operção : {r}')
            r = app_omie.alterar_produto(

            )
        except Exception as erro:
            sg.popup_error(f'Erro na operação {erro}!')






