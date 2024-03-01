greeting = "Hello"
print(greeting[1:4])  # prints ell 2 3 4
print(greeting[1:])  # prints ell 1 2 3 4
print(greeting[:])  # prints Hello 0 1 2 3 4
print(greeting[1:100])  # prints ello 0 1 2 3 4
print(greeting[-1])  # prints last character o
print(greeting[:-3])  # prints all except the last 3 characters
print(greeting[-3:])  # prints the last 3 elements

# Convert numbers to string
value = 2.7914
# formatted string, all values inside the curly brackets {} are formated to string
print(f'value = {value:.3f}')
car = {'tires': 4, 'doors': 2}  # dictionary, its like a js object
print(f'car = {car}')

# Example of formatted string
address_book = [{'name': 'N.X.', 'addr': '15 Jones St', 'bonus': 70}, {'name': 'J.P',
                                                                       'addr': '1005 5th St', 'bonus': 400}, {'name': 'A.A.', 'addr': '200001 Bdwy', 'bonus': 5}]
# for bucle to iterate over a dictionary
for person in address_book:
    print(f'{person["name"]:8} || {person["addr"]:20} || {person["bonus"]:>5}')
    # the two points and a number slice type notation servs for make blank space so the output is
    # more organized
  # % operator

# string % operator
# %d int, %s string, %f/%g floating point
# to the right there is a tuple, the string takes from the tuple the matching values and
# puts it on the string in order (first 3, second puff, third huff and so on)
text = "%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down." % (
    3, 'puff', 'huff', 'house')
print(text)
# in python you cannot split long lines like you do in js because you dont have a closing line token
# like ; (on the other hand this is useful because you dont need a token to end the line)
# so, for splitting a long line in python you can enclose it with () [] or {}
text = ("%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down." %
        (3, 'puff', 'huff', 'house')
        )  # LIKE THIS!!!
# you can also split the string in chunks and python automatically concatenates them
print(text)
