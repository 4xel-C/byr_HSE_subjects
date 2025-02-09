import os
from datetime import datetime

from rich.console import Console

from .config import MONTH
from .procedures import Procedure, ProcedureManager

# initializing the console for rich text
console = Console()


# Main menu definitions (can be implemented to add sub menus using the stack to navigate)
MENUS = {
    "main": {
        "1": ("Automatic procedure selection", "auto"),
        "2": ("Manual procedure selection", "manual"),
        "3": ("View procedures list", "procedures"),
        "4": ("Quit", "exit"),
    },
}


def display_menu(menu: str) -> None:
    """Function to display a menu.
    Args:
        menu (str): menu title to disply"""

    if menu == "main":
        console.print("\n[bold green]=== Main Menu ===")
        print()
        for key, (desc, _) in MENUS[menu].items():
            console.print(f"{key}. {desc}")


def display_procedures_menu(procedures: list[Procedure], quarter: int):
    """Display the Validation procedure menu generated when all the procedure for the current quarter have been generated.

    Args:
        procedures (list[Procedure]): List of Procedure object.
        quarter (int): The quarter for which the generation is applied.
    """

    console.print(f"\n[bold green]=== Proposed Selection for Q{quarter} ===")
    console.print("\nSelect the procedure you want to edit or confirm the selection\n")

    months = MONTH[quarter]
    options = {}

    for i, proc in enumerate(procedures):
        month_string = months[i]

        console.print(
            f"{i+1} - [bold blue]{month_string}[/bold blue] - [bold]{proc.number}[/bold] : {proc.title}"
        )

        # Gather all the options for the user input and map them to the correct procedure index in the procedures list.
        options[str(i + 1)] = f"{i}"

    print("----------------------------")

    # Adding the accept option
    console.print(f"{len(options) + 1} - Confirm selection")
    options[str(len(options) + 1)] = "confirm"

    # Adding the back option
    console.print(f"{len(options) + 1} - Choose another method")
    options[str(len(options) + 1)] = "back"

    # Adding the close application option
    console.print(f"{len(options) + 1} - Exit the application")
    options[str(len(options) + 1)] = "exit"


def display_all_procedures(manager: ProcedureManager):
    """Method to display all procedures for the procedures menu (View procedures list selection.)

    Args:
        manager (ProcedureManager): Need the ProcedureManager as input to manage all the loaded procedure.
    """

    procedures = manager.get_procedures()
    for i, proc in enumerate(procedures):
        row = f"{i+1:<2} - "

        num = f"[bold]{proc.number:<}[/bold]"
        title = proc.title

        if proc.last_review == datetime.min:
            last_review = "[blue]Last review: [bold]Never[/blue]"
        else:
            last_review = (
                f"[blue]Last review: {proc.last_review.strftime("%Y-%m")}[/blue]"
            )

        row = row + num + " - " + title + " - " + last_review

        console.print(row)


# ------------------------------------------------------------------------------------------- Helper functions
# Quarter selection function
def select_quarter() -> int:
    """Quarter submenu to display the quarter selection after selecting a method.

    Returns:
        int: return the user selection to match with the MONTH dictionnary constant.
    """

    console.print("\n[bold green]-----Choose the quarter-----\n")
    console.print("1--Q1 (Jan - Mar)")
    console.print("2--Q2 (Apr - Jun)")
    console.print("3--Q3 (Jul - Sep)")
    console.print("4--Q4 (Oct - Dec)")
    console.print("5--Exit the application")

    while True:
        selection = input("\nQuarter number: ").strip()

        if selection in {"1", "2", "3", "4"}:
            return int(selection)
        elif selection == "5":
            exit("Exiting the application")

        console.print("[red] Invalid selection. Please enter a number between 1 and 5")


# Select procedures
def select_procedures(
    manager: ProcedureManager,
    quarter: int = 1,
    auto: bool = False,
    iteration: int = None,
) -> list[Procedure]:
    """Function to display a procedure selection menu, used in the manual selection method, or in the procedure edition process on the confirmation menu.
    Also used in the automatic selection to select the least reviewed procedure by the month concerned by the desired quarter.

    Args:
        manager (ProcedureManager): ProcedureManager object to get all the procedures sorted and loaded by the program.
        quarter (int, optional): Quarter considered. Defaults to 1.
        auto (bool, optional): Decide if the selection should be automatic or manual by the user. Defaults to False.
        iteration (int, optional): Can pass an iteration number to iterated through the deffirent MONTH or the quarter during the manual selection method. Defaults to None.

    Returns:
        list[Procedure]: Return a list of the selected procedures. If only 1 procedure is selected during the manual method, return a list with 1 procedure.
    """

    if auto:
        # number of procedures to get (1 by month)
        n = len(MONTH[quarter])

        # get the sorted procedures
        return manager.get_procedures(n)

    else:
        procedures = manager.get_procedures()

        # Display the procedure and input the user for a choice
        # Clear the terminal
        os.system("cls" if os.name == "nt" else "clear")

        # If method called multiple times, provide the month detail
        if iteration is not None:
            console.print(
                f"\n[bold green]=== Select a procedure for {MONTH[quarter][iteration]} ==="
            )
        for i, proc in enumerate(procedures):
            console.print(
                f"{i+1} - [blue]Last review: {proc.last_review.strftime("%Y-%m")}[/blue] - [bold]{proc.number}[/bold] : {proc.title}"
            )

        console.print(f"{len(procedures) + 1} - [bold red]Cancel")

        while True:
            try:
                choice = int(input("\nSelect a replacement procedure: "))
                if not (0 < choice <= len(procedures) + 1):
                    raise ValueError
            except (ValueError, TypeError):
                console.print("[red]Bad input!")
                continue

            if choice == len(procedures) + 1:
                return []
            else:
                return [procedures[choice - 1]]


def want_retry():
    """Prompt a user to retry an action

    Returns:
        Bool: Return a boolean value True or False
    """
    while True:
        choice = input("Retry ? y/n").strip()

        if choice.isalpha():
            if choice.upper() in ["Y", "YES", "O", "OUI"]:
                return True
            elif choice.upper() in ["N", "NO", "NON"]:
                return False

        print("Wrong input")
