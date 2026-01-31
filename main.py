from ui.affin_cipher import Affin
from styles import TEXT_STYLE_TITLE,BUTTON_STYLE_MENU
import flet

def on_click(e:flet.TapEvent,content):
    e.page.controls = [content()]
    e.page.update()

def Menu():
    return flet.Container(
        flet.Row([
            flet.Container(
                flet.Column([
                    flet.Container(
                        flet.Text('Simmetrik shifrlash algoritmlari',style=TEXT_STYLE_TITLE),
                    ),
                    flet.Button('Sezarning affin shifri',style=BUTTON_STYLE_MENU,height=50,width=340,on_click=lambda e: on_click(e,Affin)),
                    flet.Button('Uinstonning ikkilangan kvadrati',style=BUTTON_STYLE_MENU,height=50,width=340),
                    flet.Button('Analitik usul',style=BUTTON_STYLE_MENU,height=50,width=340),
                ]),
                bgcolor="#D1D1D6",padding=20,border_radius=12
            ),
            flet.Container(
                flet.Column([
                    flet.Container(
                        flet.Text('Assimmetrik shifrlash algoritmlari',style=TEXT_STYLE_TITLE),
                    ),
                    flet.Button('Ryukzak',style=BUTTON_STYLE_MENU,height=50,width=340),
                    flet.Button('RSA',style=BUTTON_STYLE_MENU,height=50,width=340),
                    flet.Button('Rabin',style=BUTTON_STYLE_MENU,height=50,width=340),
                    flet.Button('EL-Gamal',style=BUTTON_STYLE_MENU,height=50,width=340),
                    flet.Button('Eyler funksiyasi',style=BUTTON_STYLE_MENU,height=50,width=340),
                ]),
                bgcolor="#D1D1D6",padding=20,border_radius=12
            )
        ],alignment=flet.MainAxisAlignment.CENTER,vertical_alignment=flet.CrossAxisAlignment.START),
    )

def main(page:flet.Page):
    def back_to_menu(e):
        on_click(e,Menu)
    page.window.resizable = False
    page.window.width = 900
    page.window.height = 500
    page.padding = 0
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.horizontal_alignment = flet.MainAxisAlignment.CENTER
    page.bgcolor = "#EEEEEE"
    page.fonts = {
        'sans':'DM-sans.ttf'
    }
    page.back = back_to_menu
    page.add(
        # Menu()
        Affin()
    )

flet.run(main,assets_dir='assets')