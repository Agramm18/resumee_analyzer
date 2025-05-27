# Basic imports for the required PyQt6 libraries and system access
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon


import sys

class DragAndDropField(QLabel):
    def __init__(self):
        super().__init__()
        self.setText("Drag your pdf file here")
        self.setStyleSheet("border: 2px dashed #aaa; padding: 20px;")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setAcceptDrops(True)
        self.file_path = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():

            for url in event.mimeData().urls():
                if url.toLocalFile().lower().endswith('.pdf'):
                    event.acceptProposedAction()
                    return
        event.ignore()
    
    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            pdf_path = [url.toLocalFile() for url in event.mimeData().urls()
                         if url.toLocalFile().lower().endswith('.pdf')]

            if pdf_path:
                self.file_path = pdf_path
                self.setText("PDF File: \n" + "\n".join(pdf_path))
                print("Dropped pdf file", pdf_path)

            else:
                self.setText("Only pdf files are allowed")
    
    def collect_path(self):
        resume_path = self.file_path
        return resume_path

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

        #Drag and Drop field
        drag_drop_field = DragAndDropField()
        layout.addWidget(drag_drop_field)

        collect_pdf_btn = QPushButton(
            text="Collect PDF file",
            parent=self
        )
        collect_pdf_btn.setFixedSize(150, 50)
        collect_pdf_btn.setContentsMargins(0, 25, 0, 0)
        collect_pdf_btn.setCheckable(True)
        collect_pdf_btn.clicked.connect(self.collect_resume_path)
        
        layout.addWidget(collect_pdf_btn)

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

    #collect the pdf from drag & drop for pdfplumber
    def collect_resume_path():
        pass

    def get_job_data(self):
        job_advertisment = self.job_advertisment.text()
        print(f"The job is: {job_advertisment}")

    #data collection logic for api and ai
    def collect_data(self):
        print("\n")
        job_advertisment_data = self.job_advertisment.text()
        resume = print("")

        try:
            if job_advertisment_data or resume is not None:
                print(f"Job data: {job_advertisment_data} Resume data: {resume} \n")
                print("Code logic is working")
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
