import sys, clipboard, requests
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QTextEdit
from bs4 import BeautifulSoup
import html5lib

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):


        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('상품폴더명:'), 0, 0)

        self.folder = QLineEdit()
        grid.addWidget(self.folder, 0, 1)

        btn1 = QPushButton('&복사', self)
        btn1.clicked.connect(self.buttonCopy)




        self.setWindowTitle("상품설명 html 생성기")
        self.move(300, 300)
        self.resize(400, 200)
        self.show()


    def buttonCopy(self):
        fname = self.folder.text()
        html = requests.get("http://modoodesigner.speedgabia.com/story/comment.html")
        # html = html5lib.parse(BeautifulSoup(tmp, 'html.parser'))
        html.encoding=None




        # requests.get()
        # print()
        clipboard.copy(html.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

