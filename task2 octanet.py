import datetime

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


class Receipt:
    def __init__(self, tax_rate=0.05, discount_rate=0.10):
        self.items = []
        self.tax_rate = tax_rate
        self.discount_rate = discount_rate
        self.subtotal = 0
        self.tax = 0
        self.discount = 0
        self.final_total = 0

    def add_item(self, item):
        self.items.append(item)

    def calculate_totals(self):
        self.subtotal = sum(item.total_price() for item in self.items)
        self.tax = self.subtotal * self.tax_rate
        self.discount = self.subtotal * self.discount_rate
        self.final_total = self.subtotal + self.tax - self.discount

    def display_receipt(self):
        print("Receipt:")
        print(f"{'Item':20} {'Price':10} {'Quantity':10} {'Total':10}")
        print("-" * 50)
        for item in self.items:
            print(f"{item.name:20} {item.price:10.2f} {item.quantity:10} {item.total_price():10.2f}")
        print("-" * 50)
        print(f"Subtotal: {self.subtotal:.2f}")
        print(f"Tax: {self.tax:.2f}")
        print(f"Discount: {self.discount:.2f}")
        print(f"Final Total: {self.final_total:.2f}")
        print("-" * 50)

    def save_receipt(self, filename="receipt.txt"):
        with open(filename, 'w') as file:
            file.write("Receipt:\n")
            file.write(f"{'Item':20} {'Price':10} {'Quantity':10} {'Total':10}\n")
            file.write("-" * 50 + "\n")
            for item in self.items:
                file.write(f"{item.name:20} {item.price:10.2f} {item.quantity:10} {item.total_price():10.2f}\n")
            file.write("-" * 50 + "\n")
            file.write(f"Subtotal: {self.subtotal:.2f}\n")
            file.write(f"Tax: {self.tax:.2f}\n")
            file.write(f"Discount: {self.discount:.2f}\n")
            file.write(f"Final Total: {self.final_total:.2f}\n")
            file.write("-" * 50 + "\n")
        print(f"Receipt saved to {filename}")

# Sample usage
def main():
    receipt = Receipt()

    while True:
        name = input("Enter item name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        try:
            price = float(input(f"Enter price for {name}: "))
            quantity = int(input(f"Enter quantity for {name}: "))
        except ValueError:
            print("Invalid input, please enter numbers for price and quantity.")
            continue
        
        item = Item(name, price, quantity)
        receipt.add_item(item)

    receipt.calculate_totals()
    receipt.display_receipt()
    
    save = input("Do you want to save the receipt? (yes/no): ").lower()
    if save == 'yes':
        receipt.save_receipt()

if __name__ == "__main__":
    main()
