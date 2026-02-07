from utils import affin_cipher
from styles import BUTTON_STYLE_MENU,TEXT_STYLE_PATH,TEXT_STYLE_LABEL
import flet

class Affin(flet.Container):
    def __init__(self):
        super().__init__()
        self.field_alphabet = flet.TextField(
            hint_text='Alifbo',expand=True,hint_style=TEXT_STYLE_PATH,
            border_radius=8,bgcolor="#F5F4F7",border_color=flet.Colors.with_opacity(0.1,'black'),focused_border_width=1,
            text_style=flet.TextStyle(font_family='sans',size=18,color='black'),on_change=self.call_encrypt,
            value=affin_cipher.ALPHABET,cursor_color='#1E6EF4'
        )
        self.field_key_a = flet.TextField(
            hint_text='A kalit',width=100,hint_style=TEXT_STYLE_PATH,
            border_radius=8,bgcolor="#F5F4F7",border_color=flet.Colors.with_opacity(0.1,'black'),focused_border_width=1,
            text_style=flet.TextStyle(font_family='sans',size=18,color='black'),on_change=self.call_encrypt,
            value=7,cursor_color='#1E6EF4'
        )
        self.field_key_b = flet.TextField(
            hint_text='A kalit',width=100,hint_style=TEXT_STYLE_PATH,
            border_radius=8,bgcolor="#F5F4F7",border_color=flet.Colors.with_opacity(0.1,'black'),focused_border_width=1,
            text_style=flet.TextStyle(font_family='sans',size=18,color='black'),on_change=self.call_encrypt,
            value=9,cursor_color='#1E6EF4',keyboard_type=flet.KeyboardType.NUMBER
        )
        self.field_text = flet.TextField(
            hint_text='Shifrlanishi kerak bolgan matn',expand=True,hint_style=TEXT_STYLE_PATH,
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
        self.field_logs = flet.ListView(
            expand=True,
            auto_scroll=True
        )
        self.content = flet.Column([
            flet.Container(
                flet.Row([
                    flet.Button('ortga',icon=flet.Icons.ARROW_BACK_IOS,style=BUTTON_STYLE_MENU,on_click=lambda e: e.page.back(e)),
                    flet.Text('Simetrik shifrlash / Sezorning Affin Shifri',style=TEXT_STYLE_PATH,color='black'),
                    flet.Container(width=50)
                ],alignment=flet.MainAxisAlignment.SPACE_BETWEEN),shadow=flet.BoxShadow(1,6,flet.Colors.with_opacity(0.1,'black')),
                width=700,padding=flet.Padding.all(20),border_radius=12,bgcolor="#FFFFFF",
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
                    flet.Container(
                        self.field_logs,
                        height=200, # Set your fixed height here
                        bgcolor="#F5F4F7",
                        border_radius=10,padding=flet.Padding.only(left=20,right=5),
                        border=flet.Border.all(1, flet.Colors.with_opacity(0.1,'black')),
                    )
                ]),width=700,padding=flet.Padding.all(20),border_radius=12,bgcolor="#ffffff",
                shadow=flet.BoxShadow(1,6,flet.Colors.with_opacity(0.1,'black'))
            )
        ])
        self.width = 700
    
    def call_encrypt(self,e):
        a,b = str(self.field_key_a.value),str(self.field_key_b.value)
        if a.isdigit() and b.isdigit():
            self.field_cipher.value,logs = affin_cipher.encrypt(
                plain_text=self.field_text.value,
                key=(int(a),int(b)),
                alphabet=self.field_alphabet.value
            )
            self.field_logs.controls.clear()
            for i in logs.split('\n'):
                self.field_logs.controls.append(
                    flet.Text(i, size=14,font_family='consolas',color="black")
                )
        else:
            self.field_cipher.value = 'Kalit raqam bolishi kerak!'
        self.field_cipher.update()

    def call_decrypt(self,e):
        a,b = str(self.field_key_a.value),str(self.field_key_b.value)
        if a.isdigit() and b.isdigit():
            self.field_text.value,logs = affin_cipher.decrypt(
                cipher_text=self.field_cipher.value,
                key=(int(a),int(b)),
                alphabet=self.field_alphabet.value
            )
            self.field_logs.controls.clear()
            for i in logs.split('\n'):
                self.field_logs.controls.append(
                    flet.Text(i, size=14,font_family='consolas',color="black")
                )
        else:
            self.field_text.value = 'Kalit raqam bolishi kerak!'
        self.field_text.update()