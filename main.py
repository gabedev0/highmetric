from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.window import Window
from tela import *
from kivymd.uix.label import MDLabel
from kivymd.utils.set_bars_colors import set_bars_colors

Window.size = (360, 640)


class MenuScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='left')


class AnguloScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')


class AreaScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')


class ComprimentoScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')


class DensidadeScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')


class DigitalScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')


class EnergiaScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')


class ForcaScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')


class MoedaScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')


class PesoScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')


class PressaoScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')


class TemperaturaScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')


class TempoScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')


class VelocidadeScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')


class VolumeScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')


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

    def trocar_tema(self):
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.primary_palette = "Orange"
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.primary_palette = "Blue"
            self.theme_cls.theme_style = "Light"

    def atualizar_barras_de_cor(self):
        if self.theme_cls.theme_style == "Light":
            self.set_bars_colors(status_bar=(1, 1, 1, 1), navigation_bar=(0, 0, 0, 1))  # Branco e preto
        else:
            self.set_bars_colors(status_bar=(0, 0, 0, 1), navigation_bar=(1, 1, 1, 1))  # Preto e branco


if __name__ == "__main__":
    HighMetric().run()
