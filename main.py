# Basic imports for the required PyQt6 libraries and system access
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
import pdfplumber
import sys

#drag and drop logic
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
        try:
            if event.mimeData().hasUrls():
                pdf_path = [url.toLocalFile() for url in event.mimeData().urls()
                            if url.toLocalFile().lower().endswith('.pdf')]

                if pdf_path:
                    self.file_path = pdf_path[0]
                    self.setText("PDF File: \n" + "\n".join(pdf_path))
                    
                else:
                    self.setText("Only pdf files are allowed")

        except (ValueError, TypeError) as e:
            print(f"There is a Error in data Collection: {e}")
    
    #Collect the file path for logic
    def collect_path(self):
        print(f"The file path from the drag enter event is: {self.file_path}")
        return self.file_path

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resume_text = None
        self.job_advertisment = None

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
        self.drag_drop_field = DragAndDropField()
        layout.addWidget(self.drag_drop_field)

        #PDF button to send the file to the converter
        collect_pdf_btn = QPushButton(
            text="Collect PDF file",
            parent=self
        )
        collect_pdf_btn.setFixedSize(150, 50)
        collect_pdf_btn.setContentsMargins(0, 25, 0, 0)
        collect_pdf_btn.setCheckable(True)
        collect_pdf_btn.clicked.connect(self.pdf_extractor)
        
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
            text="Save Job",
            parent=self
        )
        collect_data_btn.setFixedSize(150, 50)
        collect_data_btn.setIconSize(QSize(50, 50))
        collect_data_btn.setContentsMargins(0, 25, 0, 0)
        collect_data_btn.setCheckable(True)
        collect_data_btn.clicked.connect(self.get_job_data)
        layout.addWidget(collect_data_btn)
        
        #collect all final data
        save_data = QPushButton(
            text="Save resume and job-advertisment",
            parent=self
        )
        save_data.setFixedSize(150, 50)
        save_data.setIconSize(QSize(50, 50))
        save_data.setContentsMargins(0, 25, 0, 0)
        save_data.setCheckable(True)
        save_data.clicked.connect(self.final_output)
        layout.addWidget(save_data)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    #Button Logic

    #pdf extractor with pdfplumber
    def pdf_extractor(self):
        try:
            resume_path = self.drag_drop_field.collect_path()
            
            if not resume_path:
                raise ValueError("There must be an pdf document so we can continue")
            
            else:
                with pdfplumber.open(resume_path) as pdf:
                    resume_text = ''
                    for page in pdf.pages:
                        resume_text += page.extract_text() or ''

                    print("The pdf file is extracted now")
                    self.resume_text = resume_text

        except ValueError as e:
            print("There is an error in the pdf extraction")
            print(f"The error is: {e}")
            return

        
    #Jobadvertisment data
    def get_job_data(self):
        try:
            job_data = self.job_advertisment.text()
            
            if not job_data:
                raise ValueError("We neeed an jobadvertisment so we can continue")
            
            else:
                print(f"The job advertisment is: {job_data}")
                self.job_advertisment = job_data

        except ValueError as e:
            print("There is an invalid input in the job advertisment")
            print(f"The error is: {e}")
            return

    #data collector for api  
    def final_output(self):
        if self.job_advertisment and self.resume_text:
            print("Every value are saved")
            print("Code Logic is working")
            print("Scusess!! \n")

            #collect the data for the api
            from api import getData
            api_collector = getData(res_text=self.resume_text, job_adv=self.job_advertisment)
            api_collector.store_pdf()
            api_collector.store_job_adv()

        else:
            print("There is somewhere an error")

# Application setup and launch
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()