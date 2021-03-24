import sys, clipboard, requests
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, \
    QLineEdit, QTextEdit, QStatusBar
import webbrowser
from bs4 import BeautifulSoup
import html5lib


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.stat = True
        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('상품폴더명:'), 0, 0)
        grid.addWidget(QLabel('카테고리:'), 1, 0)
        grid.addWidget(QLabel('펜던트이름:'), 2, 0)
        grid.addWidget(QLabel('체인이름:'), 3, 0)
        grid.addWidget(QLabel('클래습이름:'), 4, 0)

        self.folder = QLineEdit()
        self.category = QLineEdit()
        self.pandent = QLineEdit()
        self.chain = QLineEdit()
        self.clasp = QLineEdit()
        grid.addWidget(self.folder, 0, 1)
        grid.addWidget(self.category, 1, 1)
        grid.addWidget(self.pandent, 2, 1)
        grid.addWidget(self.chain, 3, 1)
        grid.addWidget(self.clasp, 4, 1)

        self.btn1 = QPushButton('&복사', self)
        grid.addWidget(self.btn1, 4, 2)
        self.btn1.clicked.connect(self.buttonCopy)

        self.setWindowTitle("상품설명 html 생성기")
        self.move(300, 300)
        self.resize(400, 200)
        self.show()

    def buttonCopy(self):
        self.btn1.setText("복사")
        fname = self.folder.text()
        catename = self.category.text()
        pname = self.pandent.text()
        cname = self.chain.text()
        craspname = self.clasp.text()
        host = "http://modoodesigner.speedgabia.com/"
        html = "<div style=\"width: 1260px;\">"
        target = ["detail/story/" + catename + "/" + fname + "/comment.html",
                  "detail/story/" + catename + "/" + fname + "/product_info.html",
                  "detail/story/pandent_info.html",
                  "detail/pandent/" + pname + ".html",
                  "detail/story/chain_info.html",
                  "detail/chain/" + cname + ".html",
                  "deatil/clasp/" + craspname + ".html",
                  "detail/delivery/notice.html"
                  ]

        for h in target:
            html += self.gethtml(host + h)
        html += "</div>"
        clipboard.copy(html)

        filepath = "html_file.html"
        with open(filepath, 'w', encoding="euc-kr") as f:
            f.write(html)
            f.close()

        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        webbrowser.get(chrome_path).open_new(filepath)
        print(filepath)

    def gethtml(self, text):

        response = requests.get(text, allow_redirects=False)
        response.encoding = "euc-kr"

        if response.status_code != 200:
            self.btn1.setText("오류")
            self.stat = False
            return ""

        # print(text)
        return response.text


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
