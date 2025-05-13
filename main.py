# Basic imports for the required PyQt6 libraries and system access
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt6.QtCore import Qt, QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configure main window
        self.setWindowTitle("Resume Analyzer")
        self.setFixedSize(QSize(500, 500))

        # Create a basic label with user instructions
        label = QLabel("Drag the resume here")
        font = label.font()
        font.setPointSize(15)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        label.setContentsMargins(0, 20, 0, 0)

        self.setCentralWidget(label)

# Application setup and launch
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
