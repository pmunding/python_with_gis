

# create class calculator with the default operations
class calculator:
    # Substract
    def substract(self, a, b):
        return a - b 

    #addition
    def addition(self, a, b):
        return a + b

    #multiply 
    def multiply(self, a, b):
        return a * b

    #divide
    def divide(self, a, b):
        if (b == 0):
            return "cant divide by zero"
        else:
            return a / b

