from procedures import ProcedureManager
from menu import select_quarter, select_generation_method

# Path to the DATA folder containing the procedures list, the history and templates
PATH = "data/"


def main():
    # Initializing the ProcedureManager object
    manager = ProcedureManager(PATH)
    print(manager.procedures)

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
