dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'
print(dict)
dict['a'] = 6  # you can overwrite a dict value
print('a' in dict)  # True

for key in dict:
    print(key)  # keys are not organized

print(dict.keys())  # get the keys list dict_keys(['a', 'g', 'o'])
# get the values list dict_values(['alpha', 'gamma', 'omega'])
print(dict.values())
# loop over the keys in sorted order
for key in sorted(dict.keys()):
    print(key, dict[key])

# dict_items([('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')])
print(dict.items())

for k, v in dict.items():
    print(k, '>', v)  # print all key and values of a dictionary

h = {}
h['word'] = 'garfield'
h['count'] = 42
# s = 'I want %(count)d copies of %(word)s' % h  # %d for int, %s for string
# 'I want 42 copies of garfield'
s = f'I want {h["count"]} copies of {h["word"]}'
print(s)

# delete
x = 6
del x
list = [0, 1, 2, 3, 4, 5]
del list[0]
del list[-2:]  # delete last two elements
print(list)

dict = {'a': 1, 'b': 2, 'c': 3}
del dict['b']
print(dict)

# with open you cand open files
f = open('foo.txt', 'rt', encoding='utf-8')  # rt comes from Read y Text
# r y t are defaults values in open
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exist
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)
for line in f:
    print(line, end='')  # end='' so print does not add an end-of-line char
a = open('foo.txt', 'r', encoding='utf-8')
# read the whole file into memory and returns the content as a list of lines
# print(a.readlines())
print(a.read())  # read the whole file into one string
f.close()
a.close()
# with a you append and with write w you erase all and write
b = open('foo.txt', "a", encoding="utf-8")
# new text
# erase all the previous text and replace it all with sample graffiti
b.write("sample graffiti")
b.close()
# reading one line at the time is useful when you have 10gb of text so you cand read one line
# then the garbage collector erase the line from memory and pass to the next line
# erase it from memory and pass to the next and so on, with this method you avoid using 10gb of
# memory


with open('foo.txt', 'rt', encoding='utf-8') as f:
    for line in f:
        print(line)

with open('write_test', encoding='utf-8', mode='wt') as f:
    f.write('\u20ACunicode\u20AC\n')  # €unicode€
    # AKA print('\u20ACunicode\u20AC', file=f)  ## which auto-adds end='\n'
