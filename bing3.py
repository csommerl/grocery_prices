import json

def log_price():
    item_name = input("Enter item name: ")
    store_name = input("Enter store name: ")
    quantity = float(input("Enter quantity in ounces: "))
    price = float(input("Enter price: "))

    with open('prices.json', 'r') as f:
        data = json.load(f)

    if item_name not in data:
        data[item_name] = {}

    data[item_name][store_name] = round(price / quantity, 2)

    with open('prices.json', 'w') as f:
        json.dump(data, f)

def view_price():
    item_name = input("Enter item name: ")

    with open('prices.json', 'r') as f:
        data = json.load(f)

    if item_name not in data:
        print(f"{item_name} not found.")
        return

    print(f"Price per ounce of {item_name}:")
    for store_name, price_per_ounce in data[item_name].items():
        print(f"{store_name}: ${price_per_ounce:.2f}")

def main():
    while True:
        choice = input("(l)og or (v)iew? ")

        if choice == 'l':
            log_price()
        elif choice == 'v':
            view_price()
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()

