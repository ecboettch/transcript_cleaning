# transcript_cleaning
Formats automated transcripts according to local requirements

Scripts work in Python 2.7 so it can run on any Mac. Small changes can be made for it to run with Python 3.

ZoomTranscriptCleaner: This script takes a Zoom transcript (NameOfFile.vtt) and outputs a cleaned version (NameOfFileClean.txt). 
* Based on a dictionary supplied by the researcher (replacements), fixes common mistranscriptions
* Removes timestamps
* Removes line breaks between consecutive lines spoken by same person
* Based on a list of names supplied by the researcher (team), swaps out each name for <INTERVIEWER> or <INTERVIEWEE>. If a name is not found in the list team, including if the team is empty, the script will ask the person running it whether the name is an interviewer. Enter the string 'yes' to code that name as <INTERVIEWER>; enter any other string for it to be coded as <INTERVIEWEE>.
* Where ther are multiple interviewers or interviewees, numbers interviewers or interviewees as <INTERVIEWER-1>, <INTERVIEWER-2> based on who speaks first
  
AbbrevCleaner: This script takes a text file (NameOfFile.txt) and outputs a new file (NameOfFileAbbrev.txt) and a list of unrecognized abbreviations. It capitalizes interviewer lines and spells out recognized abbreviations in brackets. 

* Uppercases all interviewer statements
* Spells out acronyms and abbreviations based on dictionary supplied by researcher (replacements). Performs some basic stemming to detect plurals and possessives.
* Prints list of unknown abbreviations, defined as a string containing at least two capital letters. (False positives do occur frequently.)

  
TeamsTranscriptCleaner: This script takes a Teams transcript and outputs a cleaned version.
* Combines consecutive lines from the same speaker
* Removes timestamps
* Does not fix mistranscriptions or substitute speaker names
