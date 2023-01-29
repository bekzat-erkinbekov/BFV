data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = [i for i in data_tuple if type(i) == str]
numbers = [i for i in data_tuple if type(i) != str]
del numbers[0]
delete = numbers.pop(0)
letters.append(delete)
numbers.insert(1, 2)
numbers.sort()
letters.reverse()
letters[1] = "G"
letters[-2] = "c"
numbers[1] = 4
numbers[2] = 9
print(tuple(letters))
print(tuple(numbers))