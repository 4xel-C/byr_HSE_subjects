from datetime import datetime
import os
from rich.console import Console
from .procedures import Procedure, ProcedureManager

# initializing the console for rich text
console = Console()

# Menu definitions
MENUS = {
    "main": {
        "1": ("Automatic procedure selection", "auto"),
        "2": ("Manual procedure selection", "manual"),
        "3": ("View procedures list", "procedures"),
        "4": ("Quit", "exit")
    },
}

# Match the quarter number (QX) to the corresponding month
MONTH = {
    1: ["January", "February", "March"],
    2: ["April", "May", "June"],
    3: ["July/August", "September"],
    4: ["October", "November", "December"],
}


def display_menu(menu: str) -> None:

    if menu == "auto":
        pass

    elif menu == "manual":
        pass

    else:
        console.print("\n[bold green]=== Main Menu ===") 
        print()
        for key, (desc, _) in MENUS[menu].items():
                console.print(f"{key}. {desc}")


def display_procedures_menu(procedures: list[Procedure], quarter: int):
    console.print("\n[bold green]=== Proposed Selection for Q{quarter} ===")
    console.print("\nSelect the procedure you want to edit or confirm the selection\n")

    months = MONTH[quarter]
    options = {}
    
    for i, proc in enumerate(procedures):
        
        month_string = months[i]
        
        console.print(f"{i+1} - [bold blue]{month_string}[/bold blue] - [bold]{proc.number}[/bold] : {proc.title}")
        
        # Gather all the options for the user input and map them to the correct procedure index in the procedures list.
        options[str(i+1)] = f"{i}"

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


# Starting menu function
def select_quarter() -> int:
    """Starting menu function to display the quarter selection to the user and manage his choice."""
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
def select_procedures(manager: ProcedureManager, quarter: str = 1, auto: bool = False) -> list[Procedure]:

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
        for i, proc in enumerate(procedures):
            console.print(f"{i+1} - [blue]Last review: {proc.last_review.strftime("%Y-%m")}[/blue] - [bold]{proc.number}[/bold] : {proc.title}")
        
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
                return [procedures[choice-1]]
        
def display_all_procedures(manager: ProcedureManager):
    procedures = manager.get_procedures()
    for i, proc in enumerate(procedures):
            row = f"{i+1:<2} - "

            num = f"[bold]{proc.number:<}[/bold]"
            title = proc.title
            
            if proc.last_review == datetime.min:
                last_review = "[blue]Last review: [bold]Never[/blue]"
            else:
                last_review = f"[blue]Last review: {proc.last_review.strftime("%Y-%m")}[/blue]"

            row = row + num + " - " + title + " - " + last_review

            console.print(row)
