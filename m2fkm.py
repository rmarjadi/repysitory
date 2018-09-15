"""Miles to feet and kilometer Conversion
Riza Marjadi"""

print("This program will convert a distance value in miles to feet and kilometers")
    
more="y"
while more=="y":
    while True:
        try:
            d=float(input("\nEnter the distance value in mile(s): "))
            break
        except ValueError:
            print("\nInvalid value! Please enter a numerical value.")
        
    print(str(d) + ' mile(s) is equal to ' + str(d*5280) + " feet\n or " + str(d*1.609344) + " kilometers")
    more=str(input("\nDo you want to convert more distance values? (y/n): "))
