x = y = z = 33  # assing same value to three variables

# make global variables


def myfunc():
    global x
    x = "fantastic"


# specify datatype
x = str(3)
y = int(3)
z = float(3)

# print type of the data
x = print(type(x))

# the diference between list and tuple are that tuple are unchangeables

a = 3+5j
print(complex(a))  # convert to a complex number

# you can put placeholders in a string
text = "Method {}"
print(text.format("Man"))
b = "Hello-World"
print(b.split("-"))  # split a string and returns a list with the splits
