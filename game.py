import datetime
import random

from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


class MyGameApp(BoxLayout):
    def __init__(self, size_of_gread):
        super(MyGameApp, self).__init__()
        self.size_of_gread = size_of_gread

        self.main_layout = BoxLayout(orientation="vertical")
        self.start_time = datetime.datetime.now()
        self.flag1 = False
        self.flag2 = False
        self.button_one = False
        self.button_two = False
        self.new_game_flag = False
        self.info_layout = BoxLayout(orientation="horizontal", size=(800, 50), size_hint=(None, None))
        self.steps_label = Label(text=str(0))
        self.clock = Clock.schedule_interval(self.set_time, 1)
        self.back_button = Button(text='Back', on_press=self.back_button_dis)
        self.timer_label = Label(text='0')
        self.info_layout.add_widget(self.back_button)
        self.info_layout.add_widget(Label(text='Steps: '))
        self.info_layout.add_widget(self.steps_label)
        self.info_layout.add_widget(Label(text='Time: '))
        self.info_layout.add_widget(self.timer_label)
        self.main_layout.add_widget(self.info_layout)
        self.all_number_layout = BoxLayout(orientation="vertical")
        self.main_mass = self.get_matrix()


    def build(self):
        row_count = 0
        for row in self.main_mass:
            h_layout = BoxLayout()
            if row_count < self.size_of_gread:
                lable_count = 0
                for label in row:
                    lable_count += 1
                    if lable_count <= self.size_of_gread:
                        button = Button(text=str(label), pos_hint={"center_x": 0.5, "center_y": 0.5})
                        button.bind(on_press=self.on_button_press)
                    else:
                        button =TextInput(
                            text=str(label),
                            pos_hint={"center_x": 0.5, "center_y": 0.5},
                            halign = "center",
                            background_color =[1,0.8,0],
                            disabled=True
                        )
                    h_layout.add_widget(button)

            else:
                for i in range(self.size_of_gread):
                    label = row[i]
                    button =TextInput(
                            text=str(label),
                            pos_hint={"center_x": 0.5, "center_y": 0.5},
                            halign = "center",
                            background_color =[1,0.8,0],
                            disabled=True
                            )
                    h_layout.add_widget(button)
                self.end_game_button = Button(
                    text=str(self.generete_rand),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    on_press=self.check_end_game,
                    background_color=[0.07, 0.9, 0.9, 0.8])
                h_layout.add_widget(self.end_game_button)
            self.all_number_layout.add_widget(h_layout)
            row_count += 1

        self.main_layout.add_widget(self.all_number_layout)
        return self.main_layout

    def on_button_press(self, button):

        if not self.flag1:
            self.flag1 = True
            self.button_one = button
            self.button_one.background_color = [0.216, 0.69, 0.22]
        else:
            self.flag2 = True
            self.button_two = button
        if self.flag1 and self.flag2:
            self.steps_label.text = str(int(self.steps_label.text)+1)
            tmp_var = self.button_one.text
            self.button_one.text = self.button_two.text
            self.button_two.text = tmp_var
            self.flag2 = False
            self.flag1 = False
            self.button_one.background_color = [1, 1, 1]
            self.button_one.index = self.button_one.parent.children.index(self.button_one)
            self.button_two.index = self.button_two.parent.children.index(self.button_two)

            new_sum = 0
            new_sum2 = 0

            for i in range(1, self.size_of_gread + 1):
                new_sum += int(self.button_one.parent.children[i].text)
                new_sum2 += int(self.button_two.parent.children[i].text)
            self.button_one.parent.children[0].text = str(new_sum)
            self.button_two.parent.children[0].text = str(new_sum2)
            new_sum_3 = 0
            new_sum_4 = 0
            first_flag = False
            for i in self.all_number_layout.children:
                if not first_flag:
                    first_flag = True
                else:
                    new_sum_3 += int(i.children[self.button_one.index].text)
                    new_sum_4 += int(i.children[self.button_two.index].text)
            self.all_number_layout.children[0].children[int(self.button_one.index)].text = str(new_sum_3)
            self.all_number_layout.children[0].children[int(self.button_two.index)].text = str(new_sum_4)

    def set_time(self, *args):
        self.timer_label.text = str(datetime.datetime.now() - self.start_time)[0:7]

    def back_button_dis(self,button):
        self.main_layout.parent.manager.current = 'settings'

    def check_end_game(self, button):

        if not self.new_game_flag:
            flag = True
            for row in self.all_number_layout.children:
                if int(row.children[0].text) != self.generete_rand:
                    flag = False
            for button in self.all_number_layout.children[0].children:
                if int(button.text) != self.generete_rand:
                    flag = False
            if flag:
                self.clock.cancel()
                self.end_game_button.background_color = [0, 1, 0]
                self.end_game_button.text = ' Good\n Tap for New Game'
                self.new_game_flag = True

                popup = Popup(auto_dismiss=False, title='nice', size_hint=(0.7, 0.7))
                popup_content = BoxLayout(orientation="vertical")
                popup_label = Label(text=f'Good job, you result:\n'
                                            f'passed in {self.timer_label.text} minutes\n'
                                            f'completed in {self.steps_label.text} steps\n')
                popup_content.add_widget(popup_label)

                popup.add_widget(popup_content)
                popup_button = Button(text='Close',
                                      size_hint=(1, 0.2),
                                      on_press=popup.dismiss)
                popup_content.add_widget(popup_button)

                # bind the on_press event of the button to the dismiss function
                popup_content.bind(on_press=popup.dismiss)
                # open the popup
                popup.open()


            else:
                self.end_game_button.background_color = [1, 0, 0]
                self.new_game_flag = False
                popup = Popup(auto_dismiss=False,
                              title='',
                              size_hint=(0.7, 0.7))
                              # size=(400, 400))
                popup_content = BoxLayout(orientation="vertical")
                popup_label = Label(text=f'sum of numbers in all rows and columns\n '
                                            f'is not equal {self.generete_rand}',
                                    size=(400, 400))
                popup_content.add_widget(popup_label)

                popup.add_widget(popup_content)
                popup_button = Button(text='Close',
                                      size_hint=(1, 0.2),
                                      on_press=popup.dismiss)
                popup_content.add_widget(popup_button)
                popup.open()
        else:
            screen_for_delete = self.main_layout.parent.manager.get_screen('game')

            self.main_layout.parent.manager.current = 'settings'
            self.main_layout.parent.manager.remove_widget(screen_for_delete)

    def get_matrix(self):
        import copy

        self.generete_rand = self.size_of_gread * random.randint(self.size_of_gread, self.size_of_gread*random.randint(3, 6))
        buttons = list()
        Icount = 0
        for i in range(self.size_of_gread):
            tmp_mas = list()
            random_arr = self.generete_rand
            count = 0
            if Icount == self.size_of_gread - 1:
                for j in range(self.size_of_gread):
                    column_sum = 0
                    for k in buttons:
                        column_sum += k[j]
                    tmp_mas.append(self.generete_rand - column_sum)

            else:
                for j in range(self.size_of_gread):
                    if self.size_of_gread - 1 == count:
                        tmp_mas.append(random_arr)
                    else:
                        f = int(self.generete_rand/self.size_of_gread +random.randint(-self.size_of_gread*2,self.size_of_gread*2))
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


        for i in range(self.size_of_gread):
            for j in range(self.size_of_gread):
                buttons[i][j] = random_arr.pop()
        # original_mass = copy.deepcopy(buttons)
        # print('original')
        # for i in original_mass:
        #     print(i)
        # print('shuffle')
        # for i in buttons:
        #     print(i)

        for row in buttons:
            row.append(sum(row))

        random_arr = list()
        for i in range(self.size_of_gread):
            mysum = 0
            for j in range(self.size_of_gread):
                mysum += buttons[j][i]
            random_arr.append(mysum)
        random_arr.append(self.generete_rand)
        buttons.append(random_arr)

        return buttons
