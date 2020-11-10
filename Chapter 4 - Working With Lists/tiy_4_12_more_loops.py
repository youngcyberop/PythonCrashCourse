'''
4-12. More Loops: All versions of foods.py in this section have avoided
using for loops when printing to save space.
Choose a version of foods.py, and write two for loops to print each list of
foods.
'''
print("\n*******************************************************")
print("4-12 More Loops")
print("*******************************************************")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
# Choose a version of foods.py, and write two for loops to print each list
# of foods.
for food in my_foods:
    print(food)
for food in friend_foods:
    print(food)
