import os

from utils import (
    MENUS,
    MONTH,
    ProcedureManager,
    console,
    display_all_procedures,
    display_menu,
    display_procedures_menu,
    select_procedures,
    select_quarter,
    want_retry,
)


def main():
    # Initializing the ProcedureManager object
    proc_manager = ProcedureManager()

    # Stack of actives menus
    stack = ["main"]

    while stack:
        os.system("cls" if os.name == "nt" else "clear")
        current_menu = stack[-1]

        # Main starting menu
        if current_menu == "main":
            display_menu(current_menu)

        # exit menu to quit the application
        elif current_menu == "exit":
            quit("Closing the application.")

        # Procedures menu to display all procedures
        elif current_menu == "procedures":
            display_all_procedures(proc_manager)
            input("Press any key to return to main menu")
            stack.pop()
            continue

        # Automatic method selection of the procedures based on the least reviewed procedures
        elif current_menu == "auto":
            quarter = select_quarter()

            # select procedures automaticly and go to selection menu
            procedures = select_procedures(proc_manager, quarter, auto=True)
            stack.append("validation")
            continue

        # Manual method selection
        elif current_menu == "manual":
            quarter = select_quarter()
            procedures = list()

            # For each month of the quarter, prompt the user to choose a procedure
            for i in range(len(MONTH[quarter])):
                selection = select_procedures(
                    proc_manager, quarter=quarter, iteration=i
                )

                # if user choose cancel (empty return, go back to the previous menu)
                if not selection:
                    break

                procedures.append(selection[0])

            if len(procedures) != len(MONTH[quarter]):
                stack.pop()
                continue

            stack.append("validation")
            continue

        # Validation menu to confirm the selection of the procedures for the corresponding quarter
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
                    procedures[choice - 1] = replacement[0]
                continue

            # Choice confirmation
            elif choice == len(procedures) + 1:
                stack.append("confirm")
                continue

            # choice "choose another method"
            elif choice == len(procedures) + 2:
                stack.pop()
                stack.pop()
                continue

            # choice "exit"
            elif choice == len(procedures) + 3:
                stack.append("exit")
                continue

        # Confirmation menu after confirming the selection
        elif current_menu == "confirm":
            # Write the document
            is_writted = proc_manager.write_document(procedures, quarter)
            if is_writted:
                console.print("[green]Your Word file has been generated!")
                input("Press enter to update history file")
            else:
                console.print("[red]File couldn't have been created!")
                if want_retry():
                    continue
                else:
                    stack.append("exit")
                    continue

            # Update the hisotry file:
            is_updated = proc_manager.update_history_file(procedures, quarter)
            if is_updated:
                console.print("[green]The history has been [bold]Updated[/bold]!")
                input("\nPress any key to exit the application")
                stack.append("exit")
                continue
            else:
                console.print("[red]History couldn't have been updated!")
                if want_retry():
                    continue
                else:
                    stack.append("exit")
                    continue

        # use the menu dictionary to update the menu selection
        choice = input().strip()

        if choice in MENUS[current_menu]:
            stack.append(MENUS[current_menu][choice][1])


if __name__ == "__main__":
    main()
