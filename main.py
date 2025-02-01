from rich.console import Console
from rich.markdown import Markdown
from procedures import ProcedureHandler

PATH = "data/procedure_list.xlsx"

# initializing the console for rich text
console = Console()

def main():

    # Initializing the ProcedureHandler object
    procedures = ProcedureHandler(PATH)

    # Variable to keep track of the current menu and the selection
    current_menu = "start"
    quarter = None
    

    # Main loop of the program
    while True:

        # select the menu to display
        match current_menu:

            case "start":
                console.print("\n-----Choose the quarter-----\n")
                console.print("1--Q1 (Jan - Mar)")
                console.print("2--Q2 (Apr - Jun)")
                console.print("3--Q3 (Jul - Sep)")
                console.print("4--Q4 (Oct - Dec)")

                selection_start = input("\nQuarter number: ")

                try:
                    if 0 < int(selection_start) < 5:
                        quarter = selection_start
                        current_menu = "main"
                    else:
                        raise ValueError
                except ValueError:
                    input("Invalid slection. Please enter a number between 1 and 4")

            
            case "main":
                console.print("\n[bold green]=== Main menu ===")
                console.print(f"\nGenerate the discussion file for Q{quarter}: Choose an option\n")
                console.print("1 - Generate the file automaticly")
                console.print("2 - Cherry pick each procedure")
                console.print("3 - Choose another quarter")
                
                selection_main = input()
                
                try:
                    if 0 < int(selection_main) < 4:
                        quarter = selection_main
                        current_menu = "main"
                    else:
                        raise ValueError
                except ValueError:
                    input("Invalid slection. Please enter a number between 1 and 3")
                    continue
                
                print("testing the continue bypass")
                    
                


                # testing part
                # for proc in procedures.list:
                #     print(proc.number, proc.part if proc.part else "")
                # break


if __name__ == "__main__":
    main()
 