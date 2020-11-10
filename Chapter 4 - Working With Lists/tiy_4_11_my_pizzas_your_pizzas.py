'''
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (
page 56). Make a copy of the list of pizzas,
    and call it friend_pizzas. Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite
pizzas are:, and then use a for loop to print
the first list. Print the message My friend’s favorite pizzas are:, and then
use a for loop to print the sec- ond list.
Make sure each new pizza is stored in the appropriate list.
'''
print("\n*******************************************************")
print("4-11 My pizzas, your pizzas")
print("*******************************************************")
#   My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page
#   56). Make a copy of the list of pizzas,
#     and call it friend_pizzas. Then, do the following:
pizzas = ["pepperoni", "bacon", "banana peppers"]
friends_pizzas = pizzas[:]
#   • Add a new pizza to the original list.
pizzas.append("sausage")
#   • Add a different pizza to the list friend_pizzas.
friends_pizzas.append("ham")
#   • Prove that you have two separate lists. Print the message My favorite
#   pizzas are:, and then use a for loop to
#   print the first list. Print the message My friend’s favorite pizzas
#   are:, and then use a for loop to print the
#   sec- ond list. Make sure each new pizza is stored in the appropriate list.
print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"{pizza}")
print("My friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(f"{pizza}")
