products = {
    "apple": 50,
    "banana": 30,
    "mango": 120,
    "orange": 80,
    "grapes": 200
}

for item,price in products.items():
    print(f" {item.capitalize()} RS. {price}" )

cart={}
total = 0
while True:

    choice=input("Enter product to buy or (Done)").lower()

    if choice == "done":
        break

    if choice in products:
        qty = input("Enter Quantity of Buy:")

        if qty.isdigit():
            qty = int(qty)
            cart[choice] = cart.get(choice,0)+qty
            print("Your product is Edit")
        else:
            print("invalid")
    else:
        print("your product is not avaible")


    for item,qty in cart.items():
        price = products[item]
    cost = price*qty
    total += cost
print(f"{item} and {qty} and total is {total}")