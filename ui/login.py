from utils import playfair_cipher
from styles import BUTTON_STYLE_OUTLINED,TEXT_STYLE_PATH,TEXT_STYLE_LABEL
import flet

class Login(flet.Container):
    def __init__(self):
        super().__init__()
        self.primary_color = "blue"
        self.circle_color = "black"
        self.BORDER_STYLE = flet.Border.all(2,self.circle_color)
        self.dots = [
            flet.Container(width=20,height=20,border_radius=180,border=self.BORDER_STYLE,data=''),
            flet.Container(width=20,height=20,border_radius=180,border=self.BORDER_STYLE,data=''),
            flet.Container(width=20,height=20,border_radius=180,border=self.BORDER_STYLE,data=''),
            flet.Container(width=20,height=20,border_radius=180,border=self.BORDER_STYLE,data=''),
        ]
        self.content = flet.Container(
            flet.Column([
                flet.Container(
                    flet.Text(
                        'Foydalanish uchun parolni kiriting',color="#333333",
                        font_family='sans',size=18,weight='w700'
                    ),
                    alignment=flet.Alignment.CENTER,margin=flet.Margin.only(top=20,bottom=20)
                ),
                flet.Row(self.dots,alignment=flet.MainAxisAlignment.CENTER),
                flet.Container(
                    flet.Column([
                        flet.Row([
                            flet.Button(
                                '1',on_click=self.on_typing,
                                style=BUTTON_STYLE_OUTLINED,width=70,height=70,
                            ),
                            flet.Button(
                                '2',on_click=self.on_typing,
                                style=BUTTON_STYLE_OUTLINED,width=70,height=70,
                            ),
                            flet.Button(
                                '3',on_click=self.on_typing,
                                style=BUTTON_STYLE_OUTLINED,width=70,height=70,
                            ),
                        ],alignment=flet.MainAxisAlignment.CENTER,spacing=30),
                        flet.Row([
                            flet.Button(
                                '4',on_click=self.on_typing,
                                style=BUTTON_STYLE_OUTLINED,width=70,height=70,
                            ),
                            flet.Button(
                                '5',on_click=self.on_typing,
                                style=BUTTON_STYLE_OUTLINED,width=70,height=70,
                            ),
                            flet.Button(
                                '6',on_click=self.on_typing,
                                style=BUTTON_STYLE_OUTLINED,width=70,height=70,
                            ),
                        ],alignment=flet.MainAxisAlignment.CENTER,spacing=30),
                        flet.Row([
                            flet.Button(
                                '7',on_click=self.on_typing,
                                style=BUTTON_STYLE_OUTLINED,width=70,height=70,
                            ),
                            flet.Button(
                                '8',on_click=self.on_typing,
                                style=BUTTON_STYLE_OUTLINED,width=70,height=70,
                            ),
                            flet.Button(
                                '9',on_click=self.on_typing,
                                style=BUTTON_STYLE_OUTLINED,width=70,height=70,
                            ),
                        ],alignment=flet.MainAxisAlignment.CENTER,spacing=30),
                        flet.Row([
                            flet.Button(
                                '0',on_click=self.on_typing,
                                style=BUTTON_STYLE_OUTLINED,width=70,height=70,
                            ),
                        ],alignment=flet.MainAxisAlignment.CENTER,spacing=30)
                    ],spacing=30),
                    margin=flet.Margin.only(top=20,bottom=20)
                )
            ]),
            padding=flet.Padding.all(20),
            border_radius=12,bgcolor='#ffffff',
            shadow=flet.BoxShadow(1,6,flet.Colors.with_opacity(0.1,'black')),
        )
        self.width=400
    
    def on_typing(self, e):
        typed = str(e.control.content)
        empty_dot = next((d for d in self.dots if not d.data), None)
        if empty_dot:
            empty_dot.data = typed
            empty_dot.bgcolor = self.circle_color
            if all(d.data for d in self.dots):
                password=''
                for i in self.dots:
                    password+=i.data
                    i.data = ''
                    i.bgcolor = 'transparent'
                    i.update()
                
                if password == '1234':
                    e.page.back(e)
        self.update()