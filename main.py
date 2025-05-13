from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt6.QtCore import Qt, QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resumee Analyzer")
        self.setFixedSize(QSize(500, 500))

        widget = QLabel("Drag the resumee here")
        font = widget.font()
        font.setPointSize(15)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        widget.setContentsMargins(0, 20, 0, 0)

        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = QWidget()
window = MainWindow()
window.show()
app.exec()