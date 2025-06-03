#api for performance reasons
#the api will collect the data from main.py
#and send it to the other codes
#so the performance is better

from main import MainWindow

final_data = MainWindow.collect_final_data


class dataCollector:
    def __init__(self, job_advertisment=final_data):
        self.job_advertisment = job_advertisment