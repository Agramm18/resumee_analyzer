import pdfplumber
from main import DragAndDropField

class pdfData:
    def __init__(self, file_path):
        self.path = file_path
        self.data = []
        self.pdf_text = None

    def read_pdf_file(self):
       if not self.path:
          raise ValueError("Please provide a pdf file")
       
       with pdfplumber.open(self.path) as pdf:
          text = ""
          
          for page in pdf.pages:
             page_text = page.extract_text()
             if page_text:
                text += page_text + "\n"

                self.pdf_text = text
       
    def get_pdf(self):
        if self.pdf_text is None:
            raise ValueError("No PDF text to extract data from.")

        self.data.append(self.pdf_text)
        return self.data

pdf_reader = pdfData()
pdf_reader.read_pdf_file(DragAndDropField.dragEnterEvent)
extracted_data = pdf_reader.get_pdf()
print(extracted_data)
