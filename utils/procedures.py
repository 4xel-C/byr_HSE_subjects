import sys
from datetime import datetime
from dataclasses import dataclass
from openpyxl import load_workbook


# Data class to represent each procedure
@dataclass
class Procedure:
    number: str  # Number of the procedure, format: PROCXXX
    part: int  # Number of the part (If a long procedure is partionnated)
    title: str
    ignored: bool  # Check if the procedure has to be ignored.
    last_review: datetime = datetime.min


# Class to manage the procedures
class ProcedureManager:
    def __init__(self, path: str) -> None:
        self.path = path
        self.procedures_list_file = "procedure_list.xlsx"
        self.history_file = "discussions_history.xlsx"
        self.procedures = []  
        self.__load_procedures()
        self.__generate_history()


    def __load_procedures(self) -> None:
        """Load all the procedures details from a file as a Procedure object and store them in self.procedures"""

        procedures_path = self.path + self.procedures_list_file
        
        wb = load_workbook(procedures_path)
        sheet = wb.active

        for number, part, title, ignored in sheet.iter_rows(min_row=2, values_only=True):
            self.procedures.append(Procedure(number.strip(), part, title.strip(), ignored))
        return
    
    
    def __generate_history(self) -> None:
        """Load the history file and get the last reviewed date for each procedure"""
        
        history_path = self.path + self.history_file
        
        wb = load_workbook(history_path)
        sheet = wb.active

        for number, date in sheet.iter_rows(min_row=2, values_only=True):
            for proc in self.procedures:
                if number.strip() == proc.number:
                    proc.last_review = max(proc.last_review, date) 
        return


    def select_procedures(self, n=3) -> list[Procedure]:
        """Select n random procedures among the oldest review"""
        procedures = sorted(self.procedures, key = lambda x: x.last_review)

        # return the n first procedures
        return procedures[:n]

        