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
