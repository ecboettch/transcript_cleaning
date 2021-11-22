__author__ = 'eboettch'

# find and replace function
def fixerror(line):
    # updated 8/16/2021 based on 03, 04
    # replacements = {" cobra":" COVID"}
    replacements = {}
    errors = replacements.keys()
    """
    i = 0
    while i<len(line):
        for e in errors: #for each pair in the dictionary
            if line.find(e) != -1: # look for each key in the line
                i = line.find(e) # jump i to the index of the thing you found, to reduce the number of checks of the line
                line = line.replace(e,replacements.get(e)) # replace the key with its value
        i=i+1
    """
    for e in errors:
        line = line.replace(e,replacements.get(e))
        # another way to control this is to append a space, a comma, and a period to e and e's replacement
    return line



#gets file from user
clutterFile = input("What file do you want to clean?")
# interviewee = input("How does the interviewee's name appear in the file?")
file = open(clutterFile, 'r')

#all the lines of the thing in a list, called data
data = file.readlines()
file.close()


def findSpeaker(line):
    speakerend = line.find(":")
    speaker = line[0:speakerend]
    return speaker

def identSpeaker (speaker1,speaker2):
    if speaker1==speaker2:
        return True
    else:
        return False

def removeSpeaker (line, speaker):
    noSpeaker = line[len(speaker)+1:len(line)]
    return noSpeaker

# team = ['Jane Researcher', 'Joe Interviewer']
team = [] # fill in with everyone's actual names
interviewers = []
#interviewees = [interviewee]
interviewees =[]

def cleanSpeaker(line, speaker):
    # handle what happens if speaker is not interviewee or in team
    if speaker not in interviewees + team:
        question = "Is " + speaker + " an interviewer? Type yes if so"
        if speaker == "": # putting this in to check where this is firing
            print(line)
        newSpeaker = str(input(question))
        if newSpeaker == 'yes':
            team.append(speaker)
        else:
            interviewees.append(speaker)
    # handling for interviewer
    if speaker in team:
        if speaker in interviewers:
            number = interviewers.index(speaker) +1
        else:
            interviewers.append(speaker)
            number = interviewers.index(speaker) + 1
        line = line.replace(speaker, "<INTERVIEWER-" + str(number) +">")
        # line = line.upper() #commenting this out to move the capitalization function to a later script
    else:
        number = interviewees.index(speaker) + 1
        line = line.replace(speaker, "<INTERVIEWEE-"+ str(number)+">")
    return line


new = []
newline = ""
prevSpeaker=""
for line in data:
    #if data.index(line) > start:

    # this is new

    if line[0].isalpha() == True and line.find(":") < 0 and line[:6] != "WEBVTT": # if it's dialogue (alpha) but no speaker (no colon), treat as
        newline = newline[0:len(newline) - 2]            # identical to previous speaker
        newline = newline + " "+ line
        # print(line[:6])
    if line[0].isalpha() == True and line.find(":") > -1: #check that this is a line of dialogue
         # find speaker
        speaker = findSpeaker(line)
         # is this the same as previous speaker?
         # yes, combine the lines
        if identSpeaker(speaker,prevSpeaker) == True:
            # trim the carriage return from the line you've been amassing
            newline=newline[0:len(newline)-2]
            # combine the line you've been amassing with the line from the data, minus the speaker
            newline = newline + removeSpeaker(line,speaker)
        else:
            # clean the line you've been amassing, fix its speaker, add it to the file,
            # check if interviewee
            """
            if prevSpeaker != interviewee:
                newline = newline.upper()
                """
            if len(newline) > 0:
                newline = fixerror(newline)
                newline = cleanSpeaker(newline, prevSpeaker)
            # write the old line
            #new.append(newline + "\n")
            new.append(newline) # creating a version of this which doesn't have a hard return between speakers
            # start amassing the new line
            newline = line
            prevSpeaker = speaker
# add the last line - needs to do all the other things you did previously
newline = fixerror(newline)
newline = cleanSpeaker(newline, prevSpeaker)
new.append(newline)

# don't number the interviewers, interviewees if there's only one of them
i = 0
while i < len(new):
    if len(interviewees)==1:
        new[i] = new[i].replace("INTERVIEWEE-1", "INTERVIEWEE")
    if len(interviewers)==1:
        new[i] = new[i].replace("INTERVIEWER-1", "INTERVIEWER")
    i=i+1

filename = clutterFile[0:len(clutterFile)-4]
nameofnewfile = filename + "Clean.txt"
# writes to a new file
file1 = open(nameofnewfile, "w")
for line in new:
    file1.write(line)
