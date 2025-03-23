# create an empty list
my_list = []

# appending elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After Appending:", my_list)

# insert elements at a specific index
my_list.insert(1, 15)
print(my_list)

# extending my_list with another list
my_list2 = [50, 60, 70]
my_list.extend(my_list2)
print(my_list)

# remove elements from my_list
my_list.remove(40)
print(my_list)

# sorting my_list
my_list.sort()
print(my_list)

# find and print the index of the value 30 in my_list.
index_of_30 = my_list.index(30)
print(index_of_30)