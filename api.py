#api for performance reasons
#the api will collect the data from main.py
#and send it to the other codes
#so the performance is better

#Spacy imports
import spacy
import en_core_web_trf
import de_dep_news_trf
import spacy_fastlang

#GUI imports
from main import MainWindow

#NLP Code imports
from resume_nlp import collectDocument

#values from the gui

#collect the pdf and jobadvertisment from the gui
class getData:
    def __init__(self, res_text, job_adv):
        self.res_text = res_text
        self.job_adv = job_adv

#detect the language from the resume
class languageDetection:
    def __init__(self, language):
        self.resume_language = language
