import PySimpleGUI as sg

cabecalho = ['codigo', 'codigo_produto', 'codigo_produto_integracao', 'descricao', 'valor_unitario']

unidades = ['Kg', 'g', 'L', 'ml', 'm', 'cm', 'mm', 'in', 'ft', 'yd', 'UN']

lay_list_prod = [
    [sg.Frame('Buscar produtos', [
        [sg.Column(
            [
                [sg.Text(f'{"Página :":61}'),
                 sg.Push(),
                 sg.InputText(k='-IN-PAGINAS-', expand_x=True, enable_events=True)],

                [sg.Text(f'{"Registros por páginas :":50}'),
                 sg.Push(),
                 sg.InputText(k='-IN-REGISTROS-POR-PAGINA-', expand_x=True, enable_events=True)],

            ], size=(0, 75), expand_x=True
        ), sg.Column(
            [
                [sg.Push()]
            ],
        )],
        [sg.Button('Atualizar', expand_x=True, k='-ATUIALIZA-PRODUTOS-', pad=(10, 10) )]
    ]
, expand_x=True
)],
    # tabela produtos
    [sg.Table([], headings=cabecalho, k='-TABELA-LISTAR-PRODUTOS-', expand_x=True, expand_y=True)]
]

lay_alt_prod =[
    []
]

lay_inclui_prod = [
    [sg.Text( 'Codigo do Produto ' ), sg.InputText( k='-IN-COD-PRODUTO-', expand_x=True )],
    [sg.Text('Nome do Produto'), sg.InputText(k='-IN-NOME-PRODUTO-', expand_x=True)],
    [sg.Text('NCM'), sg.InputText(k='-IN-NCM-', expand_x=True, enable_events=True)],
    [sg.Text('Valor Unitário'), sg.InputText(k='-IN-VALOR-UNITARIO-', expand_x=True, enable_events=True)],
    [sg.Text('Unidade'), sg.Combo(unidades,  k='-IN-UNIDADE-')],

    [sg.Text('Família do Produto'),
     sg.Listbox([[]],  k='-IN-FAMILIA-', size=(100, 10), expand_x=True),
     sg.Button(' Carregar ', k='-CARREGAR-FAMILIA-PRODUTO-')],

    [sg.Button('Incluir', expand_x=True, k='-INCLUIR-PRODUTO-', pad=(10, 10))]
]

main_layout = [
    ##################################################################
    [sg.TabGroup(
        [
            [sg.Tab('Listar produtos', lay_list_prod)],
            [sg.Tab('Alterar produtos', lay_alt_prod)],
            [sg.Tab('Incluir produtos', lay_inclui_prod)]
        ], expand_x=True, expand_y=True
    )]
    ##################################################################
]

