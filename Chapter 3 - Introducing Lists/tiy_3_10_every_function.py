'''3-10. Every Function: Think of something you could store in a list. For
example,
    you could make a list of mountains, rivers, countries, cities,
    languages, or
    any- thing else you’d like. Write a program that creates a list
    containing these items
    and then uses each function introduced in this chapter at least once.'''
print("\n*******************************************************")
print("3-10 Every function")
print("*******************************************************")
my_languages = ["france", "german", "spanish", "english", "chinese"]
#   Print base list
print(my_languages)
#   Print base list with title function
print(f"{my_languages[1].title()}")
#   Pop
print(f"{my_languages.pop(1)}")
print(my_languages)
#   Insert
my_languages.insert(1, "holand")
print(my_languages)
#   Append
my_languages.append("vietnam")
print(my_languages)
#   Sort
my_languages.sort()
print(my_languages)
#   Sort reverse
my_languages.sort(reverse=True)
print(my_languages)
#   Sorted
print(f"{sorted(my_languages)}")
#   Sorted reverse
print(sorted(my_languages, reverse=True))
#   Reverse
my_languages.reverse()
print(my_languages)
#   Len
# len(my_languages)
print(f"{len(my_languages)}")
