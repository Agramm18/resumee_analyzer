# Basic imports for the required PyQt6 libraries and system access
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon

import sys

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Configure main window
        self.setWindowTitle("Resume Analyzer")
        self.setFixedSize(QSize(800, 800))

        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(15)

        #Welcome text
        gui_title = QLabel("Welcome to my resumee analyzer")
        font = gui_title.font()
        font.setPointSize(20)
        gui_title.setFont(font)
        gui_title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(gui_title)
        
        # drag & drop field for the resume
        label_title = QLabel("Drag the resume here")
        font = label_title.font()
        font.setPointSize(15)
        label_title.setFont(font)
        label_title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        label_title.setStyleSheet("""
                        QLabel {
                                  border: 2px solid white;
                                  border-radius: 25px;
                                  padding: 25px;

                                  }
                                  """)
        layout.addWidget(label_title)

        sub_text = QLabel("Please paste in a job advertisement")
        font = sub_text.font()
        font.setPointSize(15)
        sub_text.setFont(font)
        sub_text.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(sub_text)

        #input field for job advertisment
        job_advertisment = QLineEdit(parent=self)
        layout.addWidget(job_advertisment)

        send_job_btn = QPushButton(
            icon=QIcon("send_icon.svg"),
            text="Send to AI",
            parent=self
        )
        send_job_btn.setFixedSize(150, 50)
        send_job_btn.setIconSize(QSize(50, 50))
        layout.addWidget(send_job_btn)



        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

# Application setup and launch
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
