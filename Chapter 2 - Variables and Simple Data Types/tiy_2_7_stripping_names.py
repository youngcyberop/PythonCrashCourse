'''
2-7. Stripping Names: Use a variable to represent a person’s name, and include
some whitespace characters at the beginning and end of the name. Make sure
you use each character combination, "\t" and "\n", at least once.
    Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip().
'''

#   practice with generic space bar white spaces
first_name = " Robert "
last_name = " Young "
print(first_name)
print(last_name)

#   practice with \n and \t white spaces
first_name = "\nRobert"
last_name = "\tYoung"
print(first_name)
print(last_name)

#   rstrip()
print("\nrstrip")
first_name = " Robert "
first_name = first_name.rstrip()
print(first_name)

#   lstrip()
print("\nlstrip")
first_name = " Robert "
first_name = first_name.lstrip()
print(first_name)

#   strip()
print("\nstrip")
first_name = " Robert "
first_name = first_name.strip()
print(first_name)




