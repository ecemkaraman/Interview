# list is a collection which is ordered and changeable, with continuous space.
#
# Space: O(n)

"""Time Complexities"""
my_list = [1, 2, 3, 4, 5]
# Accessing an element by index: O(1) → you go directly to that index
print(my_list[2]) # Output: 3

#Access an element by value: O(n) - iterate through whole list
target = 3
for element in my_list:
    if element == target:
        print(“Element found!”)
        break
    else:
        print(“Element not found.”)

#Adding/removing an element at the end: O(1)
my_list.append(6) # [1, 2, 3, 4, 5, 6]
my_list.pop() # [1, 2, 3, 4, 5]

#Adding/removing an element anywhere else: O(n) →the rest needs the be re-indexed
my_list.insert(0, 0) # [0, 1, 2, 3, 4, 5]
my_list.pop(2) # [0, 1, 3, 4, 5]

#Appending one list to another: O(k), k=len(list_being_appended)
list2 = [6, 7, 8]
list1.extend(list2) # [1, 2, 3, 4, 5, 6, 7, 8]

#Slicing a list: O(k), k=len(resulting_sublist)
sublist = my_list[1:4] # [2, 3, 4]

def list_operations():
    # initialization
    list1 = [3, 1, 2, 4]

    list2 = list(range(5))
    # [*X] equals to list(X)
    list2 = [*range(5)]

    # append
    list1.append(5)
    list1 += [5]
    list1 += 5,
    list1.extend([5, 6])

    # insert
    list1.insert(0)

    # index
    list1.index(3)

    # count
    list1.count(3)

    # remove
    list1.remove(3)

    # sort
    list1.sort(reverse=True)

    # reverse
    list1.reverse()