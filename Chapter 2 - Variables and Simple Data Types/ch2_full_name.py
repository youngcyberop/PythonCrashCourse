# Using Variables in Strings

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

#   f-strings are format strings which place variables into strings

#   usage example
print(f"Hello, {full_name.title()}!")

#   usage example
message = f"Hello, and welcome {full_name.title()}!"
print(message)

#   f-strings were introduced in Python 3.6 and replaced format() method

full_name = "{} {}".format(first_name, last_name)
print(full_name)

# Adding whitespace
# add \t for tab
print("\tPython")
# add \n for new line
print("Languages:\n\tPython\n\tJavaScript\n\tC")

# Stripping whitespace

favorite_language = 'python '
#   .rstrip() removes white space before and after the string
favorite_language.rstrip()
#   .rstrip() only removes white space temporarily
#   so use rstrip() has to modify the variable
favorite_language = favorite_language.rstrip()
print(favorite_language)

#   white space can be removed from the left and right side of variables
favorite_language = ' python '
print(favorite_language)
#   left removal
favorite_language = favorite_language.lstrip()
print(favorite_language)
#   right removal
favorite_language = favorite_language.strip()
print(favorite_language)
