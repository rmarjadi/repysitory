#Riza Marjadi
"""Assignment 2-Problem 3: Check a string pattern
to match Murray State course number"""

print('This program will check if the string you enter matches Murray State\'s course number pattern.\n')

def checkCourse():
    import re

    courseSearch=input('Check if it is a Murray State\'s course: ')
    courseRegex = re.compile(r'''(
        ([a-zA-Z]{3})
        ([ -]*)
        (\d{3})
        $
        )''', re.VERBOSE)
    
    matches = []

    for match in courseRegex.findall(courseSearch):
        matches.append(match[0])

    if len(matches) > 0:
        print('That matches a pattern similar to Murray State\'s course number.')
    else:
        print('That is not a Murray State\'s course number.')

more="y"
while more=="y":
    checkCourse()
    more=str(input("\nDo you want to check more string pattern? (y/n): "))

    

    
