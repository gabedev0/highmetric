from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from tela import *
from kivymd.utils.set_bars_colors import set_bars_colors

Window.size = (360, 640)


class MenuScreen(Screen):
    pass


class AnguloScreen(Screen):
    pass


class AreaScreen(Screen):
    pass


class ComprimentoScreen(Screen):
    pass


class DensidadeScreen(Screen):
    pass


class DigitalScreen(Screen):
    pass


class EnergiaScreen(Screen):
    pass


class ForcaScreen(Screen):
    pass


class MoedaScreen(Screen):
    pass


class PesoScreen(Screen):
    pass


class PressaoScreen(Screen):
    pass


class TemperaturaScreen(Screen):
    pass


class TempoScreen(Screen):
    pass


class VelocidadeScreen(Screen):
    pass


class VolumeScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(AnguloScreen(name='angulo'))
sm.add_widget(AreaScreen(name='area'))
sm.add_widget(ComprimentoScreen(name='comprimento'))
sm.add_widget(DensidadeScreen(name='densidade'))
sm.add_widget(DigitalScreen(name='digital'))
sm.add_widget(EnergiaScreen(name='energia'))
sm.add_widget(ForcaScreen(name='forca'))
sm.add_widget(MoedaScreen(name='moeda'))
sm.add_widget(PesoScreen(name='peso'))
sm.add_widget(PressaoScreen(name='pressao'))
sm.add_widget(TemperaturaScreen(name='temperatura'))
sm.add_widget(TempoScreen(name='tempo'))
sm.add_widget(VelocidadeScreen(name='velocidade'))
sm.add_widget(VolumeScreen(name='volume'))


class HighMetric(MDApp):
    def build(self):
        screen = Builder.load_string(menu)
        return screen

    def toggle_theme(self):
        """Alterna entre o tema claro e escuro."""
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.primary_palette = "Orange"
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.primary_palette = "Blue"
            self.theme_cls.theme_style = "Light"


if __name__ == "__main__":
    HighMetric().run()
