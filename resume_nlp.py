import spacy
import en_core_web_trf
import de_dep_news_trf
import spacy_fastlang

#supported languages
nlp_en = en_core_web_trf.load()
nlp_de = de_dep_news_trf.load()

nlp_de.add_pipe("language_detector", last=True)
nlp_en.add_pipe("language_detector", last=True)

class collectDocument:
    def __init__(self, doc):
        self.doc = doc

    def language_detection(self):
        from api import getData
        try:
            detection = nlp_en(self.doc)
            document_language = detection._.language

            from api import languageDetection
            file_language = languageDetection(language=document_language)

            if document_language == 'de':
                print("The language from the file is German")
                self.doc = nlp_de(self.doc)
                return self.doc
            
            elif document_language == 'en':
                print("The document language is English")
                self.doc = nlp_en(self.doc)
                return self.doc
            
            elif not document_language:
                raise ValueError("No language is detectet try it again")
            
            else:
                raise ValueError("This language is not supported right now")
            
        except ValueError as e:
            print(f"There is a error in the language detection")
            print(e)
            return

class resumeAnalysis_de:
    def __init__(self):
        pass

class resumeAnalysis_en:
    def __init__(self):
        pass