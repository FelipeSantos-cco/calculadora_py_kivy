from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):

    def build(self):
        self.operadores = ["/", "*", "+", "-"]
        self.ultimo_operador = None
        self.ultimo_botao = None

        main_layout = BoxLayout(orientation = "vertical")

        self.solucao = TextInput(multiline = False,
                                    readonly = True,
                                    halign = "right",
                                    font_size = 65
                                )
        main_layout.add_widget(self.solucao)
        
        botoes = [
            ["1","2","3","/"],
            ["4","5","6","*"],
            ["7","8","9","-"],
            [".","0","Limpar","+"]
        ]

        for linha in botoes:
            h_layout = BoxLayout()
            
            for label in linha:
                botao = Button(text = label,
                                pos_hint = {"center_x": 0.5, "center_y": 0.5},
                                )
                botao.bind(on_press=self.on_button_press)
                h_layout.add_widget(botao)

            main_layout.add_widget(h_layout)

        # Deixar o botão de igual em baixo de todos os outros 
        botao_igual = Button(text="=", pos_hint = {"center_x": 0.5, "center_y": 0.5}, background_color=(0,1,0,1))
        botao_igual.bind(on_press = self.on_solution)
        main_layout.add_widget(botao_igual)

        return main_layout
    

    def on_button_press(self, instance):
        atual = self.solucao.text
        botao_text = instance.text

        # Limpar a tela
        if botao_text == "Limpar":
            self.solucao.text = ""

        else:
            if atual and (self.ultimo_operador and botao_text in self.operadores):
                return
            
            elif atual == "" and botao_text in self.operadores: 
                return
            
            elif atual == "0":
                self.solucao.text = botao_text

            elif atual == "." and botao_text in self.operadores: 
                return
            
            else:
                novo_text = atual + botao_text
                self.solucao.text = novo_text
        
        self.ultimo_botao = botao_text
        self.ultimo_operador = self.ultimo_botao in self.operadores


    def on_solution(self, instance):
        text = self.solucao.text

        if text:
            solucao = str(eval(self.solucao.text))
            self.solucao.text = solucao

if __name__ == "__main__":
    app = MainApp()
    app.run()