# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gaokao.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(947, 724)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(30, 60, 641, 521))
        self.graphicsView.setObjectName("graphicsView")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(710, 170, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(710, 110, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.submitButton = QtWidgets.QPushButton(Dialog)
        self.submitButton.setGeometry(QtCore.QRect(710, 300, 131, 51))
        self.submitButton.setObjectName("submitButton")
        self.stu_name = QtWidgets.QLabel(Dialog)
        self.stu_name.setGeometry(QtCore.QRect(100, 630, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.stu_name.setFont(font)
        self.stu_name.setObjectName("stu_name")
        self.loading_label = QtWidgets.QLabel(Dialog)
        self.loading_label.setGeometry(QtCore.QRect(720, 410, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.loading_label.setFont(font)
        self.loading_label.setText("")
        self.loading_label.setObjectName("loading_label")

        self.retranslateUi(Dialog)
        self.submitButton.clicked.connect(Dialog.submit)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "输入得分"))
        self.submitButton.setText(_translate("Dialog", "提交"))
        self.stu_name.setText(_translate("Dialog", "TextLabel"))
