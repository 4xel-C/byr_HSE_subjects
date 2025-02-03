
# 🚧 UNDER CONSTRUCTION 🚧  

## 🚀 To Be Implemented  

- [ ] Complete the menu navigation logic. 
- [ ] Enable priority selection of newly added procedures that have never appeared in the archive.  
- [ ] Enable cherry picking when reviewing the selection.
- [ ] Enable procedure checking to make sure no procedure are forgotten.


# Automation of Subject Generation for HSE Discussions  

## Introduction  
This program automates the generation of monthly security discussion documents at Bayer. It automatically selects one subject per month for the current quarter and tracks which procedures have been reviewed along with their dates.  

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

- `main.py`: This file will contains all the CLI's menus interaction. It uses the functions from the `menu.py` to manage menus displaying and user's choices.
- `procedures.py`: This file contains the data structure to manage procedures using the following classes:
   -  `Procedure` dataclass: This class map the information of each procedure into a `Procedure` object, to keep track of the tittle, their code, their function (reference document or not), and the last date they were discussed among the teams.
   - `ProcedureManager`: Class to load all the procedures available. It recieves a `'PATH'` to instanciate the handler, with PATH beeing the path of the folder containing the procedures, the history, and the templates.