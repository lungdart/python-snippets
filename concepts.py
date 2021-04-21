##################
### Data types ###
##################
# Integers (Whole numbers)
0
-42
99999

# Floats (Fractional numbers)
.0
0.7
-42.198
-0.0000002

# Strings (Words and sentences)
'Hello World'
"How are you?"
"Notice I can use two symbols to make strings!"

# Logic
True
False
None # Special case which means empty, which is different than false

#################
### VARIABLES ###
#################
name = "Hello world"
number = 42
new_number = 100.99

##################
### CONTAINERS ###
##################
# Lists
list1 = [1, 2, 'foo', "bar"]
empty_list = []
list2 = [42.88, None, False, True]

list2.append("Hello there!")
list2[0] #42.88
len(list1)

# Tuples
tuple1 = (1, 2, 'foo', "bar")
tuple2 = (42.88, None, False, True)
empty_tuple = (,) # Empty tuples need to look silly to be different then parenthesis in PEDMAS

tuple1[2] # 'foo'
tuple1.append("This can't be done!") # ERROR
len(tuple1)

# Dictionaries
dict_1 = {'a': True, 'b': False}
empty_dict = {}
dict_2 = {42: None}

dict_1['a']
dict_2[42]
dict_2["Brand new key"] = True
len(dict_1)

# Functions
def add_and_double(number1, number2):
    new_number = (number1 + number2) * 2
    return new_number

result = add_and_double(42, 99)

#################
### Branching ###
#################
if my_number < 100:
    do_thing_1()
elif your_name is not None:
    do_thing_2()
else:
    go_to_sleep(44)


###############
### Looping ###
###############
# For loops
for value in [1, 2, 3, 4]:
    print(value)

my_dictionary = {'a': True, 'b': False}
for key in my_dictionary:
    print( my_dictionary[key] )

# While loops
while True:
    go_forever()

result = 100
while result > 5:
    result = result / 2
    print(result)

###############
### Classes ###
###############
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def height_in_cm(self):
        return self.height * 2.54

    def is_senior(self):
        return self.age > 65

shawn = Person("Shawn", 35, 68)
shawn.height_in_cm() # 172
if shawn.is_senior():
    print("You're getting old!")
