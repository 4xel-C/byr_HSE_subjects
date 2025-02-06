from utils import ProcedureManager, select_quarter, select_generation_method, select_automatic_generation_menu

# Path to the DATA folder containing the procedures list, the history and templates
PATH = "data/"

# Match the quarter number (QX) to the corresponding month
MONTH = {
    1: ["January", "February", "March"],
    2: ["April", "May", "June"],
    3: ["July/August", "September"],
    4: ["October", "November", "December"],
}


def main():
    # Initializing the ProcedureManager object
    manager = ProcedureManager(PATH)

    # quarter selection (return 1, 2, 3 or 4)
    quarter = select_quarter()

    # Main loop of the program
    while True:
        method = select_generation_method(quarter)

        # Return to the quarter selection menu
        if method == "back":
            quarter = select_quarter()
            continue

        # Automatic generation based on the least reviewed procedure
        elif method == "auto":

            # If the 3rd quarter was selected, only select 2 procedures (Only 2 procedures reviewed during summer)
            months = MONTH[quarter]
            number_procedure = len(months)
            procedures_selection = manager.select_procedures(number_procedure)
            
            # display the menu
            select_automatic_generation_menu(procedures_selection, quarter, months)

        elif method == "manual":
            print("To be implemented")
            pass

if __name__ == "__main__":
    main()
