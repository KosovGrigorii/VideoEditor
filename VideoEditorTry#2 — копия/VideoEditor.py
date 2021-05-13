import sys
from PyQt5.QtGui import QPalette, QColor, QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar, QAction, QStatusBar, QCheckBox, QComboBox, \
    QLineEdit, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QPushButton, QTabWidget, QDialog, \
    QDialogButtonBox, QMessageBox, QFileDialog, QTextEdit, QFrame, QStyle, QSizePolicy, QSlider, \
    QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt, QSize, QDir
from PyQt5.QtMultimediaWidgets import QVideoWidget
from moviepy.editor import VideoFileClip

from TimeLine import QTimeLine
from VideoItself import VideoWindow


class ListBoxWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def dropEvent(self, event):
        if event.mimeData().hasText():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            links = []
            links.append(event.mimeData().text())
            self.addItems(links)
        else:
            event.ignore()


class MainWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(MainWidget, self).__init__(*args, **kwargs)
        main_layout = QVBoxLayout()
        layout = QHBoxLayout()
        layout1 = QVBoxLayout()
        layout2 = QVBoxLayout()

        self.listbox_view = ListBoxWidget(self)
        self.buttl2 = QPushButton('Get Value', self)
        self.buttl2.setGeometry(850, 400, 200, 50)
        self.buttl2.clicked.connect(lambda: self.playSelectedItem())
        layout2.addWidget(self.listbox_view)
        layout2.addWidget(self.buttl2)

        self.butt = QPushButton('Import Video')
        self.butt.clicked.connect(lambda: self.import_vid())
        layout1.addWidget(self.butt)
        layout1.addWidget(QPushButton('Add Photo/Video'))
        layout1.addWidget(QPushButton('Cut'))
        layout1.addWidget(QPushButton('Rotate'))
        layout1.addWidget(QPushButton('Картинка в картинке?'))
        layout1.addWidget(QPushButton('Paste'))
        layout1.addWidget(QPushButton('Fade in/Fade out'))
        layout1.addWidget(QPushButton('Change size'))
        layout1.addWidget(QPushButton('Speed up/Slow down'))
        layout1.addStretch()
        layout.addLayout(layout1, 2)

        layout.addLayout(layout2, 8)
        layout3 = QVBoxLayout()
        self.VideoPlay = VideoWindow()
        layout3.addWidget(self.VideoPlay)
        layout.addLayout(layout3, 8)
        main_layout.addLayout(layout, 2)
        lay = QHBoxLayout()
        lay.addWidget(QTimeLine(1000, 100))
        main_layout.addLayout(lay, 1)
        self.setLayout(main_layout)

    def import_vid(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Video File', "Video files (*.avi *.mp4 *.flv)")

        if file_name != '':
            self.listbox_view.addItem(file_name)


    def playSelectedItem(self):
        item = QListWidgetItem(self.listbox_view.currentItem())
        self.VideoPlay.openFile(item.text())
        #return item.text()


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Video Editor")
        w = 700
        h = 500
        self.resize(w, h)

        main_widget = MainWidget()

        self.setCentralWidget(main_widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
