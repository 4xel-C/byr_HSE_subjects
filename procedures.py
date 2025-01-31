import sys
from dataclasses import dataclass
from openpyxl import load_workbook

# Data class to represent each procedure
@dataclass
class Procedure:
    number: str  # Number of the procedure, format: PROCXXX
    ref_doc: str # Number of the reference document, format: DRXX or DEXX or None if empty
    part: int # Number of the part (If a long procedure is partionnated)
    title: str


# Class to manage the procedures
class ProcedureHandler():
    def __init__(self, path: str) -> None:
        self.path = path
        self.list = []
        self.__load_procedures(path)
        self.__sort_procedures()

    def __load_procedures(self, path: str) -> None:
        """Load all the procedures details from a file as a Procedure object and store them in self.procedures"""
        wb = load_workbook(path)
        sheet = wb.active

        for row in sheet.iter_rows(min_row=2, values_only=True):
            self.list.append(Procedure(*row))
        return
    
    def __sort_procedures(self):
        """Sort the procedures by number"""
        try:
            self.list.sort(key=lambda x: (int(x.number[4:]), x.part))
        except ValueError:
            input("Error: One of the procedure number is incorrect!")
            sys.exit(1)
        return
