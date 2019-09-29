# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWinSignalSlot02.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(652, 311)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 60, 401, 121))
        self.groupBox.setObjectName("groupBox")
        self.numberSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.numberSpinBox.setGeometry(QtCore.QRect(90, 30, 42, 22))
        self.numberSpinBox.setObjectName("numberSpinBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(22, 35, 54, 12))
        self.label.setObjectName("label")
        self.styleCombo = QtWidgets.QComboBox(self.groupBox)
        self.styleCombo.setGeometry(QtCore.QRect(140, 30, 69, 22))
        self.styleCombo.setObjectName("styleCombo")
        self.styleCombo.addItem("")
        self.styleCombo.addItem("")
        self.styleCombo.addItem("")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(220, 35, 54, 12))
        self.label_2.setObjectName("label_2")
        self.printButton = QtWidgets.QPushButton(self.groupBox)
        self.printButton.setGeometry(QtCore.QRect(280, 30, 75, 23))
        self.printButton.setObjectName("printButton")
        self.previewStatus = QtWidgets.QCheckBox(self.groupBox)
        self.previewStatus.setGeometry(QtCore.QRect(50, 70, 71, 16))
        self.previewStatus.setObjectName("previewStatus")
        self.previewButton = QtWidgets.QPushButton(self.groupBox)
        self.previewButton.setGeometry(QtCore.QRect(130, 65, 75, 23))
        self.previewButton.setObjectName("previewButton")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(440, 60, 171, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.resultLabel = QtWidgets.QLabel(self.groupBox_2)
        self.resultLabel.setGeometry(QtCore.QRect(20, 20, 131, 81))
        self.resultLabel.setText("")
        self.resultLabel.setObjectName("resultLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "打印控件"))
        self.groupBox.setTitle(_translate("Form", "打印控制"))
        self.label.setText(_translate("Form", "打印份数："))
        self.styleCombo.setItemText(0, _translate("Form", "A3"))
        self.styleCombo.setItemText(1, _translate("Form", "A4"))
        self.styleCombo.setItemText(2, _translate("Form", "A5"))
        self.label_2.setText(_translate("Form", "纸张类型："))
        self.printButton.setText(_translate("Form", "打印"))
        self.previewStatus.setText(_translate("Form", "全屏预览"))
        self.previewButton.setText(_translate("Form", "预览"))
        self.groupBox_2.setTitle(_translate("Form", "操作结果"))


import os
import shutil
import sys

from PyQt5.QtCore import Qt, QPoint, pyqtSignal
from PyQt5.QtWidgets import *


class MyMainWindow(QMainWindow, Ui_Form):
    helpSignal = pyqtSignal(str)
    printSignal = pyqtSignal(list)
    previewSignal = pyqtSignal([int, str], [str])

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.helpSignal.connect(self.showHelpMessage)
        self.printSignal.connect(self.printPaper)
        self.previewSignal[str].connect(self.previewPaper)
        self.previewSignal[int, str].connect(self.previewPaperWithArgs)
        self.printButton.clicked.connect(self.emitPrintSignal)
        self.previewButton.clicked.connect(self.emitPreviewSignal)

    def emitPreviewSignal(self):
        if self.previewStatus.isChecked():
            self.previewSignal[int, str].emit(1080, 'Full Screen')
        else:
            self.previewSignal[str].emit('Preview')

    def emitPrintSignal(self):
        plist = []
        plist.append(self.numberSpinBox.value())
        plist.append(self.styleCombo.currentText())
        self.printSignal.emit(plist)

    def printPaper(self, list):
        self.resultLabel.setText('打印：' + '份数：' + str(list[0]) + '纸张:' + str(list[1]))

    def previewPaperWithArgs(self, style, text):
        self.resultLabel.setText(str(style) + text)

    def previewPaper(self, text):
        self.resultLabel.setText(text)

    # 重载按键事件
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F1:
            self.helpSignal.emit('help message')

    def showHelpMessage(self, message):
        self.resultLabel.setText(message)
        self.statusBar().showMessage(message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())


