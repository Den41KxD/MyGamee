

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager


from screens import MenuScreen, SettingsScreen

MAIN_WINDOW_KV="""

#:import Factory kivy.factory.Factory

<MyPopup@Popup>:
    id: AboutPopup
    auto_dismiss: False
    title: 'About' 
    BoxLayout:
        orientation: "vertical"

        TextInput:
            multiline: True
            text:
                'Alternately swap the cubes until the sum of all horizontal and vertical ones is the same.\\nFor help, the required amount is indicated on the button at the bottom right.\\n\
                When the amount is the same everywhere, click on the button at the bottom right, see your result and proceed to the next level\\n\
                complaints and suggestions: denyshrachov96@gmail.com'
            disabled: True 
        Button:
            size_hint: 1, 0.2
            text:'Close'
            on_press: AboutPopup.dismiss()
    

<MenuScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: 'Start'
            on_press: root.manager.current = 'settings'
        Button:
            text: 'About'
            on_release: Factory.MyPopup().open()
        Button:
            text: 'Quit'
            on_press: app.stop()

<SettingsScreen>:
    BoxLayout:
        orientation: "vertical"


        Button:
            text: 'return to game'
            on_state:
                if 'game' in root.manager.screen_names:\
                    root.manager.current='game'
                    
        Button:
            text: 'Back'
            on_press: root.manager.current='menu'

        Label:
            text: 'Settings:'
            center_x: 0.5
            center_y: 0.5
        Label:
            text: 'choose difficulty:'
            center_x: 0.5
            center_y: 0.5

        Slider:
            id: slider
            min: 2
            max: 15
            step: 1
            value_track: True

        Label:
            text: str(slider.value)

        Button:
            text: 'Go Play'
            on_press: root.printMe()
            # on_press: root.manager.current='game'
"""

Builder.load_string(MAIN_WINDOW_KV)


class ExampleApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm


if __name__ == '__main__':
    ExampleApp().run()

