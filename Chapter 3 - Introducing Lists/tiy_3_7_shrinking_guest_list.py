'''
3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
• Print a message to each of the two people still on your list, letting them
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.
'''

# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.

# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# call to the end of your program informing people that you found a bigger
# dinner table.
guests = ['george washington', 'denzel washington', 'martha bush']
print(f"Welcome {guests[0].title()} to dinner.")
print(f"Welcome {guests[1].title()} to dinner.")
print(f"Welcome {guests[2].title()} to dinner.")
print(f"\nHowever, a larger table has been found!")

# • Use insert() to add one new guest to the beginning of your list.
guests.insert(0, 'ed norton')

# • Use insert() to add one new guest to the middle of your list.
guests.insert(3, 'john wick')

# • Use append() to add one new guest to the end of your list.
guests.append('john adams')

# • Print a new set of invitation messages, one for each person in your list.
print(f"\nWelcome {guests[0].title()} to dinner.")
print(f"Welcome {guests[1].title()} to dinner.")
print(f"Welcome {guests[2].title()} to dinner.")
print(f"Welcome {guests[3].title()} to dinner.")
print(f"Welcome {guests[4].title()} to dinner.")
print(f"Welcome {guests[5].title()} to dinner.")

print(f"\nDue to unforseen circumstances, we will only be able to invite two to dinner.")

# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
removed_guest1 = guests.pop(5)
print(removed_guest1)
