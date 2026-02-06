from utils import playfair_cipher
from styles import BUTTON_STYLE_MENU,TEXT_STYLE_PATH,TEXT_STYLE_LABEL
import flet

class Playfair(flet.Container):
    def __init__(self):
        super().__init__()
        self.field_keyword = flet.TextField(
            hint_text='Kalit So`z',expand=True,hint_style=TEXT_STYLE_PATH,
            border_radius=8,bgcolor="#F5F4F7",border_color=flet.Colors.with_opacity(0.1,'black'),focused_border_width=1,
            text_style=flet.TextStyle(font_family='sans',size=18,color='black'),on_change=self.call_matrix,
            cursor_color='#1E6EF4'
        )
        self.field_text = flet.TextField(
            hint_text='Shifrlanishi kerak bolgan xabar',expand=True,hint_style=TEXT_STYLE_PATH,
            border_radius=8,bgcolor="#F5F4F7",border_color=flet.Colors.with_opacity(0.1,'black'),focused_border_width=1,
            text_style=flet.TextStyle(font_family='sans',size=18,color='black'),on_change=self.call_encrypt,
            cursor_color='#1E6EF4'
        )
        self.field_cipher = flet.TextField(
            hint_text='Shifrlangan matn',expand=True,hint_style=TEXT_STYLE_PATH,
            border_radius=8,bgcolor="#F5F4F7",border_color=flet.Colors.with_opacity(0.1,'black'),focused_border_width=1,
            text_style=flet.TextStyle(font_family='sans',size=18,color='black'),on_change=self.call_decrypt,
            cursor_color='#1E6EF4'
        )
        self.square_matrix = flet.Column([],spacing=-1)
        self.content = flet.Column([
            flet.Container(
                flet.Row([
                    flet.Button('ortga',icon=flet.Icons.ARROW_BACK_IOS,style=BUTTON_STYLE_MENU,on_click=lambda e: e.page.back(e)),
                    flet.Text('Simetrik shifrlash / Uinstonning ikkilangan kvadrati',style=TEXT_STYLE_PATH),
                    flet.Container()
                ],alignment=flet.MainAxisAlignment.SPACE_BETWEEN),shadow=flet.BoxShadow(1,6,flet.Colors.with_opacity(0.1,'black')),
                width=700,padding=flet.Padding.all(20),border_radius=12,bgcolor='#ffffff'
            ),
            flet.Container(
                flet.Column([
                    flet.Row([
                        flet.Text('Kalit so`z',style=TEXT_STYLE_LABEL),
                        self.field_keyword
                    ]),
                    flet.Row([
                        flet.Text('Kvadrat',style=TEXT_STYLE_LABEL),
                        self.square_matrix,
                    ],spacing=50),
                    flet.Row([
                        flet.Text('Oddiy Matn',style=TEXT_STYLE_LABEL),
                        self.field_text
                    ]),
                    flet.Row([
                        flet.Text('Shifrli Matn',style=TEXT_STYLE_LABEL),
                        self.field_cipher
                    ]),
                    # flet.Row([
                    #     flet.Button('shifrlash',style=BUTTON_STYLE_MENU,height=40,width=300,on_click=self.call_encrypt),
                    #     flet.Button('shifrini ochish',style=BUTTON_STYLE_MENU,height=40,width=300,on_click=self.call_decrypt)
                    # ],alignment=flet.MainAxisAlignment.SPACE_EVENLY)
                ]),width=700,padding=flet.Padding.all(20),border_radius=12,bgcolor='#ffffff',shadow=flet.BoxShadow(1,6,flet.Colors.with_opacity(0.1,'black'))
            )
        ])
        self.width = 700
    
    def did_mount(self):
        self.call_matrix(None)
    
    def call_matrix(self,e):
        self.square_matrix.controls.clear()
        MATRIX = playfair_cipher.square(self.field_keyword.value)
        for row in MATRIX:
            ROW = flet.Row([],spacing=-1)
            for i in row:
                ROW.controls.append(
                    flet.Container(
                        flet.Text(i,size=18,color='#1E6EF4',font_family='sans'),
                        width=30,height=30,bgcolor='#F1F1F1',
                        alignment=flet.Alignment.CENTER,
                        border=flet.Border.all(1,flet.Colors.with_opacity(0.4,'black'))
                    )
                )
            self.square_matrix.controls.append(ROW)
        self.square_matrix.update()
        if e:
            self.call_encrypt(e)
    
    def call_encrypt(self,e):
        self.field_cipher.value = playfair_cipher.encrypt(
            plain_text=self.field_text.value,
            keyword=self.field_keyword.value
        )
        self.field_cipher.update()

    def call_decrypt(self,e):
        self.field_text.value = playfair_cipher.decrypt(
            cipher_text=self.field_cipher.value,
            keyword=self.field_keyword.value
        )
        self.field_text.update()