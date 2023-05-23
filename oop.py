import json

class GroceryItem:
    def __init__(self, name):
        self.name = name
        self.stores = {}

    def add_price(self, store_name, quantity, price):
        if store_name not in self.stores:
            self.stores[store_name] = []

        self.stores[store_name].append((quantity, price))

    def get_price_per_ounce(self):
        result = {}
        for store_name, prices in self.stores.items():
            total_quantity = 0
            total_price = 0
            for quantity, price in prices:
                total_quantity += quantity
                total_price += price

            result[store_name] = round(total_price / total_quantity, 2)

        return result

class GroceryList:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name):
        if item_name not in self.items:
            self.items[item_name] = GroceryItem(item_name)

    def add_price(self, item_name, store_name, quantity, price):
        if item_name not in self.items:
            self.add_item(item_name)

        self.items[item_name].add_price(store_name, quantity, price)

    def get_price_per_ounce(self, item_name):
        if item_name not in self.items:
            return None

        return self.items[item_name].get_price_per_ounce()

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            data = {}
            for item_name, item in self.items.items():
                data[item_name] = item.stores

            json.dump(data, f)

    def load_from_file(self, filename):
        try:
            with open(filename) as f:
                data = json.load(f)
                for item_name, stores in data.items():
                    for store_name, prices in stores.items():
                        for quantity, price in prices:
                            self.add_price(item_name, store_name, quantity, price)
        except FileNotFoundError:
            pass

def main():
    grocery_list = GroceryList()
    grocery_list.load_from_file('prices.json')

    while True:
        choice = input("(l)og or (v)iew? ")

        if choice == 'l':
            item_name = input("Enter item name: ")
            store_name = input("Enter store name: ")
            quantity = float(input("Enter quantity in ounces: "))
            price = float(input("Enter price: "))

            grocery_list.add_price(item_name, store_name, quantity, price)
            grocery_list.save_to_file('prices.json')
        elif choice == 'v':
            item_name = input("Enter item name: ")
            prices = grocery_list.get_price_per_ounce(item_name)

            if prices is None:
                print(f"{item_name} not found.")
                continue

            print(f"Price per ounce of {item_name}:")
            for store_name, price_per_ounce in prices.items():
                print(f"{store_name}: ${price_per_ounce:.2f}")
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()

