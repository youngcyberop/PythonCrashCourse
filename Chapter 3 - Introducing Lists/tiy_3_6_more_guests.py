'''
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
call to the end of your program informing people that you found a bigger
dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
'''

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
