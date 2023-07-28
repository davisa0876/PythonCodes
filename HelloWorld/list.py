mylist = []
mylist.append([1,3])
mylist.append([2,2])
mylist.append([3,1])
print(mylist[0][1]) # prints 1
print(mylist[1][1]) # prints 2
print(mylist[2][1]) # prints 3

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
# prints out 1,2,3
for x in mylist:
    print(x)

mylist = [1,2,3]
print(mylist[2])

numbers = [1, 2, 3, 4, 5]
strings = ["apple", "banana", "cherry"]
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
