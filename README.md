
# 🚧 UNDER CONSTRUCTION 🚧  

## 🚀 To Be Implemented  

- [ ] Complete the menu logic and overall program functionality.  
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
