from calculator import calculator  # import class calculator from caalculator.py 
cal = calculator()          # create new Object of class calculator   

print(cal.addition(7,5))
print(cal.substract(34,21))
print(cal.multiply(54,2))
print(cal.divide(144,2))
print(cal.divide(45,0))

import shopping
spadacard = shopping.Shopping_card()

spadacard.add_item("Birne", 10)
spadacard.add_item("Apfel", 9)
spadacard.add_item("Mango", 4)
spadacard.display_card()
spadacard.remove_item("Apfel")

spadacard.calculate




