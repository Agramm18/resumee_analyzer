#api for performance reasons
#the api will collect the data from main.py
#and send it to the other codes
#so the performance is better

from main import MainWindow

class getData:
    def __init__(self, res_text, job_adv):
        self.res_text = res_text
        self.job_adv = job_adv
    
    def store_pdf(self):
        if self.res_text:
            print(f"The extracted text from the resume is: {self.res_text} \n")
        
        else:
            raise ValueError("There is no resume")

    def store_job_adv(self):
        if self.job_adv:
            print(f"The job advertisment is: {self.job_adv}")

        else:
            raise ValueError("There is no job advertisment")
