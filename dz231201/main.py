import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui
import datetime
import uuid

db = sqlite3.connect('database.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS homeworks(
	created_date TEXT,
	deadline TEXT,
	done INTEGER,
	description TEXT,
	short_description TEXT,
	subject TEXT,
	id TEXT
)''')

db.commit()

for i in cursor.execute('SELECT * FROM homeworks'):
    print(i)


class Ui_CreateTask(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(581, 580)
        MainWindow.setStyleSheet('background-color: #524b4b;')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setText('Создание задания')
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet('color: white;')
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName('label')

        self.deadline = QtWidgets.QLineEdit(self.centralwidget)
        self.deadline.setGeometry(QtCore.QRect(80, 270, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deadline.setFont(font)
        self.deadline.setText('')
        self.deadline.setPlaceholderText('deadline YYYY-MM-DD')
        self.deadline.setObjectName('deadline')

        self.description = QtWidgets.QLineEdit(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(80, 200, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.description.setFont(font)
        self.description.setPlaceholderText('description')
        self.description.setObjectName('description')

        self.subject = QtWidgets.QLineEdit(self.centralwidget)
        self.subject.setGeometry(QtCore.QRect(80, 130, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.subject.setFont(font)
        self.subject.setText('')
        self.subject.setPlaceholderText('subject')
        self.subject.setObjectName('subject')

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 350, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName('pushButton')
        self.pushButton.setText('submit')

        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


class Ui_ShowTasks(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(581, 580)
        MainWindow.setStyleSheet('background-color: #524b4b;')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.items = cursor.execute('SELECT * FROM homeworks')
        self.renderitems = []

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setText('Список заданий')
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet('color: white;')
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName('label')

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 350, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName('pushButton')
        self.pushButton.setText('Создать задание')

        for key, i in enumerate(self.items):
            print('aaa', key, i)
            self.renderitems.append(QtWidgets.QPushButton(self.centralwidget))
            self.renderitems[key].setGeometry(QtCore.QRect(20, 70 + key * 50, 540, 41))
            font = QtGui.QFont()
            font.setPointSize(26)
            self.renderitems[key].setFont(font)
            self.renderitems[key].setText(f'{key + 1}. {i[5]}, дедлайн: {i[1]}')
            self.renderitems[key].setLayoutDirection(QtCore.Qt.LeftToRight)
            self.renderitems[key].setStyleSheet('color: white;')
            self.renderitems[key].setObjectName(i[5])

            def handler():
                self.open_task(i[6])

            self.renderitems[key].pressed.connect(handler)

        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def open_task(self, id: str):
        self.task = ShowTask(id)
        self.task.show()
        self.hide()


class Ui_ShowTask(object):
    def setupUi(self, MainWindow, id):
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(581, 580)
        MainWindow.setStyleSheet('background-color: #524b4b;')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.task = cursor.execute(f'SELECT * FROM homeworks WHERE id="{id}";')

        for i in self.task:
            self.task = i

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setText(f'Задание по {i[5]}')
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet('color: white;')
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(i[6])

        self.created_date = QtWidgets.QLabel(self.centralwidget)
        self.created_date.setGeometry(QtCore.QRect(95, 60, 400, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.created_date.setFont(font)
        self.created_date.setText(f'Дата создания: {i[0]}')
        self.created_date.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.created_date.setStyleSheet('color: white;')
        self.created_date.setAlignment(QtCore.Qt.AlignCenter)
        self.created_date.setObjectName(i[0])

        self.deadline = QtWidgets.QLabel(self.centralwidget)
        self.deadline.setGeometry(QtCore.QRect(95, 100, 400, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.deadline.setFont(font)
        self.deadline.setText(f'Дедлайн: {i[1]}')
        self.deadline.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.deadline.setStyleSheet('color: white;')
        self.deadline.setAlignment(QtCore.Qt.AlignCenter)
        self.deadline.setObjectName(i[0])

        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


class CreateTask(QtWidgets.QMainWindow, Ui_CreateTask):
    def __init__(self):
        super(CreateTask, self).__init__()
        self.setupUi(self)
        self.pushButton.pressed.connect(self.create_homework)

    def open_show_tasks(self):
        self.show_task_screen = ShowTasks()
        self.show_task_screen.show()
        self.hide()

    def create_homework(self):
        created_date = datetime.datetime.now().date()
        subj = self.subject.text()
        desc = self.description.text()
        deadline = self.deadline.text()

        if len(subj) == 0 or len(desc) == 0 or len(deadline) == 0:
            return

        cursor.execute(
            f'INSERT INTO homeworks VALUES("{created_date}", "{deadline}", "0", "{desc}", "{desc[0:30]}", "{subj}", "{uuid.uuid4()}")')
        db.commit()
        self.open_show_tasks()


class ShowTasks(QtWidgets.QMainWindow, Ui_ShowTasks):
    def __init__(self):
        super(ShowTasks, self).__init__()
        self.setupUi(self)
        self.pushButton.pressed.connect(self.open_create_task)

    def open_create_task(self):
        self.create_task_screen = CreateTask()
        self.create_task_screen.show()
        self.hide()


class ShowTask(QtWidgets.QMainWindow, Ui_ShowTask):
    def __init__(self, id):
        super(ShowTask, self).__init__()
        self.setupUi(self, id)


App = QtWidgets.QApplication([])
window = ShowTasks()
window.show()
App.exec()