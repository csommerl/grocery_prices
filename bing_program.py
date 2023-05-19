import argparse
import json
import os


def view_prices(item):
    with open("grocery.json") as f:
        data = json.load(f)
    if item in data:
        for store, price in data[item].items():
            print(f"{store}: {price}")
    else:
        print(f"{item} not found.")

def log_price(item, store, price):
    if not os.path.exists("grocery.json"):
        with open("grocery.json", "w") as f:
            json.dump({}, f)
    with open("grocery.json") as f:
        data = json.load(f)
    if item in data:
        data[item][store] = price
    else:
        data[item] = {store: price}
    with open("grocery.json", "w") as f:
        json.dump(data, f)
    print(f"Price of {item} at {store} is now {price}.")


def interface():
    while True:
        command = input("Enter command (view or log): ")
        if command == "view":
            item = input("Enter item: ")
            view_prices(item)
        elif command == "log":
            item = input("Enter item: ")
            store = input("Enter store: ")
            price = float(input("Enter price: "))
            log_price(item, store, price)
        else:
            print("Invalid command.")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Log and view prices for grocery items at different stores.")
    parser.add_argument("command", help="view or log", nargs="?")
    parser.add_argument("item", help="grocery item", nargs="?")
    parser.add_argument("--store", help="store name")
    parser.add_argument("--price", type=float, help="price")

    args = parser.parse_args()

    if args.command == "view":
        view_prices(args.item)
    elif args.command == "log":
        if not args.store or not args.price:
            print("Please specify store and price.")
        else:
            log_price(args.item, args.store, args.price)
    else:
        interface()