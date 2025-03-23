# create an empty list
my_list = []

# appending elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)


# insert elements at a specific index
my_list.insert(1, 15)


# extending my_list with another list
my_list2 = [50, 60, 70]
my_list.extend(my_list2)


# remove elements from my_list
my_list.remove(40)


# sorting my_list
my_list.sort()


# find and print the index of the value 30 in my_list.
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

# Print the final list
print("Final list:", my_list)