l=[1,2,3,8,7]
print(l)
for i in l:
    print(i)
    
#len:
print(len(l))

##added value:
l.append(4)
print(l)


#inser in specific position:position value

l.insert(1,0)
print(l)

#remove element:
l.remove(0)
print(l)

#remove element by index:

re=l.pop(1)
print(re)

#clear the list:
# l.clear()
# print(l)

# Extending list with another list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print("List1 after extending with list2:", list1)

# Slicing
print("Sliced list:", list1[1:4])


# Reversed
list1.reverse()
print("Reversed list:", list1)

# Sorting the list
list1.sort()
print("Sorted list:", list1)