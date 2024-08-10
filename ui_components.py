from PyQt5.QtWidgets import QWidget, QLabel, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox, QGraphicsDropShadowEffect, QButtonGroup
from PyQt5.QtGui import QFont, QPalette, QColor, QLinearGradient, QBrush
from PyQt5.QtCore import Qt
from equation_generators import generate_linear_equation, generate_quadratic_equation, generate_system_of_linear_equations
from equation_solvers import solve_linear_equation, solve_quadratic_equation, solve_system_of_linear_equations

class MathSolverApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.correct_answer = None  # Инициализация переменной
        self.incorrect_attempts = 0  # Количество неправильных попыток

    def initUI(self):
        self.setWindowTitle('Math Solver')
        self.setGeometry(100, 100, 450, 400)

        # Установка фонового градиента
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 450, 400)
        gradient.setColorAt(0.0, QColor("#1e3c72"))
        gradient.setColorAt(1.0, QColor("#2a5298"))
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(palette)

        # Шрифт
        font = QFont("Arial", 12)

        # Создание эффекта полупрозрачного стекла
        glass_effect = QGraphicsDropShadowEffect(self)
        glass_effect.setBlurRadius(15)
        glass_effect.setXOffset(0)
        glass_effect.setYOffset(0)
        glass_effect.setColor(QColor(0, 0, 0, 150))

        # Заголовок
        self.title = QLabel('Выберите тип уравнения и уровень сложности', self)
        self.title.setFont(QFont("Arial", 18, QFont.Bold))
        self.title.setStyleSheet("color: white; background-color: rgba(255, 255, 255, 0.1); border-radius: 10px; padding: 10px;")
        self.title.setGraphicsEffect(glass_effect)
        self.title.setAlignment(Qt.AlignCenter)

        # Радиокнопки для выбора типа уравнения
        radio_btn_style = """
            QRadioButton::indicator {
                width: 16px;
                height: 16px;
            }
            QRadioButton::indicator:checked {
                background-color: black;
                border: 1px solid white;
                border-radius: 8px;
            }
            QRadioButton::indicator:unchecked {
                background-color: gray;
                border: 1px solid white;
                border-radius: 8px;
            }
        """
        
        self.linear_btn = QRadioButton('Линейное')
        self.linear_btn.setFont(font)
        self.linear_btn.setStyleSheet(f"color: black; {radio_btn_style}")

        self.quadratic_btn = QRadioButton('Квадратное')
        self.quadratic_btn.setFont(font)
        self.quadratic_btn.setStyleSheet(f"color: black; {radio_btn_style}")

        self.system_btn = QRadioButton('Система линейных')
        self.system_btn.setFont(font)
        self.system_btn.setStyleSheet(f"color: black; {radio_btn_style}")

        # Радиокнопки для выбора уровня сложности
        self.easy_btn = QRadioButton('Легкий')
        self.easy_btn.setFont(font)
        self.easy_btn.setChecked(True)
        self.easy_btn.setStyleSheet(f"color: black; {radio_btn_style}")

        self.medium_btn = QRadioButton('Средний')
        self.medium_btn.setFont(font)
        self.medium_btn.setStyleSheet(f"color: black; {radio_btn_style}")

        self.hard_btn = QRadioButton('Сложный')
        self.hard_btn.setFont(font)
        self.hard_btn.setStyleSheet(f"color: black; {radio_btn_style}")

        # Создаем группы радиокнопок для типов уравнений и уровня сложности
        self.type_group = QButtonGroup(self)
        self.type_group.addButton(self.linear_btn)
        self.type_group.addButton(self.quadratic_btn)
        self.type_group.addButton(self.system_btn)

        self.difficulty_group = QButtonGroup(self)
        self.difficulty_group.addButton(self.easy_btn)
        self.difficulty_group.addButton(self.medium_btn)
        self.difficulty_group.addButton(self.hard_btn)

        # Поле для отображения уравнения
        self.equation_label = QLabel('')
        self.equation_label.setFont(font)
        self.equation_label.setStyleSheet("color: white; background-color: rgba(255, 255, 255, 0.1); border-radius: 10px; padding: 10px;")
        self.equation_label.setGraphicsEffect(glass_effect)

        # Кнопка для генерации уравнения
        self.generate_btn = QPushButton('Сгенерировать уравнение', self)
        self.generate_btn.setFont(font)
        self.generate_btn.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.2);
                color: white;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.3);
            }
        """)
        self.generate_btn.setGraphicsEffect(glass_effect)
        self.generate_btn.clicked.connect(self.generate_equation)

        # Поле для ввода ответа пользователя
        self.answer_input = QLineEdit(self)
        self.answer_input.setFont(font)
        self.answer_input.setPlaceholderText("Введите ваш ответ здесь")
        self.answer_input.setStyleSheet("color: white; background-color: rgba(255, 255, 255, 0.1); border-radius: 10px; padding: 5px;")
        self.answer_input.setGraphicsEffect(glass_effect)

        # Кнопка для проверки ответа
        self.check_btn = QPushButton('Проверить', self)
        self.check_btn.setFont(font)
        self.check_btn.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.2);
                color: white;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.3);
            }
        """)
        self.check_btn.setGraphicsEffect(glass_effect)
        self.check_btn.clicked.connect(self.check_answer)

        # Метка для отображения результата
        self.result_label = QLabel('')
        self.result_label.setFont(font)
        self.result_label.setStyleSheet("color: white; background-color: rgba(255, 255, 255, 0.1); border-radius: 10px; padding: 10px;")
        self.result_label.setGraphicsEffect(glass_effect)
        self.result_label.setAlignment(Qt.AlignCenter)

        # Layouts
        vbox = QVBoxLayout()
        hbox_type = QHBoxLayout()
        hbox_difficulty = QHBoxLayout()

        hbox_type.addWidget(self.linear_btn)
        hbox_type.addWidget(self.quadratic_btn)
        hbox_type.addWidget(self.system_btn)

        hbox_difficulty.addWidget(self.easy_btn)
        hbox_difficulty.addWidget(self.medium_btn)
        hbox_difficulty.addWidget(self.hard_btn)

        vbox.addWidget(self.title)
        vbox.addLayout(hbox_type)
        vbox.addLayout(hbox_difficulty)
        vbox.addWidget(self.generate_btn)
        vbox.addWidget(self.equation_label)
        vbox.addWidget(self.answer_input)
        vbox.addWidget(self.check_btn)
        vbox.addWidget(self.result_label)

        self.setLayout(vbox)

    def generate_equation(self):
        self.incorrect_attempts = 0  # Сбросить количество попыток при генерации нового уравнения

        difficulty = self.get_difficulty()

        if self.linear_btn.isChecked():
            self.a, self.b = generate_linear_equation(difficulty)
            self.equation_label.setText(f'Уравнение: {self.a}x + {self.b} = 0')
            self.correct_answer = str(solve_linear_equation(self.a, self.b))

        elif self.quadratic_btn.isChecked():
            self.a, self.b, self.c = generate_quadratic_equation(difficulty)
            self.equation_label.setText(f'Уравнение: {self.a}x^2 + {self.b}x + {self.c} = 0')
            self.correct_answer = solve_quadratic_equation(self.a, self.b, self.c)

        elif self.system_btn.isChecked():
            self.A, self.B = generate_system_of_linear_equations(difficulty)
            self.equation_label.setText(f'Система уравнений:\n{self.A[0,0]}x + {self.A[0,1]}y = {self.B[0]}\n{self.A[1,0]}x + {self.A[1,1]}y = {self.B[1]}')
            self.correct_answer = solve_system_of_linear_equations(self.A, self.B)

            if self.correct_answer is None:
                self.equation_label.setText('Система не имеет единственного решения.')
                self.correct_answer = ""

    def get_difficulty(self):
        if self.easy_btn.isChecked():
            return 'easy'
        elif self.medium_btn.isChecked():
            return 'medium'
        elif self.hard_btn.isChecked():
            return 'hard'

    def check_answer(self):
        user_answer = self.answer_input.text().strip()

        # Попробуем привести оба ответа к float и сравнить их
        try:
            correct_answer_num = float(self.correct_answer)
            user_answer_num = float(user_answer)
            is_correct = abs(correct_answer_num - user_answer_num) < 1e-9  # Допустимая погрешность
        except ValueError:
            is_correct = user_answer == self.correct_answer

        if is_correct:
            self.result_label.setText('Правильно!')
            self.result_label.setStyleSheet("color: lightgreen; background-color: rgba(0, 255, 0, 0.1); border-radius: 10px; padding: 10px;")
            self.incorrect_attempts = 0  # Сброс количества попыток при правильном ответе
        else:
            self.incorrect_attempts += 1
            self.result_label.setText(f'Неправильно! Попыток: {self.incorrect_attempts}')
            self.result_label.setStyleSheet("color: red; background-color: rgba(255, 0, 0, 0.1); border-radius: 10px; padding: 10px;")
            
            if self.incorrect_attempts % 5 == 0:  # Каждая пятая попытка
                show_answer = QMessageBox.question(self, 'Показать ответ?', 
                                                   'Вы сделали 5 неправильных попыток. Хотите увидеть правильный ответ?', 
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                
                if show_answer == QMessageBox.Yes:
                    QMessageBox.information(self, 'Правильный ответ', f'Правильный ответ: {self.correct_answer}')
                    self.incorrect_attempts = 0  # Сбросить количество попыток
