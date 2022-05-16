import datetime
import random

from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider

MAIN_WINDOW_KV= """
<MenuScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: 'Start'
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Settings'
            on_press: root.manager.current = 'game'
        Button:
            text: 'Quit'
            on_press: app.stop() 
        
<SettingsScreen>:
    BoxLayout:
        orientation: "vertical"
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
            min: 3
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




class MyGameApp(BoxLayout):
    def __init__(self, size_of_gread):
        super(MyGameApp, self).__init__()
        self.size_of_gread= size_of_gread


    def build(self):
        self.main_layout = BoxLayout(orientation="vertical")
        self.flag1 = False
        self.flag2 = False
        self.button_one = False
        self.button_two = False
        self.info_layout = BoxLayout(orientation="horizontal",size=(800, 50), size_hint=(None, None))
        self.steps_label = Label(text=str(0))
        # self.timer =Clock.schedule_interval(self.set_time,1)
        self.info_layout.add_widget(Label(text='Steps: '))
        self.info_layout.add_widget(self.steps_label)
        self.info_layout.add_widget(Label(text='Time: '))
        # self.info_layout.add_widget(self.timer)

        self.main_layout.add_widget(self.info_layout)

        self.all_number_layout = BoxLayout(orientation="vertical")
        self.main_mass = self.get_matrix()

        row_count=0
        for row in self.main_mass:
            h_layout = BoxLayout()
            if row_count<self.size_of_gread:
                lable_count=0
                for label in row:
                    lable_count+=1
                    if lable_count<=self.size_of_gread:
                        button = Button(text=str(label),pos_hint={"center_x": 0.5, "center_y": 0.5})
                        button.bind(on_press=self.on_button_press)
                    else:
                        button = TextInput(text=str(label),pos_hint={"center_x": 0.5, "center_y": 0.5},disabled=True)

                    h_layout.add_widget(button)

            else:
                for label in row:
                    button = TextInput(text=str(label), pos_hint={"center_x": 0.5, "center_y": 0.5}, disabled=True)
                    h_layout.add_widget(button)
            self.all_number_layout.add_widget(h_layout)
            row_count+=1

        self.main_layout.add_widget(self.all_number_layout)
        return self.main_layout


    def on_button_press(self, button):

        if self.flag1 == False:
            self.flag1 = True
            self.button_one = button
            self.button_one.background_color=[0.216, 0.69, 0.22]
        else:
            self.flag2=True
            self.button_two = button
        if self.flag1 and self.flag2:
            self.steps_label.text = str(int(self.steps_label.text)+1)
            tmp_var = self.button_one.text
            self.button_one.text=self.button_two.text
            self.button_two.text = tmp_var
            self.flag2 = False
            self.flag1 = False
            self.button_one.background_color = [1, 1, 1]
            self.button_one.index = self.button_one.parent.children.index(self.button_one)
            self.button_two.index = self.button_two.parent.children.index(self.button_two)

            new_sum = 0
            new_sum2=0

            for i in range(1, self.size_of_gread + 1):
                new_sum += int(self.button_one.parent.children[i].text)
                new_sum2 += int(self.button_two.parent.children[i].text)
            self.button_one.parent.children[0].text = str(new_sum)
            self.button_two.parent.children[0].text = str(new_sum2)
            new_sum_3=0
            new_sum_4=0
            first_flag = False
            for i in self.all_number_layout.children:
                if first_flag == False:
                    first_flag = True
                else:
                    new_sum_3 += int(i.children[self.button_one.index].text)
                    new_sum_4 += int(i.children[self.button_two.index].text)
            self.all_number_layout.children[0].children[int(self.button_one.index)].text = str(new_sum_3)
            self.all_number_layout.children[0].children[int(self.button_two.index)].text = str(new_sum_4)


    def get_matrix(self):
        import copy

        generete_rand = self.size_of_gread * random.randint(self.size_of_gread, self.size_of_gread*random.randint(3,6))
        buttons = list()
        Icount = 0
        for i in range(self.size_of_gread):
            tmp_mas = list()
            random_arr = generete_rand
            count = 0
            if Icount == self.size_of_gread - 1:
                for j in range(self.size_of_gread):
                    column_sum = 0
                    for k in buttons:
                        column_sum += k[j]
                    tmp_mas.append(generete_rand - column_sum)

            else:
                for j in range(self.size_of_gread):
                    if self.size_of_gread - 1 == count:
                        tmp_mas.append(random_arr)
                    else:
                        f = random.randint(self.size_of_gread, self.size_of_gread*2)
                        random_arr -= f
                        tmp_mas.append(f)
                        count += 1

            Icount += 1
            buttons.append(tmp_mas)


        new_arr = list()
        for i in buttons:
            for j in i:
                new_arr.append(j)
        random_arr = new_arr[:]
        random.shuffle(random_arr)
        original_mass = copy.deepcopy(buttons)

        for i in range(self.size_of_gread):
            for j in range(self.size_of_gread):
                buttons[i][j]=random_arr.pop()

        print('original')
        for i in original_mass:
            print(i)
        print('shuf')
        for i in buttons:
            print(i)

        for row in buttons:
            row.append(sum(row))

        random_arr = list()
        for i in range(self.size_of_gread):
            mysum = 0
            for j in range(self.size_of_gread):
                mysum += buttons[j][i]
            random_arr.append(mysum)
        random_arr.append(generete_rand)
        buttons.append(random_arr)

        return buttons

class MenuScreen(Screen):
    pass

class GameScreen(Screen):
    def __init__(self,grid,**kwargs):
        super(GameScreen, self).__init__(**kwargs)
        layout = MyGameApp(grid).build()
        self.add_widget(layout)


class SettingsScreen(Screen):
    def printMe(self):
        self.parent.add_widget(GameScreen(grid=self.ids.slider.value,name='game'))
        self.parent.current='game'


class ExampleApp(App):

    def build(self):
        sm = ScreenManager()

        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm


if __name__ == '__main__':
    ExampleApp().run()

