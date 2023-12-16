import requests
import sqlite3 as sql
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication,QWidget,QTextEdit,QVBoxLayout,QPushButton
import sys



class Get_News_From_Site(object):
    def Getting_News(self, url):
        all_news = []
        req = requests.get(url)
        src = BeautifulSoup(req.text, "html.parser")
        #print(src)
        for i in src.findAll('a', attrs={"class": "list-item__title color-font-hover-only"}):
            all_news.append(i.string)
            #   all_news.append('\n')
        return all_news

    def Getting_Time(self, url):
        all_time = []
        req = requests.get(url)
        src = BeautifulSoup(req.text, "html.parser")
        for i in src.findAll('div', attrs={"class": "list-item__date"}):
            all_time.append(i.string+" 16.12.2023")
        return all_time


class Creating_Database(Get_News_From_Site):

    def Base(self):
        t = Get_News_From_Site()
        self.new = t.Getting_News("https://ria.ru/world/")
        self.time = t.Getting_Time("https://ria.ru/world/")
        with sql.connect('data1.db') as self.db:
            self.cursor = self.db.cursor()
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS news(new VARCHAR, datetime VARCHAR)''')
            for i in range(len(self.new)):
                print(self.new[i], self.time[i])
                self.cursor.execute(f'INSERT INTO news VALUES(?,?)',(self.new[i],self.time[i],) )
                self.db.commit()

            self.cursor.execute('SELECT * FROM news')
            res = self.cursor.fetchall()
        return res

    # def get_lable(self):
    #     return self.cursor.execute('SELECT * FROM news')

class Get_Data(Creating_Database):
    def __init__(self):
        h = Creating_Database()
        self.data = h.Base()
        for i in self.data:
            print(i)


class App(QWidget,Creating_Database):
    def stop(self, parent=None):
        #super().__init__(parent)
        o = Creating_Database()
        self.items = o.Base()


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
        for i in self.items:
            print("1")
            self.textEdit.setPlainText(f"{i}")


# c= Creating_database()
# print(c.Base())'
if __name__ == '__main__':
        app = QApplication(sys.argv)
        win = App()
        win.show()
        sys.exit(app.exec_())

