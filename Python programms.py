def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * discount_percent / 100
        return price - (price * discount_percentage / 100)
    else:
        return price


price = float(input("Enter the price: "))
discount_percent = float(input("Enter the discount percent: "))
final_price = calculate_discount(price, discount_percent)

if final_price == price:
    print("You don't have a discount, your final price is:", final_price)
else:
    print(f" You are eligible to a discount, your final price is: {final_price}")


