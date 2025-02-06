from rich.console import Console
from .procedures import Procedure

# initializing the console for rich text
console = Console()


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


# Main menu function
def select_generation_method(quarter: int) -> str:
    """Function to display the main menu to the user and manage his choice.
    Parameter: quarter (int): selected in the 'select_quarter' function."""

    console.print("\n[bold green]=== Main menu ===")
    console.print(f"\nGenerate the discussion file for Q{quarter}: Choose an option\n")
    console.print("1 - Generate the file automaticly")
    console.print("2 - Cherry pick each procedure")
    console.print("3 - Choose another quarter")
    console.print("4 - Exit the application")

    while True:
        selection = input("\nMenu selection:").strip()

        match selection:
            case "1":
                return "auto"
            case "2":
                return "manual"
            case "3":
                return "back"
            case "4":
                exit("Exiting the application")
            case _:
                console.print(
                    "[red]Invalid selection. Please enter a number between 1 and 3"
                )

def select_automatic_generation_menu(procedures: list[Procedure], quarter: int, months: list) -> str:
    """Display the menu after choosing the selection method for the procedure:
    Display the proposed procedures for each month and propose and edition / validation menu.
    Take as input a list of procedures to display, the selected quarter, and the list of month.
    Return the user menu selection."""
    
    console.print(f"\n[bold green]=== Proposed Selection for Q{quarter} ===")
    console.print(f"\nSelect the procedure you want to edit or confirm the selection\n")

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
    
    while True:
        selection = input("\nYour selection: ").strip()
        
        if selection not in options:
            console.print("[red]Invalid selection. Please retry.")
            
        elif options[selection] == "exit":
            exit("Exiting the application")
        
        else: 
            return options[selection]
        

def manual_selection_procedure_menu(procedures: list[Procedure]) -> str:
    """Recieve a list of procedure as an argument and diisplay all the procedure sorted by last review date.
    Return the index of the selected procedure by the user."""
    
    console.print(f"\n[bold green]=== Select the new procedure ===")    
    
    options = {}
    
    for i, proc in enumerate(procedures):
   
        console.print(f"{i+1} - [bold blue]{proc.number}[/bold blue] - [bold]{proc.title}[/bold] - Last review date: {proc.last_review.strftime("%Y-%m")}")
        
        # Gather all the options for the user input and map them to the correct procedure index in the procedures list.
        options[str(i+1)] = f"{i}"
    
    print("----------------------------")
        
    # Adding the back option
    console.print(f"{len(options) + 1} - Back")
    options[str(len(options) + 1)] = "back"
    
    while True:
        selection = input("\nYour selection: ").strip()
        
        if selection not in options:
            console.print("[red]Invalid selection. Please retry.")
        else: 
            return options[selection]