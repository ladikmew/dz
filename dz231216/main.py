import requests
import sqlite3 as sql
from datetime import date
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton
import sys

with sql.connect('data.db') as db:
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS news(new VARCHAR, datetime VARCHAR)''')


class Get_News_From_Site():
    def Getting_News(self, url):
        all_news = []
        req = requests.get(url)
        src = BeautifulSoup(req.text, "html.parser")
        # print(src)
        for i in src.findAll('a', attrs={"class": "list-item__title color-font-hover-only"}):
            all_news.append(i.string)
            #   all_news.append('\n')
        return all_news

    def Getting_Time(self, url):
        all_time = []
        req = requests.get(url)
        src = BeautifulSoup(req.text, "html.parser")
        for i in src.findAll('div', attrs={"class": "list-item__date"}):
            all_time.append(i.string + " " + str(date.today()))
        return all_time


class Creating_Database(Get_News_From_Site):
    def Base(self):
        t = Get_News_From_Site()
        self.new = t.Getting_News("https://ria.ru/world/")
        self.time = t.Getting_Time("https://ria.ru/world/")
        for i in range(len(self.new)):
            # print(self.new[i], self.time[i])
            cursor.execute(f'INSERT INTO news VALUES(?,?)', (self.new[i], self.time[i],))
            db.commit()

            cursor.execute('SELECT * FROM news')
            res = cursor.fetchall()
        return res

class App(QWidget,Creating_Database):
    def __init__(self):
        super(App, self).__init__()
        self.database = Creating_Database()
        self.items = self.database.Base()
    def setup_Ui(self):
        print(self.items)

        self.setWindowTitle("QTextEdit")
        self.resize(500, 600)

        self.textEdit = QTextEdit()
        self.btnPress1 = QPushButton("Get News")

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        self.setLayout(layout)

        self.btnPress1.clicked.connect(self.btnPress1_Clicked)

    def btnPress1_Clicked(self):
        self.textEdit.setPlainText('\n\n'.join(map(lambda x: f'{x[0]} {x[1]}', self.items)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    f = App()
    f.setup_Ui()
    f.show()
    sys.exit(app.exec_())

