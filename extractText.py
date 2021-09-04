import os
from fnmatch import fnmatch

root = 'dart-files'
pattern = "*.dart"

allFiles = []

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            filePath = os.path.join(path, name)
            allFiles.append(filePath)

print(allFiles)

extractedText = []


def extractText_pattern1(wholeText):
    index = 0
    startingIndex = 0
    endingIndex = 0
    state = 0  # nothing found yet

    for c in wholeText:
        if state == 0:  # nothing found yet
            if c == 't':
                state = 1  # first t found
                #print('t found')
            index = index + 1
            continue
        if state == 1:
            if c == 'e':
                state = 2  # e found.
                #print('e found')
            else:
                state = 0
            index = index + 1
            continue
        if state == 2:
            if c == 'x':
                state = 3  # x found.
                #print('x found')
            else:
                state = 0
            index = index + 1
            continue
        if state == 3:
            if c == 't':
                #print('t found')
                state = 4  # second t found.
            else:
                state = 0
            index = index + 1
            continue
        if state == 4:
            if c == ':':
                #print(': found')
                state = 5  # separator colon found.
            elif c == ' ' or c == '\t':
                #print('space found')
                pass
            else:
                state = 0
            index = index + 1
            continue
        if state == 5:
            if c == '\'':  # first quote found.
                #print('quote found')
                startingIndex = index + 1
                endingIndex = index + 1
                state = 6  #
            elif c == ' ' or c == '\t':
                pass
            else:
                state = 0

            index = index + 1
            continue

        if state == 6:
            if c == '\'':  # second quote found.
                #print('quote found again')
                #print(startingIndex)
                #print(endingIndex)

                if endingIndex - startingIndex == 1:
                    extractedText.append('')
                else:
                    extractedText.append(wholeText[startingIndex:endingIndex +
                                                   1])
                state = 0

            elif c >= ' ' and c <= 'z':
                #print('char found')
                endingIndex = index
            else:
                state = 0

            index = index + 1
            continue


def extractText_pattern2(wholeText):
    index = 0
    startingIndex = 0
    endingIndex = 0
    state = 0  # nothing found yet

    for c in wholeText:
        if state == 0:  # nothing found yet
            if c == 'T':
                state = 1  # first t found
                #print('T found')
            index = index + 1
            continue
        if state == 1:
            if c == 'e':
                state = 2  # e found.
                #print('e found')
            else:
                state = 0
            index = index + 1
            continue
        if state == 2:
            if c == 'x':
                state = 3  # x found.
                #print('x found')
            else:
                state = 0
            index = index + 1
            continue
        if state == 3:
            if c == 't':
                #print('t found')
                state = 4  # second t found.
            else:
                state = 0
            index = index + 1
            continue
        if state == 4:
            if c == '(':
                #print('( found')
                state = 5  # separator colon found.
            elif c == ' ' or c == '\t':
                #print('space found')
                pass
            else:
                state = 0
            index = index + 1
            continue
        if state == 5:
            if c == '\'':  # first quote found.
                #print('quote found')
                startingIndex = index + 1
                endingIndex = index + 1
                state = 6  #
            elif c == ' ' or c == '\t':
                pass
            else:
                state = 0

            index = index + 1
            continue

        if state == 6:
            if c == '\'':  # second quote found.
                #print('quote found again')
                #print(startingIndex)
                #print(endingIndex)

                if endingIndex - startingIndex == 1:
                    extractedText.append('')
                else:
                    extractedText.append(wholeText[startingIndex:endingIndex +
                                                   1])

                state = 0

            elif c >= ' ' and c <= 'z':
                #print('char found')
                endingIndex = index
            else:
                state = 0

            index = index + 1
            continue


for f in allFiles:
    dartFile = open(f)
    wholeText = dartFile.read()
    extractText_pattern1(wholeText)
    extractText_pattern2(wholeText)

print(extractedText)
