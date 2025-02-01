from procedures import ProcedureHandler
from menu import select_quarter, select_generation_method

PATH = "data/procedure_list.xlsx"


def main():
    # Initializing the ProcedureHandler object
    procedures = ProcedureHandler(PATH)

    # quarter selection
    quarter = select_quarter()

    # Main loop of the program
    while True:
        method = select_generation_method(quarter)

        # Return to the quarter selection menu
        if method == "back":
            quarter = select_quarter()
            continue


if __name__ == "__main__":
    main()
