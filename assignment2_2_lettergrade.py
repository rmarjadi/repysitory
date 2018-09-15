#Riza Marjadi
"""Assignment 2-Problem 2: Letter grad
Converting a numeric grade into a standard letter grade"""

print('This program will convert a numeric grade into a standard letter grade.\n')

letterMin={'D':70, 'C':80, 'B':90, 'A':100}

def letterGrade(numGrade):
    for grade in letterMin:
        if numGrade < float(letterMin[grade]):
            return grade
            break
                
more="y"
while more=="y":
    while True:
        try:
            numGrade=float(input("\nEnter a numeric grade: "))
            break
        except ValueError:
            print("\nInvalid value! Please enter a numerical value.")

    print('The letter grade is: ' + letterGrade(numGrade))
    more=str(input("\nDo you want to convert more grades? (y/n): "))

