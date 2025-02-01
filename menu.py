from rich.console import Console

# initializing the console for rich text
console = Console()


# Starting menu function
def select_quarter() -> int:
    """Starting menu function to display the quarter selection to the user and manage his choice."""
    console.print("\n-----Choose the quarter-----\n")
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

        if selection == "1":
            return "auto function"
        elif selection == "2":
            return "manual function"
        elif selection == "3":
            return "back"
        elif selection == "4":
            exit("Exiting the application")
        else:
            console.print(
                "[red]Invalid selection. Please enter a number between 1 and 3"
            )
