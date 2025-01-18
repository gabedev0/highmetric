from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from tela import *

Window.size = (360, 640)


class MenuScreen(Screen):
    pass


class AnguloScreen(Screen):
    pass


class AreaScreen(Screen):
    pass


class ComprimentoScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(AnguloScreen(name='angulo'))
sm.add_widget(AreaScreen(name='area'))
sm.add_widget(ComprimentoScreen(name='comprimento'))


class HighMetric(MDApp):

    def build(self):
        screen = Builder.load_string(menu)
        return screen

    def toggle_theme(self):
        """Alterna entre o tema claro e escuro."""
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"  # Muda para o tema escuro
        else:
            self.theme_cls.theme_style = "Light"


if __name__ == "__main__":
    HighMetric().run()
