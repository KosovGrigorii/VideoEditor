import sys
from PyQt5.QtGui import QPalette, QColor, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar, QAction, QStatusBar, QCheckBox, QComboBox, \
    QLineEdit, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QPushButton, QTabWidget, QDialog, \
    QDialogButtonBox, QMessageBox, QFileDialog, QTextEdit, QFrame
from PyQt5.QtCore import Qt, QSize, QDir
from moviepy.editor import VideoFileClip

from TimeLine import QTimeLine


class MainWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(MainWidget, self).__init__(*args, **kwargs)
        main_layout = QVBoxLayout()
        layout = QHBoxLayout()
        layout1 = QVBoxLayout()
        layout2 = QGridLayout()

        for i in range(5):
            for j in range(6):
                emp = QLabel()
                emp.setStyleSheet("background-color:gray")
                layout2.addWidget(emp, j, i)

        butt = QPushButton('Import Video')
        min_line = 0
        min_col = 0
        butt.clicked.connect(lambda: self.import_vid(layout2,  min_line, min_col))
        layout1.addWidget(butt)
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
        layout.addLayout(layout3, 8)
        main_layout.addLayout(layout, 2)
        lay = QHBoxLayout()
        lay.addWidget(QTimeLine(1000, 100))
        main_layout.addLayout(lay, 1)
        self.setLayout(main_layout)

    def import_vid(self, layout, min_line, min_col):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Video File', "Video files (*.avi *.mp4 *.flv)")
        clip = VideoFileClip(file_name)
        frame = clip.get_frame(10)
        layout.addWidget(frame, min_line, min_col)
        if min_col == 4:
            min_line += 1
            min_col = 0


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Video Editor")
        w = 700
        h = 500
        self.resize(w, h)
        #self.setStyleSheet("background-color: #ffffff;")

        main_widget = MainWidget()

        self.setCentralWidget(main_widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
