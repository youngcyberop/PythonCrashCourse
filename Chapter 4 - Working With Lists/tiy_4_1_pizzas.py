#   print(variable[-1]) prints the last item in a list
#   Chapter 4
#       For loops
#           Syntax: for <item> in <items>:
#                       do this
#           "For every magician in list magicians, do this"
#           Consider using "For every 'item' in 'items' syntax

'''4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store
these pizza names
    in a list, and then use a for loop to print the name of each pizza.
        • Modify your for loop to print a sentence using the name of the
        pizza instead of
            printing just the name of the pizza. For each pizza you should
            have one line of
            output containing a simple statement like I like pepperoni pizza.
        • Add a line at the end of your program, outside the for loop,
        that states how much you
            like pizza. The output should consist of three or more lines
            about the kinds of
            pizza you like and then an additional sentence, such as I really
            love pizza!'''
print("\n*******************************************************")
print("4-1 Pizzas")
print("*******************************************************")
pizzas = ["pepperoni", "bacon", "banana peppers"]
for pizza in pizzas:
    print(f"I like {pizza} pizza!")
