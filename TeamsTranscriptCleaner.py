__author__ = 'eboettch'

import re



#gets file from user
clutterFile = input("What file do you want to clean?")
# interviewee = input("How does the interviewee's name appear in the file?")
file = open(clutterFile, 'r')

#all the lines of the thing in a list, called data
data = file.readlines()
file.close()



new = []
newline = ""
prevSpeaker=""
d = 0
while d < len(data):
    line = data[d]
    if re.match('[0-9][0-9]:',line[0:3]):
        speaker = data[d+1]
        text = data[d+2]
        text = text.strip('\n')
        if speaker == prevSpeaker: # if it's the same speaker, append it to the line you're working on
            newline=newline+text
        else:
            # write the old line
            oldline = prevSpeaker.rstrip('\n') + ": " + newline + '\n\n'
            new.append(oldline)
            # start a new line
            newline = text
            prevSpeaker = speaker
        d = d+3
    else:
        d = d+1



oldline = prevSpeaker.rstrip('\n') + ": " + newline
new.append(oldline)



filename = clutterFile[0:len(clutterFile)-4]
nameofnewfile = filename + "Clean.txt"
# writes to a new file
file1 = open(nameofnewfile, "w")
for line in new:
    file1.write(line)
