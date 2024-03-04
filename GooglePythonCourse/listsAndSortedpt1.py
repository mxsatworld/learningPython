# list are like js arrays
colors = ["red", "violet", "orange"]
# this doesnt make a copy of the array, it makes that colors and b point to the same array
b = colors
b.pop()  # pop removes last element of a list, like js
print(b)  # red violet
# red violet, here the last element is also missing because b points to colors
print(colors)
list1 = [1, 2]
list2 = [3, 4]
print(list1 + list2)  # combine two list so the output is [1,2,3,4]

# for in is useful to iterate over a list
list3 = [1, 2, 5, 10, 12]
total = 0
for elem in list3:
    total += elem
print(total)

superString = "Cowboys from hell"
# you can iterate over strings
for letter in superString:
    print(letter)

# the range functions yields(genera/produce en español) a list of numbers from 0 to n-1
for number in range(100):
    print(number)  # prints 0-99

list4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(list4):
    print(list4[i])
    i = i + 3  # access every third element of the list
list4.append(11)  # add an element to the final of a list
print(list4)
list4.insert(5, 12)  # inserts in index 5 element 11
print(list4)
list4.extend(list3)  # adds the elements of list to the list 4
print(list4)
# returns the index where is 12, throws error in case of not found
print(list4.index(12))  # returns 5
# returns True or False, in case you want to avoid the traceback error
print(120 in list4)
# remove the first instance of 12, throws error in case of not findining
list4.remove(12)
list4.append(200)
list4.sort()  # sorts the list, in case of numbers sorts it from minor to mayor
print(list4)
list5 = ['c', 'u', 'm', 'b', 'i', 'a']
list5.sort()  # sorted alphabetically
print(list5)
list5.reverse()  # reverses it, the first element go to the final and so on
print(list5)
# remove the element in index 3, if no arg is passed removes the last element
list5.pop(3)

# you can also use slices in lists
print(list5[1:-1])  # prints from index 1 to second to last element
list5[0:2] = "z"  # changes the index 0 and 1 to string z
print(list5)


# NOTE, THIS IS MY OWN RESEARCH BECAUSE THE SORTED METHOD WASNT EXPLAINED AND SOLVING THE PROBLEMS
# I REALIZE THAT THIS METHOD COULD MAKE MY CODING MORE EASY AND PERFORMANT
# with sorted you cant sort a list that contains numerical and alphabetical numbers
# sorted(iterable, key=key, reverse=reverse), reserve is a boolean, false will sort ascending
# True will sort descending, default is false
# key is a function to execute to decide the order
def last(a):
    # this would make that every tuple would have associated the last item to them
    return a[-1]
# and organize it using the last item as a reference
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields


def sort_last(tuples):
    # order this having the last element of the tuple in count
    return sorted(tuples, key=last)
# [(2,2),(1,3),(3,4,5),(1,7)]


# sort descending
list6 = [1, 2, 3, 4, 5]
# sorted doesnt change the list6 list, only returns a new list
list7 = sorted(list6, reverse=True)
# with the changes made
print(list7)

strs = ['a', 'aa', 'a', 'aaa', 'wxscs']
print(sorted(strs, key=len))  # sort by length
# every item of strs is passed to the key function as argument
# the return of the key function is called "proxy value"
# then the elements are sorted acording to their "proxy value" associated
