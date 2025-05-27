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
        layout.setSpacing(5)

        #Welcome text
        gui_title = QLabel("Welcome to my resumee analyzer")
        font = gui_title.font()
        font.setPointSize(20)
        gui_title.setFont(font)
        gui_title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        gui_title.setContentsMargins(0, 25, 0, 0)
        layout.addWidget(gui_title)
        
        # drag & drop field for the resume
        label_title = QLabel("Drag the resume here")
        font = label_title.font()
        font.setPointSize(15)
        label_title.setFont(font)
        label_title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        label_title.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(label_title)

        sub_text = QLabel("Please paste in a job advertisement")
        font = sub_text.font()
        font.setPointSize(15)
        sub_text.setFont(font)
        sub_text.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(sub_text)

        #input field for job return job_advertismentadvertisment
        job_advertisment = QLineEdit(parent=self)
        job_advertisment.setStyleSheet("""
                                    QLineEdit {
                                       border: 2px solid white;
                                       padding: 15px;
                                       font-size: 20px;
                                       }
                                       """)
        job_advertisment.setFixedWidth(750)
        job_advertisment.setFixedHeight(50)
        job_advertisment.setPlaceholderText("Please paste in a job advertisment")
        self.job_advertisment = job_advertisment
        layout.addWidget(job_advertisment)

        #send button for api and calculation logic
        collect_data_btn = QPushButton(
            icon=QIcon("send_icon.svg"),
            text="Send to AI",
            parent=self
        )
        collect_data_btn.setFixedSize(150, 50)
        collect_data_btn.setIconSize(QSize(50, 50))
        collect_data_btn.setContentsMargins(0, 25, 0, 0)
        collect_data_btn.setCheckable(True)
        collect_data_btn.clicked.connect(self.collect_data)
        layout.addWidget(collect_data_btn)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    #Button Logic
    def get_job_data(self):
        job_advertisment = self.job_advertisment.text()
        print(f"The job is: {job_advertisment}")

    def collect_data(self):
        print("\n")
        job_advertisment_data = self.job_advertisment.text()
        resume = print("Working")

        try:
            if job_advertisment_data or resume is not None:
                print(f"Job data: {job_advertisment_data} Resume data: {resume} \n")
                print("Data is collected and will send to my ai")

            else:
                raise ValueError("Invalid data where found")
            
        except ValueError as e:
            print(e)
    
# Application setup and launch
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
