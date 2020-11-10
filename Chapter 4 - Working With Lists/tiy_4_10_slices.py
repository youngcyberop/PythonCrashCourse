'''
4-10. Slices: Using one of the programs you wrote in this chapter,
add several lines to the
    end of the program that do the following:
    • Print the message The first three items in the list are:. Then use a
    slice to print the first
        three items from that program’s list.
    • Print the message Three items from the middle of the list are:. Use a
    slice to print three items
        from the middle of the list.
    • Print the message The last three items in the list are:. Use a slice
    to print the last three
        items in the list.
'''
print("\n*******************************************************")
print("4-10  Slices")
print("*******************************************************")
#   Using one of the programs you wrote in this chapter, add several lines
#   to the
#   end of the program that do the following:
pets = ["dog", "cat", "monkey", "parrot", "ferret"]
#       • Print the message The first three items in the list are:. Then use
#       a slice to print the first
#         three items from that program’s list.
print(f"The first three pets in the list are {pets[:3]}")
#       • Print the message Three items from the middle of the list are:.
#       Use a slice to print three items
#         from the middle of the list.
print(f"The pets from the middle of the list are: {pets[1:4]}")
#       • Print the message The last three items in the list are:. Use a
#       slice to print the last three
#         items in the list.
print(f"The last three pets from the list are: {pets[-3:]}")
# print("Any of these animals would make a great pet!")
