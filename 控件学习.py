# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '控件学习.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(878, 594)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 230, 601, 301))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.treeView_3 = QtWidgets.QTreeView(self.horizontalLayoutWidget)
        self.treeView_3.setObjectName("treeView_3")
        self.horizontalLayout_2.addWidget(self.treeView_3)
        self.treeView = QtWidgets.QTreeView(self.horizontalLayoutWidget)
        self.treeView.setObjectName("treeView")
        self.horizontalLayout_2.addWidget(self.treeView)
        self.treeView_2 = QtWidgets.QTreeView(self.horizontalLayoutWidget)
        self.treeView_2.setObjectName("treeView_2")
        self.horizontalLayout_2.addWidget(self.treeView_2)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 1)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 30, 591, 194))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.treeView_6 = QtWidgets.QTreeView(self.gridLayoutWidget)
        self.treeView_6.setObjectName("treeView_6")
        self.gridLayout.addWidget(self.treeView_6, 0, 0, 1, 1)
        self.treeView_5 = QtWidgets.QTreeView(self.gridLayoutWidget)
        self.treeView_5.setObjectName("treeView_5")
        self.gridLayout.addWidget(self.treeView_5, 0, 1, 1, 1)
        self.treeView_4 = QtWidgets.QTreeView(self.gridLayoutWidget)
        self.treeView_4.setObjectName("treeView_4")
        self.gridLayout.addWidget(self.treeView_4, 0, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 878, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
