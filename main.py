
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import os

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        self.label = Label(text='Presiona el botón para escribir un archivo.')
        layout.add_widget(self.label)

        btn = Button(text='Escribir Archivo')
        btn.bind(on_press=self.write_file)
        layout.add_widget(btn)

        return layout

    def write_file(self, instance):
        try:
            path = '/storage/emulated/0/mi_archivo.txt'  # Ruta en almacenamiento externo
            with open(path, 'w') as f:
                f.write('¡Hola, mundo! Este es un archivo de prueba.')
            self.label.text = f'Archivo escrito en: {path}'
        except Exception as e:
            self.label.text = f'Error: {e}'

if __name__ == '__main__':
    MyApp().run()

