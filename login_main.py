from login import Ui_Dialog
from random import randint
from main import mainWindow
from PyQt5.Qt import *
import requests



class loginWindow(QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def submit(self):
        id = self.lineEdit.text()
        pwd = self.lineEdit_2.text()
        print(id,pwd)
        print("http://localhost:5000/login?id={}&pwd={}".format(id,pwd))
        res = requests.get("http://localhost:5000/login?id={}&pwd={}".format(id,pwd))
        print(res.text)

        if res.text == "ok":
            loginwindow.close()
            self.window = mainWindow()
            self.window.show()
            self.window.getImage()
            
        else:
            message_box = QMessageBox()  
            message_box.setWindowTitle("提示")  
            message_box.setText("账户或密码")  
            message_box.setIcon(QMessageBox.Information)  
            message_box.exec_()

        


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    loginwindow = loginWindow()
    loginwindow.show()
    sys.exit(app.exec_())
