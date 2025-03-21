#Create an empty list called my_list.
myList = []
# Append the following elements to my_list: 10, 20, 30, 40.
myList.append(10)
myList.append(20)
myList.append(30)
myList.append(40)
print(myList)
#Insert the value 15 at the second position in the list.
myList.insert(1,15)
print(myList)
#Extend my_list with another list: [50, 60, 70].
myList.extend([50, 60, 70])
print(myList)
#Remove the last element from my_list.
myList.pop()
print(myList)
#Sort my_list in ascending order.
myList.sort()
print(myList)
#Find and print the index of the value 30 in my_list.
index_of_30 = myList.index(30)
print("Index of 30:", index_of_30)

