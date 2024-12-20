from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QMenu, QVBoxLayout, QHBoxLayout, QLineEdit

def clear_children(layout): #ЧОМУ ЦЕ НЕ ВБУДОВАНА ФУНКЦІЯ
    for i in reversed(range(layout.count())):
        if type(layout.itemAt(i)) == QHBoxLayout or type(layout.itemAt(i)) == QVBoxLayout:
            clear_children(layout.itemAt(i))
        else:
            layout.itemAt(i).widget().setParent(None)

class Module5Window(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout()
        self.setWindowTitle("Модуль 5")
        self.lbl = QLabel("Ільчук Іван КМ-42: Модуль 5")
        self.dropd_choice = QPushButton("Оберіть завдання")
        self.task_text = QLabel("")

        self.input_layout = QVBoxLayout()

        self.output_layout = QVBoxLayout()
        self.output_lbl = QLabel("")

        taskmenu = QMenu(self)
        def task1():
            self.dropd_choice.setText("Завдання 1")
            from random import randint
            self.task_text.setText("Визначити індекси елементів списку, значення яких належать заданому\n\
діапазону (тобто не менше заданого мінімуму і не більше заданого максимуму).\n\
Необхідно:\n\
    - заповнити список випадковими числами;\n\
    - запросити для введення мінімум і максимум діапазону;\n\
    - знайти індекси елементів, значення яких входять в діапазон. Додавати\n\
      знайдені індекси до нового списку;\n\
    - вивести загальне число знайдених індексів і окремо всі індекси;\n\
    - елементи списку, які знаходяться за певним індексом, видалити зі списку\n\
      занести у новий список.")
            self.output_lbl.setText("")
            clear_children(self.input_layout)
            list_lbl = QLabel()
            self.input_layout.addWidget(list_lbl)
            lst = []
            def generate_list():
                nonlocal lst
                lst = []
                for i in range(randint(10,20)):
                    lst.append(randint(-100,100))
                list_lbl.setText(f"Згенерований список: {lst}")
            generate_list()
            btn_gen_list = QPushButton("Згенерувати новий список")
            btn_gen_list.clicked.connect(generate_list)
            self.input_layout.addWidget(btn_gen_list)
            sublay = QHBoxLayout() #лаяут існує з метою красивого виведення інпуту діапазону (в 1 рядок)
            self.input_layout.addLayout(sublay)
            edt1 = QLineEdit()
            edt2 = QLineEdit()
            sublay.addWidget(QLabel("від"))
            sublay.addWidget(edt1)
            sublay.addWidget(QLabel("до"))
            sublay.addWidget(edt2)
            btn_calc = QPushButton("Обчислити")
            error_lbl = QLabel("Помилка при зчитуванні діапазону")
            error_lbl.hide()
            self.input_layout.addWidget(error_lbl)
            def btn_calc_action():
                try:
                    diap1 = float(edt1.text())
                    diap2 = float(edt2.text())
                except:
                    error_lbl.show()
                else:
                    error_lbl.hide()
                    index_list = []
                    for i in range(len(lst)):
                        if lst[i] >= diap1 and lst[i] <= diap2:
                            index_list.append(i)
                    ch = "ів" #частка коду яка відповідає за закінчення слова індекс
                    if len(index_list) == 1:
                        ch = ""
                    elif len(index_list) <= 4:
                        ch = "и"

                    in_diap = []
                    out_diap = []

                    for i in lst:
                        if i >= diap1 and i <= diap2:
                            in_diap.append(i)
                        else:
                            out_diap.append(i)
                    s = f"Знайдено {len(index_list)} індекс{ch}:\n{index_list}\n\nЧисла в діапазоні:\n{in_diap}\n\nЧисла поза діапазоном:\n{out_diap}"
                    self.output_lbl.setText(s)
            btn_calc.clicked.connect(btn_calc_action)
            self.input_layout.addWidget(btn_calc)
            self.output_layout.addWidget(self.output_lbl)

        def task2():
            self.dropd_choice.setText("Завдання 2")
            self.task_text.setText("Спираючись на визначення базових операцій на множинах, знайти\nA = {1,2,ee,ww,a,d}, B = {2,a,c,tt,4,3}, F = ((A ∩ B) ∪ (A \\ B))")
            self.output_lbl.setText("")
            clear_children(self.input_layout)
            btn = QPushButton("Обчислити")
            def btn_clicked():
                A = {1,2,"ee","ww","a","d"}
                B = {2,"a","c","tt",4,3}
                F = lambda A,B: (A&B)|(A-B) #функція для обчислення С
                C = F(A,B)
                self.output_lbl.setText(f"A = {A}\nB = {B}\nC = {C}")
            btn.clicked.connect(btn_clicked)
            self.input_layout.addWidget(btn)
            self.output_layout.addWidget(self.output_lbl)
            

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