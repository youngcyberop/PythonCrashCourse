'''
3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end
of your program stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still
in your list.
'''

# • Start with your program from Exercise 3-4. Add a print() call at the end
#   of your program stating the name of the guest who can’t make it.
guests = ['george washington', 'denzel washington', 'martha bush']
print(f"Welcome {guests[0].title()} to dinner.")
print(f"Welcome {guests[1].title()} to dinner.")
print(f"Welcome {guests[2].title()} to dinner.")
print(f"\nGuest {guests[1].title()} will be unable to attend dinner.")

# • Modify your list, replacing the name of the guest who can’t make it with
#   the name of the new person you are inviting.
removed_guest = guests.pop(1)
guests.insert(1, 'michael moore')
print(f"\n{guests[1].title()} will take {removed_guest.title()}'s place at dinner")

# • Print a second set of invitation messages, one for each person who is still
#   in your list.
print(f"\nWelcome {guests[0].title()} to dinner.")
print(f"Welcome {guests[1].title()} to dinner.")
print(f"Welcome {guests[2].title()} to dinner.")
