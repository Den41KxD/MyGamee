from kivy.uix.screenmanager import Screen

from game import MyGameApp

class MenuScreen(Screen):
    pass

class GameScreen(Screen):
    def __init__(self,grid,**kwargs):
        super(GameScreen, self).__init__(**kwargs)
        layout = MyGameApp(grid).build()
        self.add_widget(layout)


class SettingsScreen(Screen):
    def printMe(self):
        if 'game' in self.parent.screen_names:
            screen_for_delete = self.parent.get_screen('game')
            self.parent.remove_widget(screen_for_delete)
        self.parent.add_widget(GameScreen(grid=self.ids.slider.value,name='game'))
        self.parent.current = 'game'

