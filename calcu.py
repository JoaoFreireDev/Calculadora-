import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora"
    page.bgcolor = "#AFAFAF"
    page.window.width = 350
    page.window.height = 400

    
    todos_valores = ""


    resultado_texto = ft.Text(
        value="0",
        size=28,
        color="black",
        text_align=ft.TextAlign.RIGHT
    )

    def entrar_valores(e):
        nonlocal todos_valores
        todos_valores += str(e.control.content.value)
        resultado_texto.value = todos_valores
        page.update()


    def limpar_tela(e):
        nonlocal todos_valores
        todos_valores = ""
        resultado_texto.value = todos_valores
        page.update()

    def calcular(e):
        nonlocal todos_valores
        try:
            resultado_texto.value = str(eval(todos_valores))
            todos_valores = resultado_texto.value
        except:
            resultado_texto.value = "Erro"
            todos_valores = ""
        page.update()


    tela = ft.Container(
        content=resultado_texto,
        bgcolor="#8F8F8F",
        padding=10,
        border_radius=10,
        height=70,
        alignment=ft.Alignment(1, 0)
    )

    # estilo dos numeros kk
    estilo_numeros = {
        "height": 60,
        "bgcolor": "#8F8F8F",
        "color": "white",
        "expand": 1,
    }

    estilo_operadores = {
        "height": 60,
        "bgcolor": "#817F7F",
        "color": "black",
        "expand": 1,
    }

    estilo_limpar = {
        "height": 60,
        "bgcolor": "#FF5E00",
        "color": "white",
        "expand": 1,
    }

    estilo_igual = {
        "height": 60,
        "bgcolor": "#00C510",
        "color": "white",
        "expand": 1,
    }

    grelha_de_botoes = [
        [
            ("C", estilo_limpar, limpar_tela), 
            ("%", estilo_operadores, entrar_valores), 
            ("/", estilo_operadores, entrar_valores), 
            ("*", estilo_operadores, entrar_valores)
         ],
        [
            ("7",  estilo_numeros, entrar_valores),
            ("8",  estilo_numeros, entrar_valores),
            ("9",  estilo_numeros, entrar_valores),
            ("-", estilo_operadores, entrar_valores)
        ],
        [
            ("4",  estilo_numeros, entrar_valores),
            ("5",  estilo_numeros, entrar_valores),
            ("6",  estilo_numeros, entrar_valores),
            ("+", estilo_operadores, entrar_valores)
        ],
        [
            ("1",  estilo_numeros, entrar_valores),
            ("2",  estilo_numeros, entrar_valores),
            ("3",  estilo_numeros, entrar_valores),
            ("=", estilo_igual, calcular),
        ],
       
        [
            ("0",  {**estilo_numeros, "expand": 2}, entrar_valores), 
            (".", estilo_numeros, entrar_valores), 
            ("⌫", estilo_limpar, lambda e: None)
         ],
    ]

    botoes = []

    for linha in grelha_de_botoes:
        linha_control = []

        for text, estilo, handler in linha:
            btn = ft.ElevatedButton(
                content=ft.Text(text),
                on_click=handler,
                **estilo,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),
                    padding=ft.Padding(0, 0)
                )
            )

            linha_control.append(btn)

        botoes.append(ft.Row(linha_control, spacing=5))

    page.add(
        ft.Column(
            [
                tela,
                ft.Column(botoes, spacing=5)
            ]
        )
    )

ft.app(target=main)