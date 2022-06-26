# print("hi")

number1 = 5
number2 = 6
# print(5+6)

for i in range(0, 10, 2):
    pass
# print(i)

# tuple - unchangable
# tuple1 = (1,2,3,'hi',1)
tuple1 = tuple([1, 2, 3, 'hi', 1])
for i in tuple1:
    pass
# print(i)
# tuple1[0] = 5 = TypeError: 'tuple' object does not support item assignment
# print(type(tuple1))

# list items are ordered, changeable, and allow duplicate values.

list1 = ['Apple', 'Mango', 'Orange', 1]
for l in list1:
    pass
# print(l)


# A set is a collection which is unordered, unchangeable*, and unindexed., unique
# TypeError: 'set' object does not support item assignment

set1 = {'A', 'B', 'c', 'a'}
for s in set1:
    pass
# print(s)

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

dictionary1 = {
    "Name": "Murugan",
    "Age": 25,
    "Address": "coimbatore"
}
# for d in dictionary1.values(),dictionary1.keys():
for k,v in dictionary1.items():
    pass
    # print(k,v)

# print(dictionary1)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

x = lambda a : a+10
y = lambda a,b : a+b

print(x(5))
print(y(5,5))

# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

