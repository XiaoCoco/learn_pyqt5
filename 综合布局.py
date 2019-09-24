# demo_13综合布局
import sys
from PyQt5.QtWidgets import QFormLayout, QGroupBox, QWidget, QTextEdit, QApplication, QLabel, QGridLayout, QPushButton, \
    QLineEdit, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.createGridGroupBox()
        self.createGridGroupBox2()
        self.createVbox()
        self.createFormBox()
        self.mainLayout = QVBoxLayout()  # 主布局为垂直布局
        self.mainLayout.setSpacing(20)  # 主布局添加补白

        self.topLayout = QHBoxLayout()  # 上方布局
        self.bottomLayout = QGridLayout()  # 下方布局

        self.topLayout.addWidget(self.gridGroupBox)  # top局添加一组box
        self.topLayout.addWidget(self.gridGroupBox2)  # top局添加一组box
        self.topLayout.addWidget(self.vbox)  # top布局添加另一组box
        self.bottomLayout.addWidget(self.forbox)

        self.mainLayout.addLayout(self.topLayout)  # 主布局添加top布局
        self.mainLayout.addLayout(self.bottomLayout)  # 也可以不创建上面下方布局，直接addWidget液效果相同

        self.setLayout(self.mainLayout)
        self.setWindowTitle('综合布局')
        self.show()

    def createGridGroupBox(self):
        self.gridGroupBox = QGroupBox('Grid Layout')

        self.gridLayout = QGridLayout()
        self.label_1 = QLabel('中文名称')
        self.linetext_1 = QLineEdit()
        self.label_2 = QLabel('发射地点')
        self.linetext_2 = QLineEdit()
        self.label_3 = QLabel('发射时间')
        self.linetext_3 = QLineEdit()

        self.iconLabel = QLabel()
        self.iconLabel.setPixmap(QPixmap("1.png"))

        self.gridLayout.addWidget(self.label_1, 2, 0)
        self.gridLayout.addWidget(self.linetext_1, 2, 1)
        self.gridLayout.addWidget(self.label_2, 3, 0)
        self.gridLayout.addWidget(self.linetext_2, 3, 1)
        self.gridLayout.addWidget(self.label_3, 4, 0)
        self.gridLayout.addWidget(self.linetext_3, 4, 1)
        self.gridLayout.addWidget(self.iconLabel, 0, 2, 4, 1)  # 行列下标，跨行，夸列

        self.gridGroupBox.setLayout(self.gridLayout)

    def createGridGroupBox2(self):
        self.gridGroupBox2 = QGroupBox('Grid Layout')

        self.gridLayout = QGridLayout()
        self.label_1 = QLabel('中文名称')
        self.linetext_1 = QLineEdit()
        self.label_2 = QLabel('发射地点')
        self.linetext_2 = QLineEdit()
        self.label_3 = QLabel('发射时间')
        self.linetext_3 = QLineEdit()

        self.iconLabel = QLabel()
        self.iconLabel.setPixmap(QPixmap("1.png"))

        self.gridLayout.addWidget(self.label_1, 2, 0)
        self.gridLayout.addWidget(self.linetext_1, 2, 1)
        self.gridLayout.addWidget(self.label_2, 3, 0)
        self.gridLayout.addWidget(self.linetext_2, 3, 1)
        self.gridLayout.addWidget(self.label_3, 4, 0)
        self.gridLayout.addWidget(self.linetext_3, 4, 1)
        self.gridLayout.addWidget(self.iconLabel, 0, 2, 4, 1)  # 行列下标，跨行，夸列

        self.gridGroupBox2.setLayout(self.gridLayout)

    def createVbox(self):
        self.vbox = QGroupBox('Vbox layout')
        self.vlayout = QVBoxLayout()
        self.vlabel_1 = QLabel('科研任务：')
        self.vtext_1 = QTextEdit()
        self.vtext_1.setText('搭载了空间冷原子钟等14项应用载荷，以及失重心血管研究等航天医学实验设备 "\
                "开展空间科学及技术试验')
        self.vlayout.addWidget(self.vlabel_1)
        self.vlayout.addWidget(self.vtext_1)
        self.vbox.setLayout(self.vlayout)

    def createFormBox(self):
        self.forbox = QGroupBox('Form box')
        self.bottomLayout = QFormLayout()
        self.bottom_label1 = QLabel('性能特点：')
        self.bottom_linetext = QLineEdit('"舱内设计更宜居方便天宫生活"')
        self.bottom_label2 = QLabel('发射规则：')
        self.bottom_editText = QTextEdit('2020年之前，中国计划初步完成空间站建设')
        self.bottomLayout.addRow(self.bottom_label1, self.bottom_linetext)
        self.bottomLayout.addRow(self.bottom_label2, self.bottom_editText)
        self.forbox.setLayout(self.bottomLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec())
