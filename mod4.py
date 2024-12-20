from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QMenu, QVBoxLayout, QHBoxLayout, QLineEdit


def clear_children(layout): #ЧОМУ ЦЕ НЕ ВБУДОВАНА ФУНКЦІЯ
    for i in reversed(range(layout.count())):
        if type(layout.itemAt(i)) == QHBoxLayout or type(layout.itemAt(i)) == QVBoxLayout:
            clear_children(layout.itemAt(i))
        else:
            layout.itemAt(i).widget().setParent(None)

class Module4Window(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout()
        self.setWindowTitle("Модуль 4")
        self.lbl = QLabel("Ільчук Іван КМ-42: Модуль 4")
        self.dropd_choice = QPushButton("Оберіть завдання")
        self.task_text = QLabel("")

        self.input_layout = QVBoxLayout()

        self.output_layout = QVBoxLayout()
        self.output_lbl = QLabel("")

        def task1():
            self.output_lbl.setText("")
            clear_children(self.input_layout)

            self.dropd_choice.setText("Завдання 1")
            self.task_text.setText("Умова: Мішень для стрільби являє собою концентричні кільця з центром на початку\n\
координат. радіус внутрішнього кільця {(десятки)} - 1см. Ширина всіх інших\n\
кілець - по 1см. Написати функцію, яка за координатами трьох точок попадання\n\
(х1, у1), (х2, у2) і (х3, у3) обчислює суму вибитих очок. Координати уводити.")
            sublay = QHBoxLayout()
            lbl_x1 = QLabel("x1:")
            edt_x1 = QLineEdit()
            lbl_y1 = QLabel("y1:")
            edt_y1 = QLineEdit()

            lbl_x2 = QLabel("x2:")
            edt_x2 = QLineEdit()
            lbl_y2 = QLabel("y2:")
            edt_y2 = QLineEdit()

            lbl_x3 = QLabel("x3:")
            edt_x3 = QLineEdit()
            lbl_y3 = QLabel("y3:")
            edt_y3 = QLineEdit()

            for i in [lbl_x1,edt_x1,lbl_y1,edt_y1,\
                      lbl_x2,edt_x2,lbl_y2,edt_y2,\
                      lbl_x3,edt_x3,lbl_y3,edt_y3]:
                sublay.addWidget(i)

            import sys

            def get_points(x,y,radius): #опис функції, яка повертає кількість очок за попадання в точку (x,y)
                points = 10
                circle_num = 1 #номер кола
                distance_squared = x**2 + y**2 #квадрат відстані точки (x,y) від центру мішені
                while distance_squared - (radius * circle_num) ** 2 > sys.float_info.epsilon and points > 0: #віднімає 1 очко за кожне коло, в яке
                    points -= 1                                                                     #точка (x,y) не влучила
                    circle_num += 1
                return points 

            def get_total_points(x1,y1,x2,y2,x3,y3,radius): #підраховує очки за 3 точки
                return get_points(x1,y1,radius) + get_points(x2,y2,radius) + get_points(x3,y3,radius)
            
            def btn_action():
                try:
                    points = get_total_points(float(edt_x1.text()),float(edt_y1.text()),\
                                            float(edt_x2.text()),float(edt_y2.text()),\
                                            float(edt_x3.text()),float(edt_y3.text()), 1 )
                except Exception as ex:
                    self.output_lbl.setText("Помилка при обробці координат точок")
                else:
                    self.output_lbl.setText(f"Результат: {points} очок")
            btn_calc = QPushButton("Обчислити")
            btn_calc.clicked.connect(btn_action)

            self.input_layout.addLayout(sublay)
            self.input_layout.addWidget(btn_calc)
            self.output_layout.addWidget(self.output_lbl)

        def task2():
            self.output_lbl.setText("")
            clear_children(self.input_layout)
            self.task_text.setText("Функція - Insert(s,s1,n).\n\
Призначення - вставка в рядок s підрядка s1,\n\
починаючи з позиції n.")

            def Insert(s,s1,n):
                out_string = s[:n] #додає до рядку 
                out_string = out_string + s1
                out_string = out_string + s[n:]
                return out_string # вставляє substring в in_string на позиції n

            self.dropd_choice.setText("Завдання 2")

            lbl_string = QLabel("Рядок:        ")
            edt_string = QLineEdit()
            lbl_substring = QLabel("Підрядок: ")
            edt_substring = QLineEdit()
            lbl_index = QLabel("Позиція:    ")
            edt_index = QLineEdit()

            sublay_string = QHBoxLayout()
            sublay_string.addWidget(lbl_string)
            sublay_string.addWidget(edt_string)

            sublay_substring = QHBoxLayout()
            sublay_substring.addWidget(lbl_substring)
            sublay_substring.addWidget(edt_substring)

            sublay_index = QHBoxLayout()
            sublay_index.addWidget(lbl_index)
            sublay_index.addWidget(edt_index)

            self.input_layout.addLayout(sublay_string)
            self.input_layout.addLayout(sublay_substring)
            self.input_layout.addLayout(sublay_index)

            calc_btn = QPushButton("Обчислити")
            def calc_btn_action():
                index = None
                try:
                    index = int(edt_index.text())
                except Exception:
                    self.output_lbl.setText("Недійсна позиція")
                else:
                    self.output_lbl.setText(f"Результуючий рядок: {Insert(edt_string.text(),edt_substring.text(),index)}")
            calc_btn.clicked.connect(calc_btn_action)
            self.input_layout.addWidget(calc_btn)
        
        self.output_layout.addWidget(self.output_lbl)

        taskmenu = QMenu()
        taskmenu.addAction("Завдання 1").triggered.connect(task1)
        taskmenu.addAction("Завдання 2").triggered.connect(task2)
        self.dropd_choice.setMenu(taskmenu)

        lay.addWidget(self.lbl)
        lay.addWidget(self.dropd_choice)
        lay.addWidget(self.task_text)
        lay.addLayout(self.input_layout)
        lay.addLayout(self.output_layout)
        lay.addStretch()
        self.setLayout(lay)
