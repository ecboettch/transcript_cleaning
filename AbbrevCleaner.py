__author__ = 'eboettch'

import re # get regular expressions

# find and replace function

replacements = {}

#replacements = {" EHR": "[electronic health record]"}
errors = replacements.keys()


def fixerror(line):
    for e in errors:
        line = line.replace(e + " ",(e + " " + replacements.get(e)+" ")) #append a space
        line = line.replace(e + ".", (e + " " + replacements.get(e) + "."))
        line = line.replace(e + ",", (e + " " + replacements.get(e) + ","))
        line = line.replace(e + "s ", (e + "s " + replacements.get(e) + " "))
	line = line.replace(e + "?", (e + " " + replacements.get(e) + "?"))
    return line

newabbrevs = []

def newabbrev(line):
    stripchar = [".", ",", "s"]
    listofwords = line.split()
    # print(listofwords)
    i = 0
    # print (len(listofwords))
    while i < len(listofwords):
        word = listofwords[i]
        # print (listofwords[i])
        i = i+1
        # see if it's an abbreviation: does it contain multiple capital letters
        if re.search('.*[A-Z].*[A-Z]',word):
        #if re.match('.*[A-Z]*.*[A-Z].*',word):
            # strip space, period, comma, apostrophe s, s
            for s in stripchar:
                word = word.rstrip(s)
            # look for word in your keys/stuff to ignore
            if (" " + word) not in errors and word[0] != "<" and word not in newabbrevs:
                word = word.lstrip(" ")
                newabbrevs.append(word)


#gets file from user
clutterFile = input("What file do you want to clean?")
# interviewee = input("How does the interviewee's name appear in the file?")
file = open(clutterFile, 'r')

#all the lines of the thing in a list, called data
data = file.readlines()
file.close()


new = []
newline = ""
# prevSpeaker=""
for line in data:
    # look for abbreviations & replace
    if line[1].isalpha():
        line = fixerror(line)
        newabbrev(line)
        if line[:12] == "<INTERVIEWER":
            # print (line[:12])
            line = line.upper()
            # print (line[:12])
    new.append(line)
    # print(line)
print (newabbrevs)


filename = clutterFile[0:len(clutterFile)-4]
nameofnewfile = filename + "Abbrev.txt"
# writes to a new file
file1 = open(nameofnewfile, "w")
for line in new:
    file1.write(line)
