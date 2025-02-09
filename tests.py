import unittest
from datetime import datetime, timedelta
from unittest.mock import MagicMock, patch


from utils import (
    Procedure,
    ProcedureManager,
    display_all_procedures,
    display_menu,
    display_procedures_menu,
    select_procedures,
    select_quarter,
)


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

    @patch("builtins.input", side_effect=["3"])
    @patch("rich.console.Console.print")
    def test_select_quarter_3(self, mock_print, mock_input):
        result = select_quarter()
        self.assertEqual(result, 3)
        mock_print.assert_any_call("\n[bold green]-----Choose the quarter-----\n")
        mock_print.assert_any_call("3--Q3 (Jul - Sep)")

    # test 2 bad selection, then a selection with a space for quarter selection
    @patch("builtins.input", side_effect=["abc", "7", "2  "])
    def test_select_quarter_invalid_then_valid(self, mock_input):
        self.assertEqual(select_quarter(), 2)

    # -------------------------------------------------Display_menu
    @patch("rich.console.Console.print")
    def test_display_menu(self, mock_print):
        display_menu("main")
        self.assertTrue(mock_print.called)
        mock_print.assert_any_call("\n[bold green]=== Main Menu ===")
        self.assertIn(
            "1. Automatic procedure selection",
            [call[0][0] for call in mock_print.call_args_list],
        )

    # -------------------------------------------------Display_procedures_menu
    @patch("rich.console.Console.print")
    def test_display_procedures_menu_Q1(self, mock_print):
        # Create a mock procedure list
        procedures = list()
        for i in range(3):
            mock_procedure = MagicMock()
            mock_procedure.number = f"{i}"
            mock_procedure.title = f"title {i}"
            mock_procedure.last_review = datetime.min + timedelta(days=i)
            procedures.append(mock_procedure)

        display_procedures_menu(procedures, 1)

        self.assertTrue(mock_print.called)
        mock_print.assert_any_call("\n[bold green]=== Proposed Selection for Q1 ===")
        mock_print.assert_any_call(
            "1 - [bold blue]January[/bold blue] - [bold]0[/bold] : title 0"
        )
        mock_print.assert_any_call(
            "2 - [bold blue]February[/bold blue] - [bold]1[/bold] : title 1"
        )
        mock_print.assert_any_call(
            "3 - [bold blue]March[/bold blue] - [bold]2[/bold] : title 2"
        )

    @patch("rich.console.Console.print")
    def test_display_procedures_menu_Q3(self, mock_print):
        # Create a mock procedure list
        procedures = list()
        for i in range(2):
            mock_procedure = MagicMock()
            mock_procedure.number = f"{i}"
            mock_procedure.title = f"title {i}"
            mock_procedure.last_review = datetime.min + timedelta(days=i)
            procedures.append(mock_procedure)

        display_procedures_menu(procedures, 3)

        self.assertTrue(mock_print.called)
        mock_print.assert_any_call("\n[bold green]=== Proposed Selection for Q3 ===")
        mock_print.assert_any_call(
            "1 - [bold blue]July/August[/bold blue] - [bold]0[/bold] : title 0"
        )
        mock_print.assert_any_call(
            "2 - [bold blue]September[/bold blue] - [bold]1[/bold] : title 1"
        )

    # ------------------------------- Procedure selection menu
    @patch("utils.ProcedureManager")
    @patch("os.system")  # Mock os.system to prevent clearing the console
    @patch("builtins.input", side_effect=["3"])
    @patch("rich.console.Console.print")
    def test_select_procedures_manu(
        self, mock_print, mock_input, mock_os, mock_manager
    ):
        # Create a mock procedure list
        procedures = list()
        for i in range(5):
            mock_procedure = MagicMock()
            mock_procedure.number = f"{i}"
            mock_procedure.title = f"title {i}"
            mock_procedure.last_review = datetime.min + timedelta(days=i)
            procedures.append(mock_procedure)

        mock_manager.get_procedures.return_value = procedures

        result = select_procedures(mock_manager, quarter=1, auto=False)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].number, "2")
        mock_print.assert_called()

    @patch("utils.ProcedureManager")
    @patch("os.system")  # Mock os.system to prevent clearing the console
    @patch("builtins.input", side_effect=["9", "5"])
    @patch("rich.console.Console.print")
    def test_select_procedures_manu_wrong_then_right(
        self, mock_print, mock_input, mock_os, mock_manager
    ):
        # Create a mock procedure list
        procedures = list()
        for i in range(5):
            mock_procedure = MagicMock()
            mock_procedure.number = f"{i}"
            mock_procedure.title = f"title {i}"
            mock_procedure.last_review = datetime.min + timedelta(days=i)
            procedures.append(mock_procedure)

        mock_manager.get_procedures.return_value = procedures

        result = select_procedures(mock_manager, quarter=1, auto=False)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].number, "4")
        mock_print.assert_called()

    @patch("utils.ProcedureManager")
    @patch("os.system")  # Mock os.system to prevent clearing the console
    @patch("builtins.input", side_effect=["6"])
    @patch("rich.console.Console.print")
    def test_select_procedures_manu_cancel(
        self, mock_print, mock_input, mock_os, mock_manager
    ):
        # Create a mock procedure list
        procedures = list()
        for i in range(5):
            mock_procedure = MagicMock()
            mock_procedure.number = f"{i}"
            mock_procedure.title = f"title {i}"
            mock_procedure.last_review = datetime.min + timedelta(days=i)
            procedures.append(mock_procedure)

        mock_manager.get_procedures.return_value = procedures

        result = select_procedures(mock_manager, quarter=1, auto=False)

        self.assertEqual(len(result), 0)
        mock_print.assert_called()

    @patch("utils.ProcedureManager")
    @patch("os.system")  # Mock os.system to prevent clearing the console
    @patch("builtins.input", side_effect=["6"])
    @patch("rich.console.Console.print")
    def test_select_procedures_auto(
        self, mock_print, mock_input, mock_os, mock_manager
    ):
        # Create a mock procedure list
        procedures = list()
        for i in range(2):
            mock_procedure = MagicMock()
            mock_procedure.number = f"{i}"
            mock_procedure.title = f"title {i}"
            mock_procedure.last_review = datetime.min + timedelta(days=i)
            procedures.append(mock_procedure)

        mock_manager.get_procedures.return_value = procedures

        result = select_procedures(mock_manager, quarter=3, auto=True)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].number, "0")
        self.assertEqual(result[1].number, "1")
        mock_print.assert_not_called()

    # ----------------------------------------- View all procedures menu

    @patch("rich.console.Console.print")
    def test_display_all_procedures(self, mock_print):
        procedures = list()
        for i in range(5):
            mock_procedure = MagicMock()
            mock_procedure.number = f"{i}"
            mock_procedure.title = f"title {i}"
            mock_procedure.last_review = datetime.min + timedelta(days=i)
            procedures.append(mock_procedure)

        mock_manager = MagicMock()
        mock_manager.get_procedures.return_value = procedures

        display_all_procedures(mock_manager)

        self.assertTrue(mock_print.called)
        self.assertEqual(mock_print.call_count, 5)


class TestProcedure(unittest.TestCase):
    # Testing initializing procedure object
    def test_procedure_initialization(self):
        procedure = Procedure(
            number="PROC001", part=1, title="Test title", ignored=False
        )

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
            ("PROC001", 1, "Title 1", False),
            ("PROC002", 2, "Title 2", False),
            ("PROC003", None, "Title 3", False),
            ("PROC004 ", None, "Title 3", False),
            (" PROC005 ", None, "Title 3", False),
        ]

        #  create a fake workbook history
        self.mock_workbook_history = MagicMock()
        mock_sheet = self.mock_workbook_history.active
        mock_sheet.iter_rows.return_value = [
            ("PROC001", datetime(2022, 6, 1, 0, 0)),
            ("PROC002", datetime(2022, 7, 1, 0, 0)),
            ("PROC001 ", datetime(2022, 8, 1, 0, 0)),
            (("PROC005"), datetime(2022, 9, 1, 0, 0)),
            (("PROCXYZ"), datetime(2022, 12, 1, 0, 0)),
        ]

    # mock the load_workbook method
    @patch("utils.procedures.load_workbook")
    def test_load_procedures(self, mock_load_workbook):
        # Two 'load_workbook' function are called when instanciating the ProcedureManager: 1 to load the procedures, the other, the history.
        mock_load_workbook.side_effect = [
            self.mock_workbook_proc,
            self.mock_workbook_history,
        ]

        # Initialize ProcedureManager
        manager = ProcedureManager()

        # Check if procedure are correctly charged
        self.assertEqual(manager.procedures[0].number, "PROC001")
        self.assertEqual(manager.procedures[1].number, "PROC002")
        self.assertEqual(manager.procedures[3].number, "PROC004")
        self.assertEqual(manager.procedures[4].number, "PROC005")
        self.assertEqual(manager.procedures[2].title, "Title 3")
        self.assertIs(manager.procedures[2].part, None)
        self.assertEqual(len(manager.procedures), 5)
        self.assertEqual(manager.procedures[2].last_review, datetime.min)

    @patch("utils.procedures.load_workbook")
    def test_generate_history(self, mock_load_workbook):
        # Two 'load_workbook' function are called when instanciating the ProcedureManager: 1 to load the procedures, the other, the history.
        mock_load_workbook.side_effect = [
            self.mock_workbook_proc,
            self.mock_workbook_history,
        ]

        # Initialize ProcedureManager
        manager = ProcedureManager()

        # Check if dictionnary has been correctly created
        self.assertEqual(manager.procedures[0].last_review, datetime(2022, 8, 1, 0, 0))
        self.assertEqual(manager.procedures[1].last_review, datetime(2022, 7, 1, 0, 0))
        self.assertEqual(manager.procedures[4].last_review, datetime(2022, 9, 1, 0, 0))
        (self.assertEqual(manager.procedures[2].last_review, datetime.min),)
        self.assertEqual(manager.procedures[4].last_review, datetime(2022, 9, 1, 0, 0))

    @patch("utils.procedures.load_workbook")
    def test_get_procedure_3(self, mock_load_workbook):
        # Two 'load_workbook' function are called when instanciating the ProcedureManager: 1 to load the procedures, the other, the history.
        mock_load_workbook.side_effect = [
            self.mock_workbook_proc,
            self.mock_workbook_history,
        ]

        # Initialize ProcedureManager
        manager = ProcedureManager()

        selected = manager.get_procedures(3)

        self.assertEqual(len(selected), 3)

        # Check if there are sorted by data
        self.assertLessEqual(selected[0].last_review, selected[1].last_review)
        self.assertLessEqual(selected[1].last_review, selected[2].last_review)

        # Check the 3 older procedures
        self.assertEqual(selected[0].number, "PROC003")
        self.assertEqual(selected[1].number, "PROC004")
        self.assertEqual(selected[2].number, "PROC002")

    @patch("utils.procedures.load_workbook")
    def test_get_procedure_2(self, mock_load_workbook):
        # Two 'load_workbook' function are called when instanciating the ProcedureManager: 1 to load the procedures, the other, the history.
        mock_load_workbook.side_effect = [
            self.mock_workbook_proc,
            self.mock_workbook_history,
        ]

        # Initialize ProcedureManager
        manager = ProcedureManager()

        selected = manager.get_procedures(2)

        self.assertEqual(len(selected), 2)

        # Check if there are sorted by data
        self.assertLessEqual(selected[0].last_review, selected[1].last_review)

        # Check the 3 older procedures
        self.assertEqual(selected[0].number, "PROC003")
        self.assertEqual(selected[1].number, "PROC004")

    @patch("utils.procedures.load_workbook")
    def test_get_procedure_all(self, mock_load_workbook):
        # Two 'load_workbook' function are called when instanciating the ProcedureManager: 1 to load the procedures, the other, the history.
        mock_load_workbook.side_effect = [
            self.mock_workbook_proc,
            self.mock_workbook_history,
        ]

        # Initialize ProcedureManager
        manager = ProcedureManager()

        selected = manager.get_procedures()

        self.assertEqual(len(selected), len(manager.procedures))

        # Check if there are sorted by data
        self.assertLessEqual(selected[0].last_review, selected[1].last_review)

        # Check the 3 older procedures
        self.assertEqual(selected[0].number, "PROC003")
        self.assertEqual(selected[1].number, "PROC004")


# run the tests
if __name__ == "__main__":
    unittest.main()
