from gaokao import Ui_Dialog
from random import randint
import cv2
import requests
import json

from PyQt5.Qt import *


class mainWindow(QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setImage(self,img_path):
        frame = QImage(img_path)
        pix = QPixmap.fromImage(frame)
        item = QGraphicsPixmapItem(pix)
        scene = QGraphicsScene()
        scene.addItem(item)
        self.graphicsView.setScene(scene)
     

    #获取图片
    def getImage(self):
        text = requests.get("http://localhost:5000/blank").text
        if text == "改完了！！":
            self.loading_label.setText("改完了")
            return
        print(text)
        text = json.loads(text)
        id = text["id"]
        path = text["img_src"]
        self.setImage(path)
        self.stu_name.setText(id)
		
    #提交
    def submit(self):
        point = self.textEdit.toPlainText()
        id = self.stu_name.text() 
        requests.get("http://localhost:5000/sub_blank?id=" + str(id) + "&point=" + str(point))
        print(point)
        print(id)
        self.getImage()

    def init():
        self.getImage()
        self.show()
        



if __name__ == "__main__":
    
    import sys
    app = QApplication(sys.argv)

    window = mainWindow()
    window.getImage()
    window.show()
    sys.exit(app.exec_())
