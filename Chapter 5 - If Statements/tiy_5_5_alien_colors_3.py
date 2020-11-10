'''
 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an
 if-elif-else chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed
for the appropriate color alien.
'''

print("\n*******************************************************")
print("5-5 Alien Colors #3")
print("*******************************************************")

alien_color = "red"
if alien_color == "red":
    print("Your alien color is red")
else:
    print("Your alien color is not red")

# • If the alien is green, print a message that the player earned 5 points.
if alien_color == "green":
    print("You earned 5 points")
# • If the alien is yellow, print a message that the player earned 10 points.
elif alien_color == "yellow":
    print("You earned 10 points")
#• If the alien is red, print a message that the player earned 15 points.
else:
    print("You earned 15 points")
