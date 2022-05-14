import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput





class MainApp(App):
    def __init__(self, size_of_gread):
        super(MainApp, self).__init__()
        self.size_of_gread= size_of_gread


    def build(self):
        self.main_layout = BoxLayout(orientation="vertical")
        self.flag1 = False
        self.flag2 = False
        self.button_one = False
        self.button_two = False
        self.all_number_layout = BoxLayout(orientation="vertical")
        self.main_mass = self.get_matrix()

        # for i in range(n):
        #     tmp_mas=list()
        #     for j in range(n):
        #         tmp_mas.append(random.randint(1,9))
        #     tmp_mas.append(sum(tmp_mas))
        # self.main_mass = self.main_mass
        # collum_sum = list()
        # for i in range(n):
        #     mysum = 0
        #     for j in range(n):
        #         mysum += self.main_mass[j][i]
        #     collum_sum.append(mysum)
        # # collum_sum.append(0)
        # self.main_mass.append(collum_sum)

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

        generete_rand = self.size_of_gread * random.randint(4, 9)
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
                        f = random.randint(2, 9)
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

if __name__ == "__main__":
    app = MainApp(6)
    app.run()