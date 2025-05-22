from pdf_reader import extracted_data
import spacy

# Settings for the PDF loader
# Please note: a PDF file named "resume.pdf" is required

class pdfLoader:
    def __init__(self, pdf_data=extracted_data):
        self.pdf_data = pdf_data
    
    def load_data(self):
        if self.pdf_data is not None:
            print("The data access was successful.\n")
        else:
            raise ValueError("The PDF path is empty")

# Basic setup for the languages in spaCy
# Note: Only German and English are supported
# Using spaCy's transformer models for more accurate analysis

class SpacySettings:
    def __init__(self):
        self.language_de = None
        self.language_en = None
    
    def set_spacy_languages(self):
        self.language_de = spacy.load("de_dep_news_trf")
        self.language_en = spacy.load("en_core_web_trf")

# Initialize PDF loading
pdf_loader = pdfLoader()
pdf_loader.load_data()

# Initialize spaCy models
spacy_setup = SpacySettings()
spacy_setup.set_spacy_languages()
