print("Hello, Welcome to NetworkChuck Coffee")

name = input("What is the name for your order? ")

print(f"Welcome {name}, thanks so much for stopping in today!\n")
menu = {'Black Coffee': '2$',
        'Latte': '4$',
        'Expresso': '4$',
        'Cappucino': '3$'}

print("Here is our menu, I'll give you a minute to look it over.")
print(menu)
print("\n\n")
answer = input("Have you decided on what you would like this morning?\n")
if answer == 'yes':
    order = input("Ok hun, what will it be? ")
    if order == "Black Coffee":
        print(
            f'Ok that will be 1 {order}, thanks so much, it will be right out!')
    elif order == "Latte":
        print(
            f"We sell {order}'s all the time, you will be impressed with our blend!")
    elif order == "Expresso":
        print(f"One {order}, coming right up!")
    elif order == "Cappucino":
        print(
            f"Good choice, {order} is my favorite too! It will only be a minute!")
    else:
        print("Im sorry we don't serve that. Have a nice day! ")
elif answer == "no":
    print("Ok I\'ll give you more time.. ")

print("Ok, it'll be about 5 minutes..")

lovely_loveseat_description = (
    'Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or White.')
lovely_loveseat_price = 254.00
stylish_settee_description = (
    'Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black')
stylish_settee_price = 180.50
luxurious_lamp_description = (
    'Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.')
luxurious_lamp_price = 52.15
sales_tax = .088
customer_one_total = 0
