from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        # Создаем большую кнопку по центру экрана
        return Button(text="Привет! Мое первое приложение")

if __name__ == "__main__":
    MyApp().run()
