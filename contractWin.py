# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contractWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 360)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 360))
        MainWindow.setMaximumSize(QtCore.QSize(400, 360))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 61, 16))
        self.label.setObjectName("label")
        self.contractCodeLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.contractCodeLineEdit.setGeometry(QtCore.QRect(110, 20, 131, 20))
        self.contractCodeLineEdit.setObjectName("contractCodeLineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 20, 51, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 55, 54, 12))
        self.label_2.setObjectName("label_2")
        self.kLineTypeComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.kLineTypeComboBox.setGeometry(QtCore.QRect(110, 50, 121, 22))
        self.kLineTypeComboBox.setObjectName("kLineTypeComboBox")
        self.kLineTypeComboBox.addItem("")
        self.kLineTypeComboBox.addItem("")
        self.kLineTypeComboBox.addItem("")
        self.kLineTypeComboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 54, 12))
        self.label_3.setObjectName("label_3")
        self.kLinePeriodComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.kLinePeriodComboBox.setGeometry(QtCore.QRect(110, 83, 111, 22))
        self.kLinePeriodComboBox.setObjectName("kLinePeriodComboBox")
        self.kLinePeriodComboBox.addItem("")
        self.kLinePeriodComboBox.addItem("")
        self.kLinePeriodComboBox.addItem("")
        self.kLinePeriodComboBox.addItem("")
        self.kLinePeriodComboBox.addItem("")
        self.kLinePeriodComboBox.addItem("")
        self.kLinePeriodComboBox.addItem("")
        self.kLinePeriodComboBox.addItem("")
        self.kLinePeriodComboBox.addItem("")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 120, 351, 131))
        self.groupBox.setObjectName("groupBox")
        self.AllkLineRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.AllkLineRadioButton.setGeometry(QtCore.QRect(30, 20, 89, 16))
        self.AllkLineRadioButton.setObjectName("AllkLineRadioButton")
        self.startDateRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.startDateRadioButton.setGeometry(QtCore.QRect(30, 46, 89, 16))
        self.startDateRadioButton.setObjectName("startDateRadioButton")
        self.startDateLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.startDateLineEdit.setGeometry(QtCore.QRect(110, 44, 71, 20))
        self.startDateLineEdit.setObjectName("startDateLineEdit")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(190, 47, 91, 16))
        self.label_4.setObjectName("label_4")
        self.qtyRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.qtyRadioButton.setGeometry(QtCore.QRect(30, 72, 89, 16))
        self.qtyRadioButton.setObjectName("qtyRadioButton")
        self.qtylineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.qtylineEdit.setGeometry(QtCore.QRect(110, 71, 51, 20))
        self.qtylineEdit.setObjectName("qtylineEdit")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(170, 75, 54, 12))
        self.label_5.setObjectName("label_5")
        self.historyRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.historyRadioButton.setGeometry(QtCore.QRect(30, 96, 111, 16))
        self.historyRadioButton.setObjectName("historyRadioButton")
        self.confirm = QtWidgets.QPushButton(self.centralwidget)
        self.confirm.setGeometry(QtCore.QRect(260, 270, 50, 25))
        self.confirm.setObjectName("confirm")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(330, 270, 50, 25))
        self.cancel.setObjectName("cancel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.kLineTypeComboBox.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "商品属性"))
        self.label.setText(_translate("MainWindow", "商品代码："))
        self.pushButton.setText(_translate("MainWindow", "选择"))
        self.label_2.setText(_translate("MainWindow", "K线类型："))
        self.kLineTypeComboBox.setItemText(0, _translate("MainWindow", "分笔"))
        self.kLineTypeComboBox.setItemText(1, _translate("MainWindow", "秒"))
        self.kLineTypeComboBox.setItemText(2, _translate("MainWindow", "分钟"))
        self.kLineTypeComboBox.setItemText(3, _translate("MainWindow", "日线"))
        self.label_3.setText(_translate("MainWindow", "K线周期："))
        self.kLinePeriodComboBox.setItemText(0, _translate("MainWindow", "1"))
        self.kLinePeriodComboBox.setItemText(1, _translate("MainWindow", "2"))
        self.kLinePeriodComboBox.setItemText(2, _translate("MainWindow", "3"))
        self.kLinePeriodComboBox.setItemText(3, _translate("MainWindow", "5"))
        self.kLinePeriodComboBox.setItemText(4, _translate("MainWindow", "10"))
        self.kLinePeriodComboBox.setItemText(5, _translate("MainWindow", "15"))
        self.kLinePeriodComboBox.setItemText(6, _translate("MainWindow", "30"))
        self.kLinePeriodComboBox.setItemText(7, _translate("MainWindow", "60"))
        self.kLinePeriodComboBox.setItemText(8, _translate("MainWindow", "120"))
        self.groupBox.setTitle(_translate("MainWindow", "运算起始点"))
        self.AllkLineRadioButton.setText(_translate("MainWindow", "所有K线"))
        self.startDateRadioButton.setText(_translate("MainWindow", "起始日期"))
        self.label_4.setText(_translate("MainWindow", "格式(YYYYMMDD)"))
        self.qtyRadioButton.setText(_translate("MainWindow", "固定根数"))
        self.label_5.setText(_translate("MainWindow", "根"))
        self.historyRadioButton.setText(_translate("MainWindow", "不执行历史K线"))
        self.confirm.setText(_translate("MainWindow", "确认"))
        self.cancel.setText(_translate("MainWindow", "取消"))