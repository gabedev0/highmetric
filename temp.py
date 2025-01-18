from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder


class MainScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class ThirdScreen(Screen):
    pass

class FourthScreen(Screen):
    pass

class FifthScreen(Screen):
    pass

class SixthScreen(Screen):
    pass

class SeventhScreen(Screen):
    pass

class EighthScreen(Screen):
    pass

class NinthScreen(Screen):
    pass

class TenthScreen(Screen):
    pass

class EleventhScreen(Screen):
    pass

    class TwelfthScreen(Screen):
        pass

class ThirteenthScreen(Screen):
    pass

class FourteenthScreen(Screen):
    pass

class HighMetricApp(MDApp):
    def build(self):
        return Builder.load_file("main.kv")

if __name__ == "__main__":
    HighMetricApp().run()