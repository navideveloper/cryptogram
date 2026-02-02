from utils import affin_cipher
from styles import BUTTON_STYLE_MENU,TEXT_STYLE_PATH,TEXT_STYLE_LABEL
import flet

class Affin(flet.Container):
    def __init__(self):
        super().__init__()
        self.field_alphabet = flet.TextField(
            hint_text='Alifbo',expand=True,hint_style=TEXT_STYLE_PATH,
            border_radius=8,bgcolor="#F1F1F1",border_color="#8f8f8f",focused_border_width=1,
            text_style=flet.TextStyle(font_family='sans',size=18,color='black'),on_change=self.call_encrypt,
            value=affin_cipher.ALPHABET,cursor_color='#1E6EF4'
        )
        self.field_key_a = flet.TextField(
            hint_text='A kalit',width=100,hint_style=TEXT_STYLE_PATH,
            border_radius=8,bgcolor="#F1F1F1",border_color="#8f8f8f",focused_border_width=1,
            text_style=flet.TextStyle(font_family='sans',size=18,color='black'),on_change=self.call_encrypt,
            value=7,cursor_color='#1E6EF4'
        )
        self.field_key_b = flet.TextField(
            hint_text='A kalit',width=100,hint_style=TEXT_STYLE_PATH,
            border_radius=8,bgcolor="#F1F1F1",border_color="#8f8f8f",focused_border_width=1,
            text_style=flet.TextStyle(font_family='sans',size=18,color='black'),on_change=self.call_encrypt,
            value=9,cursor_color='#1E6EF4',keyboard_type=flet.KeyboardType.NUMBER
        )
        self.field_text = flet.TextField(
            hint_text='Shifrlanishi kerak bolgan matn',expand=True,hint_style=TEXT_STYLE_PATH,
            border_radius=8,bgcolor="#F1F1F1",border_color="#8f8f8f",focused_border_width=1,
            text_style=flet.TextStyle(font_family='sans',size=18,color='black'),on_change=self.call_encrypt,
            cursor_color='#1E6EF4'
        )
        self.field_cipher = flet.TextField(
            hint_text='Shifrlangan matn',expand=True,hint_style=TEXT_STYLE_PATH,
            border_radius=8,bgcolor="#F1F1F1",border_color="#8f8f8f",focused_border_width=1,
            text_style=flet.TextStyle(font_family='sans',size=18,color='black'),on_change=self.call_decrypt,
            cursor_color='#1E6EF4'
        )
        self.content = flet.Column([
            flet.Container(
                flet.Row([
                    flet.Button('ortga',icon=flet.Icons.ARROW_BACK_IOS,style=BUTTON_STYLE_MENU,on_click=lambda e: e.page.back(e)),
                    flet.Text('Simetrik shifrlash / Sezorning Affin Shifri',style=TEXT_STYLE_PATH),
                    flet.Container()
                ],alignment=flet.MainAxisAlignment.SPACE_BETWEEN),width=700,padding=flet.Padding.all(20),border_radius=12,bgcolor='#D1D1D6'
            ),
            flet.Container(
                flet.Column([
                    flet.Row([
                        flet.Text('Alifbo',style=TEXT_STYLE_LABEL),
                        self.field_alphabet
                    ]),
                    flet.Row([
                        flet.Row([
                            flet.Text('Kalit A',style=TEXT_STYLE_LABEL),
                            self.field_key_a
                        ]),
                        flet.Row([
                            flet.Text('Kalit B',style=TEXT_STYLE_LABEL),
                            self.field_key_b
                        ]),
                    ],spacing=50),
                    flet.Row([
                        flet.Text('Oddiy Matn',style=TEXT_STYLE_LABEL),
                        self.field_text
                    ]),
                    flet.Row([
                        flet.Text('Shifrli Matn ',style=TEXT_STYLE_LABEL),
                        self.field_cipher
                    ]),
                    # flet.Row([
                    #     flet.Button('shifrlash',style=BUTTON_STYLE_MENU,height=40,width=300,on_click=self.call_encrypt),
                    #     flet.Button('shifrini ochish',style=BUTTON_STYLE_MENU,height=40,width=300,on_click=self.call_decrypt)
                    # ],alignment=flet.MainAxisAlignment.SPACE_EVENLY)
                ]),width=700,padding=flet.Padding.all(20),border_radius=12,bgcolor='#D1D1D6'
            )
        ])
        self.width = 700
    
    def call_encrypt(self,e):
        a,b = str(self.field_key_a.value),str(self.field_key_b.value)
        if a.isdigit() and b.isdigit():
            self.field_cipher.value = affin_cipher.encrypt(
                plain_text=self.field_text.value,
                key=(int(a),int(b)),
                alphabet=self.field_alphabet.value
            )
        else:
            self.field_cipher.value = 'Kalit raqam bolishi kerak!'
        self.field_cipher.update()

    def call_decrypt(self,e):
        a,b = str(self.field_key_a.value),str(self.field_key_b.value)
        if a.isdigit() and b.isdigit():
            self.field_text.value = affin_cipher.decrypt(
                cipher_text=self.field_cipher.value,
                key=(int(a),int(b)),
                alphabet=self.field_alphabet.value
            )
        else:
            self.field_text.value = 'Kalit raqam bolishi kerak!'
        self.field_text.update()