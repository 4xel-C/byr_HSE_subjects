
# 🚧 UNDER CONSTRUCTION 🚧  

## 🚀 To Be Implemented  

- [x] Complete the menu navigation logic. 
- [x] Enable priority selection of newly added procedures that have never appeared in the archive.  
- [x] Enable cherry picking when reviewing the selection.
- [x] Enable procedure checking to make sure no procedure are forgotten.
- [x] Implement The word file generation
- [x] Implement The update of the history list
- [x] Correction of a bug while loading the application where the history saves the new dates as string and not Date object.
- [ ] Implementation of an automatic mail generation method to send the discussion form


# Automation of Subject Generation for HSE Discussions  

## Introduction  
This program automates the generation of monthly security discussion documents at Bayer. It automatically selects one subject per month for the current quarter and tracks which procedures have been reviewed along with their dates through a CLI application where users navigate through menu using number input.

## Generation Options  
Two options are available for generating the document:  

1. **Automatic Generation**  
   - Randomly selects from the six procedures that have not been recently reviewed.  
   - Compares the monitoring list with the full list of available procedures.  
   - If new procedures are added, they are automatically prioritized for selection.  

2. **Cherry-Pick Option**  
   - Allows the user to manually select which procedure will be reviewed each month.  

After proposing the procedures for review, the program lets the user edit the selection by:  
- Choosing a specific month.  
- Deciding whether to randomly select a new procedure from the oldest ones or manually pick a preferred one. 

## Files

- `main.py`: Launcher file. This file will contains all the CLI's menus interaction. It uses the functions from the `menu.py` to manage menus displaying and user's choices.
- `utils` package:
   - `procedures.py`: This file contains the data structure to manage procedures using the following classes:
      -  `Procedure` dataclass: This class map the information of each procedure into a `Procedure` object, to keep track of the tittle, their code, their function (reference document or not), and the last date they were discussed among the teams.
      - `ProcedureManager`: Class to load all the procedures available. It recieves a `'PATH'` to instanciate the handler, with PATH beeing the path of the folder containing the procedures, the history, and the templates.
   - `menu`: File containing the function used to display and interact with each nested menus.
- `tests.py`: Containing all UnitTesting to ensure fiability.

## Technologies Used
- `UV`: For dependencies management and virtual environment.
- `Jupyter Notebook`: To manipulate the data.
- `Rich`: To displayer more user friendly messages in the console.
- `Openpyxl`: To manipulate and extract information from the excel files.
- `Datetime`: To keep track of the history of the discussion through datetime object.
- `Dataclass`: To facilitate creation of a data object.

## Requirement
- python >= 3.13
- openpyxl >= 3.1.5
- rich >= 13.9.4

## Installation

1. Clone the repository
2. Set up the environment using UV
   ```bash
   UV venv
   UV sync
   ```
3. Start the application
   ```bash
   python main.py
   ```

## Processus and details
The algorithm works using a **stack** menu logic: 
- Allowing the menu exploration by implementation of a 'FIFO' (First In First Out') Data structure where the last element become the actual visited menu.
- Computing logic of each menu is then separated by `if` statements using the last element of the *stack menu* as the current menu.
- The *backing* option is managed by poping out the last element of the pile, letting the previous one beeing the active menu.
- The whole logic is nested into a while loop to allow infinite navigation between menus.
- User may have the option to properly quit the application in each menu.
- User navigation is managed by inputs
   - Inputting a number to select the desired menu
   - Error management reprompting the user if an incorrect input has been entered.

The *Procedures* are managed through 2 custom objects:
   - The *Procedure* object, a data class To store all the information contained by each procedure.
   - The *ProcedureManager* object to read, write on the CSV files containing the datas, and create all the procedures, manage the extraction method, the sorting, and everything related to bring modification to this Procedures or on the CSV files storing the original datas.
