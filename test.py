
import os
import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *


# from PyQt5.QtGui import QIcon ,  QBrush , QColor
# from PyQt5.QtCore import Qt

strategy_path = r'C:\Users\xiaok\Desktop\purepython\strategy'


class TreeWidget(QWidget):
    def __init__(self,):
        super().__init__()
        self.setWindowTitle('极星量化')

        operatorLayout = QHBoxLayout()

        self.tree = QTreeWidget(self)
        # 设置列数
        self.tree.setColumnCount(1)
        # 设置头的标题
        self.tree.setHeaderLabels(['策略'])

        for d in os.listdir(strategy_path):
            root = QTreeWidgetItem(self.tree)
            root.setText(0, d)
            for file in os.listdir(os.path.join(strategy_path, d)):
                child = QTreeWidgetItem(root)
                child.setText(0, file)

        # self.tree.addTopLevelItem(root)
        # self.tree.clicked.connect(self.onTreeClicked)
        self.tree.doubleClicked.connect(self.onTreeClicked)

        mainLayout = QVBoxLayout(self)
        mainLayout.addLayout(operatorLayout)
        mainLayout.addWidget(self.tree)
        self.setLayout(mainLayout)

        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested[QtCore.QPoint].connect(self.rightMenuShow)  # 开放右键策略

    # 自定义右键菜单
    def rightMenuShow(self, point):
        self.popMenu = QMenu()
        self.addType = QMenu(self.popMenu)
        self.addType.setTitle('新建')
        rename = QAction('重命名', self)
        delete = QAction('删除', self)
        add_strategy = QAction('新建策略')
        add_group = QAction('新建分组')
        refresh = QAction('刷新', self)
        self.popMenu.addMenu(self.addType)
        self.addType.addAction(add_strategy)
        self.addType.addAction(add_group)
        self.popMenu.addAction(rename)
        self.popMenu.addAction(delete)
        self.popMenu.addAction(refresh)

        self.popMenu.exec_(self.mapToGlobal(point))

    # 节点点击事件
    def onTreeClicked(self, qmodelindex):
        item = self.tree.currentItem()
        print("key=%s ,value=%s" % (item.text(0), item.text(1)))

    # 添加节点
    def addTreeNodeBtn(self):
        print('--- addTreeNodeBtn ---')
        item = self.tree.currentItem()
        node = QTreeWidgetItem(item)
        node.setText(0, 'newNode')
        node.setText(1, '10')

    # 节点更新
    def updateTreeNodeBtn(self):
        print('--- updateTreeNodeBtn ---')
        item = self.tree.currentItem()
        item.setText(0, 'updateNode')
        item.setText(1, '20')

    # 删除节点
    def delTreeNodeBtn(self):
        print('--- delTreeNodeBtn ---')
        item = self.tree.currentItem()
        root = self.tree.invisibleRootItem()
        for item in self.tree.selectedItems():
            (item.parent() or root).removeChild(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = TreeWidget()
    tree.show()
    sys.exit(app.exec_())
