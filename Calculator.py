# ----- Classes -----

# Defining A Class For All Items
class Item:

    # Initializing All Inputs Of The Item
    def __init__(self, name, price, imported, exempted, quantity = 1):
        self.name = name
        self.price = price
        self.imported = imported
        self.exempted = exempted
        self.quantity = quantity
        self.sales_tax = 0.1
        self.import_tax = 0.05

    # Defining A Function For Returning Total Tax On An Item
    def get_tax(self):
        tax = 0
        total_tax_rate = 0
        if self.quantity > 1:
            self.price *= self.quantity 
        if not(self.exempted):
            total_tax_rate += self.sales_tax 
        if self.imported:
            total_tax_rate += self.import_tax 
        tax = self.price * total_tax_rate
        if str(tax).split(".")[1][1:3] == "25":
            tax = float(str(tax).split(".")[0] + "." + str(tax).split(".")[1][0] + "50")
        elif str(tax).split(".")[1][1:3] == "75":
            tax = float(str(tax).split(".")[0] + "." + str(int(str(tax).split(".")[1][0])+1))
        else:
            tax = round(tax / 0.05) * 0.05
        return tax
    
# Defining A Class For The Receipt
class Receipt:
    
    # Initializing The List Of Items
    def __init__(self, items):
        self.items = items

    # Defining A Function For Returning A Receipt Of All Items
    def get_receipt(self):
        total_tax = 0
        total_price = 0
        receipt = ""
        for item in self.items:
            tax = item.get_tax()
            item.price += tax
            item.price = float(str(item.price).split(".")[0] + "." +  str(item.price).split(".")[1][:2])
            total_tax += tax
            total_price += item.price
            receipt += f"{item.quantity} {item.name}: {item.price}\n"
        receipt += f"Sales Tax: {total_tax}\nTotal: {total_price}"
        return receipt
