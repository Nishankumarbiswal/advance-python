products = {
    "101": ("Rice", 50),
    "102": ("Milk", 25),
    "103": ("Bread", 30),
    "104": ("Eggs", 60)
}

cart = []

def add_product():
    code = input("Enter product code: ")

    if code in products:
        qty = int(input("Quantity: "))
        name, price = products[code]
        cart.append((name, price, qty))
    else:
        print("Product not found")

def generate_bill():
    total = 0

    print("\n----- BILL -----")
    for name, price, qty in cart:
        cost = price * qty
        total += cost
        print(name, qty, cost)

    discount = total * 0.1 if total > 200 else 0
    final = total - discount

    print("Total:", total)
    print("Discount:", discount)
    print("Payable:", final)

while True:
    print("\n1.Add Product\n2.Generate Bill\n3.Exit")
    choice = input("Choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        generate_bill()
    else:
        break