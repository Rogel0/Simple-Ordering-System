print("\nHi, Welcome to Gerodiaz Coffee shop!!!")

name = input("\nWhat is your name?: ")

print("Hello " + name + ", thank you so much for coming in today.\n\n")

menu = "Black Coffee,Espresso, Latte, Cappucino"

print(name + ", what would you like to order? Here is what we are serving.\n" + menu)

order = input()

print("\nHow many " + order + " do you like?")

quantity_order = int(input())

print("\nSounds good, " + name + " We have that " + order + ", Just wait for your " + str(quantity_order) + " " + order)











