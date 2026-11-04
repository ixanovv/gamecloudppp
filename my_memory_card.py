from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup
from random import *
kdkfdfkdfksdjfnofoe = 0
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.move(900,70)
main_win.resize(400, 200)
buttom = QPushButton('Ответить')
question = QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox('Варианты ответов')
num1 = QRadioButton('Энцы')
num2 = QRadioButton('Чулымцы')
num3 = QRadioButton('Смурфы')
num4 = QRadioButton('Алеуты')
RadioGroup = QButtonGroup()
RadioGroup.addButton(num1)
RadioGroup.addButton(num2)
RadioGroup.addButton(num3)
RadioGroup.addButton(num4)
answers = [num1, num2, num3, num4]
main_win.score = 0
main_win.total = 0

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3



AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('Верно!') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('AGBDXJENJRNVRMFS') # здесь будет написан текст правильного ответа

layout_res = QVBoxLayout()

layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft| Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)



layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(num1)
layout_ans2.addWidget(num2)
layout_ans3.addWidget(num3)
layout_ans3.addWidget(num4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(question,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
#scretch

questions_list = []
q1 = Question(
    'Наибольше население имеет страна ', 'Индия' , 'Китай', 'Россия', 'Дубай'
)
q2 = Question(
    'Python - это', 'Язык программирования' , 'Удав', 'Впн', 'Змея'
)
q3 = Question(
    'Что такое число p', 'Константа' , 'Переменная', 'Абцисса', 'Координата'
)
q4 = Question(
    'Какого цвета яблоко', 'Зеленое' , 'Фиолетовое', 'Оранжевое', 'Черное'
)
questions_list.append(q1)
questions_list.append(q2)
questions_list.append(q3)
questions_list.append(q4)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    buttom.setText('Следующий вопрос')

main_win.current_num = -1

def next_question():
    main_win.current_num += 1
    main_win.total += 1
    f = main_win.score / main_win.total * 100
    print('Статистика')
    print('Всего вопросов:', main_win.total)
    print('Правильных ответов:', main_win.score)
    print('Рейтинг:',int(f),'%')
    kur = randint(1, len(questions_list) - 1)
        
    q = questions_list[kur]
    ask(q)

def click_ok():
    if buttom.text() == 'Ответить':
        check_answer()
    else:
        next_question()

# чтобы сбросить выбор радиокнопок, временно отключается эксклюзивность (setExclusive(False)), иначе одна кнопка всегда останется нажатой. После сброса эксклюзивность включается обратно.
def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    buttom.setText('Ответить')
    RadioGroup.setExclusive(False)
    num1.setChecked(False)
    num2.setChecked(False)
    num3.setChecked(False)
    num4.setChecked(False)
    RadioGroup.setExclusive(True)

def ask(q: question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def check_answer():
    ### если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')

def show_correct(res):
    lb_Result.setText(res)
    show_result()

buttom.clicked.connect(click_ok)
q = Question('Государственный язык Бразилии', 'Португальский', 'Итальянский', 'Прусский', 'Прусский')
ask(q)

layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
#stretch
layout_line2.addStretch(1)
layout_line3.addWidget(buttom, stretch=2)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addStretch(1)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
AnsGroupBox.hide()
main_win.setLayout(layout_card)


main_win.show()
app.exec_()
