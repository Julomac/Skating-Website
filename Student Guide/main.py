from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class HomePage(Screen):
    pass


class Building(Screen):
    pass


class ScreenManager(ScreenManager):
    pass


kv = Builder.load_file("StudentGuide.kv")


class StudentGuideApp(App):
    def build(self):
        return kv


StudentGuideApp().run()

