import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from openpyxl import Workbook

from menu import select_quarter, select_generation_method
from procedures import ProcedureManager, Procedure


class TestMenuSelection(unittest.TestCase):
    
    # ----------------------------------------Quarter selection Test
    # test selection 1 for quarter selection
    @patch("builtins.input", side_effect=["1"])
    def test_select_quarter(self, mock_input):
        self.assertEqual(select_quarter(), 1)

    # test selection 5 for quarter selection
    @patch("builtins.input", side_effect=["5"])
    def test_select_quarter_exit(self, mock_input):
        with self.assertRaises(SystemExit):
            select_quarter()

    # test 2 bad selection, then a selection with a space for quarter selection
    @patch("builtins.input", side_effect=["abc", "7", "2  "])
    def test_select_quarter_invalid_then_valid(self, mock_input):
        self.assertEqual(select_quarter(), 2)

    # test selection 1 for quarter selection
    @patch("builtins.input", side_effect=["1"])
    def test_select_generation_method(self, mock_input):
        self.assertEqual(select_generation_method(1), "auto function")

    # ----------------------------------------Method selection test
    @patch("builtins.input", side_effect=["2"])
    def test_select_generation_method_manual(self, mock_input):
        self.assertEqual(select_generation_method(1), "manual function")

    @patch("builtins.input", side_effect=["sdqfkjh", "76", "3  "])
    def test_select_generation_method_invalid_then_valid(self, mock_input):
        self.assertEqual(select_generation_method(1), "back")

    @patch("builtins.input", side_effect=["4"])
    def test_select_generation_method_exit(self, mock_input):
        with self.assertRaises(SystemExit):
            select_generation_method(1)
            
class TestProcedure(unittest.TestCase):
    
    # Testing initializing procedure object
    def test_procedure_initialization(self):
        
        procedure = Procedure(number="PROC001", part=1, title="Test title", ignored=False)

        self.assertEqual(procedure.number, "PROC001")
        self.assertEqual(procedure.part, 1)
        self.assertEqual(procedure.title, "Test title")
        self.assertFalse(procedure.ignored)


class TestProcedureManager(unittest.TestCase):

    # setup method to create fake workbooks
    def setUp(self):
        
        # Create a fake work book procedure
        self.mock_workbook_proc = MagicMock()
        mock_sheet = self.mock_workbook_proc.active
        mock_sheet.iter_rows.return_value = [
            ("PROC001", 1, "Titre 1", False),  
            ("PROC002", 2, "Titre 2", False),  
        ]
        
        #  create a fake workbook history
        self.mock_workbook_history = MagicMock()
        mock_sheet = self.mock_workbook_history.active
        mock_sheet.iter_rows.return_value = [
            ("PROC001", datetime(2022, 6, 1, 0, 0)),  
            ("PROC002", datetime(2022, 6, 1, 0, 0)),  
        ]
        

    # mock the load_workbook method 
    @patch('procedures.load_workbook')
    def test_load_procedures(self, mock_load_workbook):
        
        # Two 'load_workbook' function are called when instanciating the ProcedureManager: 1 to load the procedures, the other, the history.
        mock_load_workbook.side_effect = [self.mock_workbook_proc, self.mock_workbook_history]
        

        # Initialiser ProcedureManager
        manager = ProcedureManager(path='/fake/path/')

        # Vérifier que les procédures ont été chargées correctement
        self.assertEqual(len(manager.procedures), 2)
        self.assertEqual(manager.procedures[0].number, "PROC001")
        self.assertEqual(manager.procedures[1].number, "PROC002")


# run the tests
if __name__ == "__main__":
    unittest.main()
