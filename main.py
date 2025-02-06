from utils import ProcedureManager, select_quarter, select_generation_method, select_automatic_generation_menu, manual_selection_procedure_menu

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
    
    # Initialize the method variable that will recieve the method to apply1
    method = ""
    procedures_selection = None

    # Main loop of the program
    while True:
        
        # Initialize the variables used for the loop
        months = MONTH[quarter]
        number_procedure = len(months)
        
        if not method:
            method = select_generation_method(quarter)

        # Return to the quarter selection menu
        if method == "back":
            method = None
            quarter = select_quarter()
            continue

        # --------------------------------Automatic generation based on the least reviewed procedure
        elif method == "auto":
            
            # Procédures selected for the document
            if not procedures_selection:
                procedures_selection = manager.get_procedures(number_procedure)
            
            # display the menu and get the selection from the user
            selection_to_change = select_automatic_generation_menu(procedures_selection, quarter, months)          
            
            if selection_to_change == "back":

                # Reinitialize the variables
                method = None
                procedures_selection = None
                continue
            
            elif selection_to_change == "confirm":
                print("TO BE IMPLEMENTED")
                continue
            
            # If user want to edit one specific procedure
            else:
                all_procedures_list = manager.get_procedures()
                procedure_replacement_index = manual_selection_procedure_menu(all_procedures_list)
                
                # if user choose to back without modifying a procedure
                if procedure_replacement_index == 'back':
                    continue
                
                # replace the desired procedure by the new selection
                procedures_selection[int(selection_to_change)] = all_procedures_list[int(procedure_replacement_index)]
                continue
                
        # ----------------------------------------- Manual generation of procedures
        elif method == "manual":
            print("To be implemented")
            method= None
            continue

if __name__ == "__main__":
    main()
