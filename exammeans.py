"""Mean of 5 exam scores
Riza Marjadi"""

from statistics import mean
i=0
scores=[]

while i < 5:
    while True:
        try:
            s = float(input("\nEnter exam score " + str(i+1) +", between 0 to 100: "))
            if s < 0 or s > 100:
                raise ValueError
            else:
                break
        except ValueError:
            print("\nInvalid Value! Please enter a number between 0 to 100")
            
    scores.append(s)
    i+=1

#combination of lines 24 & 25 or just line 27 will print the same result

average_score = round(mean(scores), 3)
print("\nThe average exam score is " + str(average_score))

#print("\nThe average exam score is " + "{:.2f}".format(mean(scores)))
