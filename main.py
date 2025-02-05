from utils import ProcedureManager, select_quarter, select_generation_method

# Path to the DATA folder containing the procedures list, the history and templates
PATH = "data/"


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
            print("to be implemented")
            pass

        elif method == "manual":
            print("To be implemented")
            pass

if __name__ == "__main__":
    main()
