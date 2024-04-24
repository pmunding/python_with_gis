
# class shopping card
class Shopping_card:

    # items on the card
    def __init__(self):
        self.items = []

    #function to add items
    def add_item(self, item_name, quantity):
        new_item = Item(item_name, quantity)   #creating new Item
        self.items.append(new_item)            #add new_Item to Card

    # display all items
    def display_card(self):        
        for Item in self.items:
            print(f"{Item.name} Menge: {Item.quantity}")

    # remove items
    def remove_item(self, x):
        for Item in self.items:
            if Item.name == x:
                self.items.remove(Item)
                print(f"Removed {x}. Now your card contains:")
                self.display_card()
                self.calculate()

    
    # sum the total quantity of all Items 
    def calculate(self):
        sum = 0
        for Item in self.items:
            sum = sum + Item.quantity

        print(f"the total quantity of all Items is {sum}")



# class items
class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


# testing classes and Functions

spadacard = Shopping_card()
spadacard.add_item("Birne", 10)
spadacard.add_item("Apfel", 9)
spadacard.add_item("Mango", 4)
spadacard.display_card()
spadacard.remove_item("Apfel")


    