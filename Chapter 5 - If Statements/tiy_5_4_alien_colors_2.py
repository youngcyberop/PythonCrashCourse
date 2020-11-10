'''
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3,
and write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned
5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just
earned 10 points.
• Write one version of this program that runs the if block and another that
runs the else block.
'''

print("\n*******************************************************")
print("5-4 Alien Colors #2")
print("*******************************************************")

# Choose a color for an alien as you did in Exercise 5-3,
# and write an if-else chain.
alien_color = "red"
if alien_color == "red":
    print("Your alien color is red")
else:
    print("Your alien color is not red")

# • If the alien’s color is green, print a statement that the player just
# earned 5 points for shooting the alien.
if alien_color == "green":
    print("You just earned 5 points")

# • If the alien’s color isn’t green, print a statement that the player just
# earned 10 points.
if alien_color != "green":
    print("You just earned 10 points")

# • Write one version of this program that runs the if block and another that
# runs the else block.
if alien_color == "green":
    print("You win the game")
else:
    print("You lose the game")
