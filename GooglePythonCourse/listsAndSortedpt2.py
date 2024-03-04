from operator import itemgetter, attrgetter
student_tuples = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'C', 10)]
# proxy value is the third element of the tuple
print(sorted(student_tuples, key=lambda student: student[2]))
# you can do the same with sorted(student_tuples, key=itemgetter(2))


class Student:
    def __init__(self, name, grade, age):  # object mold
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):  # repr for representation
        # the object would be represented in a tuple
        return repr((self.name, self.grade, self.age))


student_objects = [Student('john', 'A', 15), Student(
    'jane', 'B', 12), Student('dave', 'C', 10)]
# using a object property as proxy
print(sorted(student_objects, key=lambda student: student.age))
# you can do the same with sorted(student_objects, key=attrgetter('age'))
print(student_objects[0].__repr__())

# (first name, last name, score) tuples
grade = [('Freddy', 'Frank', 3), ('Anil', 'Frank', 100), ('Anil', 'Wang', 24)]
print(sorted(grade, key=itemgetter(1, 0)))
# After f = itemgetter(2), the call f(r) returns r[2].
# After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3]).
# in other words, when you pass more than 1 argfor itemgetter you receive a tuple with the
# element with the indexes you specified (2, 5, 3)
# (Frank, Freddy) (Frank, Anil) (Wang, Anil)
# each tuple works like an index value for every element in the grade list
# after that they are organized applying sort to the index value
# the same logic works with attrgetter
# After f = attrgetter('name'), the call f(b) returns b.name.
# After f = attrgetter('name', 'date'), the call f(b) returns (b.name, b.date).
# After f = attrgetter('name.first', 'name.last'), the call f(b) returns (b.name.first, b.name.last).
# [('Anil', 'Frank', 100), ('Freddy', 'Frank', 3), ('Anil', 'Wang', 24)]
tupleExample = [('Freddy', 'Frank', 3),
                ('Anil', 'Frank', 100), ('Anil', 'Wang', 24)]
print(sorted(tupleExample))
# [('Anil', 'Frank', 100), ('Anil', 'Wang', 24), ('Freddy', 'Frank', 3)]
print(sorted([('Frank', 'Freddy'), ('Frank', 'Anil'), ('Wang', 'Anil')]))
sorted(grade, key=itemgetter(0, -1))
# [('Anil', 'Wang', 24), ('Anil', 'Frank', 100), ('Freddy', 'Frank', 3)]


# TUPLES CHAPTER
# Tuples cannot be changed
# tuple[2] = 0 throws error
tuple2 = (1, 1)
print(tuple2)

# List comprehensions
nums = [1, 2, 3, 4]
squares = [n * n for n in nums]  # [1, 4, 9, 16]
# list comprehensions is a way to write a new list by using another one
# The syntax is [ expr for var in list ]
# ANOTHER EXAMPLE
strs = ['hello', 'and', 'goodbye']
shouting = [elem.upper() + '!!!' for elem in strs]
print(shouting)

# you can use if in list comprehensions
nums = [2, 8, 16, 5]
small = [n for n in nums if n <= 2]  # [2]
print(small)
