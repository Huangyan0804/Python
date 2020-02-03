import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.initWindow()

    def initWindow(self):
        # 设置窗口的位置和大小
        self.resize(800, 600)
        self.center()
        # 设置窗口的标题
        self.setWindowTitle('Icon')
        # 设置窗口的图标,使用当前目录下的图片
        self.setWindowIcon(QIcon('web.png'))
        # show
        self.show()

    def initUI(self):
        # 这种静态的方法设置一个用于显示工具提示的字体。我们使用10px滑体字体。
        QToolTip.setFont(QFont('SansSerif', 10))

        # 创建一个提示，我们称之为setToolTip()方法。我们可以使用丰富的文本格式
        # self.setToolTip('This is a <b>QWidget</b> widget')

        # 创建一个PushButton
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QWidget</b> widget')
        # btn.sizeHint()显示默认尺寸
        btn.resize(btn.sizeHint())
        btn.move(100, 100)
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(lambda: QCoreApplication.instance().quit())
        qbtn.resize(50, 50)
        qbtn.move(300, 300)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'message',
                "Are you sure to quit?", QMessageBox.Yes |
                QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        

if __name__ == '__main__':
    # 每一PyQt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
