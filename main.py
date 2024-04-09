# Check if a String contains an Element from a List in Python

my_str = 'one two three'

my_list = ['a', 'two', 'c']

if any(substring in my_str for substring in my_list):
    # 👇️ this runs
    print('The string contains at least one element from the list')
else:
    print('The string does NOT contain any of the elements in the list')