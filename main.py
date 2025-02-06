from utils import ProcedureManager, select_quarter, display_menu, select_procedures, display_procedures_menu, display_all_procedures, MENUS, MONTH
import os

# Path to the DATA folder containing the procedures list, the history and templates
PATH = "data/"

def main():

    # Initializing the ProcedureManager object
    proc_manager = ProcedureManager(PATH)

    # Stack of actives menus
    stack = ["main"]

    while stack:
        os.system("cls" if os.name == "nt" else "clear")
        current_menu = stack[-1]

        if current_menu == "main":
            display_menu(current_menu)
        
        elif current_menu == "exit":
            quit("Closing the application.")
            
        elif current_menu == "procedures":
            display_all_procedures(proc_manager)
            input("Press any key to return to main menu")
            stack.pop()
            continue

        elif current_menu == "auto":
            quarter = select_quarter()
            
            # select procedures automaticly and go to selection menu
            procedures = select_procedures(proc_manager, quarter, auto=True)
            stack.append("validation")
            continue

        elif current_menu == "manual":
            quarter = select_quarter()
            procedures = list()

            # For each month of the quarter, prompt the user to choose a procedure
            for _ in range(len(MONTH[quarter])):
                selection = select_procedures(proc_manager)

                # if user choose cancel (empty return, go back to the previous menu)
                if not selection:
                    break

                procedures.append(selection[0])

            if len(procedures) != len(MONTH[quarter]):
                stack.pop()
                continue
            
            stack.append("validation")
            continue

            
        elif current_menu == "validation":
            display_procedures_menu(procedures, quarter)

            try:
                choice = int(input("Select your option: ").strip())
                if not 0 < choice <= len(procedures) + 3:
                    raise ValueError
            except (ValueError, TypeError):
                continue

            if 0 < choice <= len(procedures):
                replacement = select_procedures(proc_manager)
                if replacement:
                    procedures[choice-1] = replacement[0]
                continue
            
            # Choice confirmation
            elif choice == len(procedures)+1:
                stack.append("confirm")

            # choice "choose another method"
            elif choice == len(procedures)+2:
                stack.pop()
                stack.pop()
                continue

            # choice "exit"
            elif choice == len(procedures)+3:
                stack.append("exit")
                continue

        elif current_menu == "confirm":
            input("TO BE IMPLEMENTED")
            stack.pop()
            continue

        choice = input().strip()

        if choice in MENUS[current_menu]:
            stack.append(MENUS[current_menu][choice][1])

if __name__ == "__main__":
    main()
