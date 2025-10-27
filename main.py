from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import App

KV = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 0.05, 0.15, 0.25, 1
            Rectangle:
                pos: self.pos
                size: self.size
        BoxLayout:
            size_hint_y: 0.25
            padding: dp(20)
            spacing: dp(10)
            Image:
                source: 'assets/icon.png'
                size_hint: None, None
                size: dp(96), dp(96)
            Label:
                text: 'Soda Pani'
                color: 1,1,1,1
                font_size: '32sp'
                halign: 'left'
                valign: 'middle'
        BoxLayout:
            orientation: 'vertical'
            padding: dp(20)
            spacing: dp(12)
            Button:
                text: 'Inventory'
                size_hint_y: None
                height: dp(56)
                on_release: app.show_placeholder('Inventory')
            Button:
                text: 'Sales'
                size_hint_y: None
                height: dp(56)
                on_release: app.show_placeholder('Sales')
            Button:
                text: 'Reports'
                size_hint_y: None
                height: dp(56)
                on_release: app.show_placeholder('Reports')
            Widget:
                size_hint_y: None
                height: dp(20)
            Label:
                id: status
                text: 'Ready'
                color: 0.8,0.9,1,1
                size_hint_y: None
                height: dp(24)
'''

class SodaPaniApp(App):
    def build(self):
        Window.clearcolor = (0.05, 0.15, 0.25, 1)
        self.root = Builder.load_string(KV)
        return self.root

    def show_placeholder(self, name):
        self.root.ids.status.text = f'{name} (placeholder) - feature coming soon'

if __name__ == '__main__':
    SodaPaniApp().run()
