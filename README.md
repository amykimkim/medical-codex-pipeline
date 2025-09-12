# medical-codex-pipeline
Objective: to create python scripts that process medical codex listed below into a standardized CSV format with only the columns that are relevant. Each python script had an objective of having three columns in the final output csv, this includes: code, description, and last update (the time when it was worked on).

## Loading in the data
- I loaded in the data utilizing the following links that were given to us through Professor Hants' repository:

    ### Snowmed (US)
- https://www.nlm.nih.gov/healthit/snomedct/archive.html

    ### ICD-10-CM (US)
- https://www.cms.gov/medicare/coding-billing/icd-10-codes 

    ### ICD-10 (WHO)
- https://icdcdn.who.int/icd10/index.html 

    ### HCPCS (US)
- https://www.cms.gov/medicare/coding-billing/healthcare-common-procedure-system/quarterly-update 

    ### LOINC (US)
- https://loinc.org/downloads/ 

    ### RxNorm (US)
- https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html 

    ### NPI (US) 
- https://download.cms.gov/nppes/NPI_Files.html 

## .gitignore
- A .gitignore file was created to exclude raw data files, especially large ones that Github was not enabling to save to the repository.
- I mainly copied the .ignore from Professor Hants' repository and made sure I also added in *.txt, *.xml, *.zip

##  /input
- I placed all of my input files into this folder and then it was excluded via .gitignore

## /output
- I set up the output file path to this folder and you can see all the sample output from my scripts.

## /requirements.txt
- This folder has all the packages that are needed for this assignment

## /Scripts
- This foldere contains all of my python scripts for each codex

# /utils/common_functions.py
- Contains 1 common function mentionedin Professor Hants' repository

## trouble shooting and issues I ran into:
- I forgot to add in asterisks in front of .txt, .xml, .csv,  and .zip, which prevented me from pushing my commits for some of the larger files
- I also continued to run into the issue of not being able to git push after creating my snomed_small output. My terminal said that the file size is too large (178MB) which exceeds Github's 100MB limit. I changed the code so that n=1000. I checked the output again in my Mac's finder and the file size is only 50KB. HOwever, my terminal was insistent that the file is too large. I trouble shoot this for several hours over a span of 2 days by myself and also with Mo. There were many steps taken that I honestly cannot remember and I got pretty lost because Mo tried a lot of functions in the terminal that I am not familiar with; I at that point was just following his instructions on what to run in my terminal to try to resolve this issue.
- I could not run my npi_processor.py. I wrote comments within the script as to why and what issues i ran into. I tried resolving it many ways, including meeting with Mo but he was also unsure. My terminal continued to say zsh: killed every time I tried to fix something and run the code. Unfortunately, there is not a successful output file for this script, but I tried my best.

## takeaways
- I clearly understood the objective of this assignment. However, I think as someone with zero prior technical experience (purely clinical), it was really difficult to navigate VS Code and perform this assignment efficiently because I do not yet have a solid foundation to build off of. It was quite overwhelming and frustrating at times trying to juggle finishing this assignment, full time work, and keeping up with lecture slides. Although I was not able to create an output for all input files, I did become a little more familiar with VS Code and Python.
- Please note that I started this repository/assignment on 9/4/25. However, when I ran into the issue of not being to git push after working on snomed_small, Mo suggested that I delete the repository completely on 9/11/25 and cloning it again. Therefore, the timestamp of changes I made are not accurate.