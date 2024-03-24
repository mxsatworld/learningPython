myset = {"apple", "banana", "orange"}
# a set is unordened, unchangeable(you cant change the items) and unindexed
print(myset)
# unordened means they can be in any order
# {'banana', 'apple', 'orange'}
# {'orange', 'banana', 'apple'}
# sets cannot have the same item
myset2 = {"apple", "banana", "orange", "orange"}
print(myset2)  # prints the set but the last item orange its not taking in acount

# you cant change the items of a set but you can add new ones
myset.add("pineapple")

# to add items from another set
tropical = {"mango", "papaya"}
myset.update(tropical)
print(myset)
# you can also use update with any iterable (list, tuple, dictionary, etc)

# to remove an item in a set use .remove or .discard
myset.remove("papaya")
# you can use the pop method to but you will remove a random item

# the clear method empties the set
tropical.clear()
print(tropical)

# the del method deletes the set completly
del tropical
# print(tropical) throws error because the set doesnt exists

# you can join two sets with the union method
set3 = myset.union(myset2)
print(set3)
