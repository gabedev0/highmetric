from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from tipos.temperatura import *
class Conversor(BoxLayout):
    entrada = StringProperty("")
    resultado = StringProperty("")

    def calcular(self, tipo):
        try:
            valor = float(self.entrada)
            if tipo == "c_para_f":
                self.resultado = f"{celsius_para_fahrenheit(valor):.2f} °F"
            elif tipo == "f_para_c":
                self.resultado = f"{fahrenheit_para_celsius(valor):.2f} °C"
            else:
                self.resultado = "Conversão não implementada"
        except ValueError:
            self.resultado = "Por favor, insira um número válido!"

class ConversorApp(App):
    def build(self):
        return Conversor()

if __name__ == "__main__":
    ConversorApp().run()
