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

def log_price(item, store, price, ounces):
    if not os.path.exists("grocery.json"):
        with open("grocery.json", "w") as f:
            json.dump({}, f)
    with open("grocery.json") as f:
        data = json.load(f)
    if item in data:
        data[item][store] = {"price": price, "ounces": ounces}
    else:
        data[item] = {store: {"price": price, "ounces": ounces}}
    with open("grocery.json", "w") as f:
        json.dump(data, f)
    print(f"Price of {item} at {store} is now {price} for {ounces} ounces.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Log and view prices for grocery items at different stores.")
    parser.add_argument("command", help="v for view or l for log", nargs="?")
    parser.add_argument("item", help="grocery item", nargs="?")
    parser.add_argument("--store", help="store name")
    parser.add_argument("--price", type=float, help="price")
    parser.add_argument("--location", help="location of store")
    parser.add_argument("--ounces", type=float, help="ounces")

    args = parser.parse_args()

    if args.command == "v":
        view_prices(args.item)
    elif args.command == "l":
        if not args.store or not args.price or not args.location or not args.ounces:
            print("Please specify store, price, location and ounces.")
        else:
            log_price(args.item, args.store, args.price, args.ounces)
            print(f"Store location: {args.location}")
    else:
        while True:
            command = input("Enter command (v or l): ")
            if command == "v":
                item = input("Enter item: ")
                view_prices(item)
            elif command == "l":
                item = input("Enter item: ")
                store = input("Enter store: ")
                price = float(input("Enter price: "))
                location = input("Enter location: ")
                ounces = float(input("Enter ounces: "))
                log_price(item, store, price, ounces)
                print(f"Store location: {location}")
            else:
                print("Invalid command.")

