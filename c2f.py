"""Celsius to Fahrenheit Conversion
Riza Marjadi"""

print("This program will convert a temperature value in Celsius to Fahrenheit")
    
more="y"
while more=="y":
    while True:
        try:
            t=float(input("\nEnter the temperature value in Celsius: "))
            break
        except ValueError:
            print("\nInvalid value! Please enter a numerical value.")

    print(str(t) + ' degree Celsius is converted to ' + str(9/5*t+32) +" degree Fahrenheit")
    more=str(input("\nDo you want to convert more values? (y/n): "))
