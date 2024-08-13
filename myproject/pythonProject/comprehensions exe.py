some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list({letter for letter in some_list if some_list.count(letter) > 1})
print(duplicates)
