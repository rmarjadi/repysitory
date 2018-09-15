"""Convert integer to roman numerals
Riza Marjadi"""

def integer_to_roman(num):
    values = [
           1000, 900, 500, 400,
           100, 90, 50, 40,
           10, 9, 5, 4,
           1
           ]
    symbol = [
           "M", "CM", "D", "CD",
           "C", "XC", "L", "XL",
           "X", "IX", "V", "IV",
           "I"
           ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // values[i]):
            roman_num += symbol[i]
            num -= values[i]
        i += 1
    return roman_num


more = 'y'
while more == 'y':
    while True:
        try:
            integervalue = int(input("\nEnter an integer value from 0 to 10000: "))
            if integervalue < 0 or integervalue > 10000:
                raise ValueError
            else:
                break
        except ValueError:
            print("\nInvalid value! Please enter an integer value from 0 to 10000.")
        
    print("Roman numeric for " + str(integervalue) + " is: " + integer_to_roman(integervalue))
    
    more=str(input("\nMore? (y/n): "))


