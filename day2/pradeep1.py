### liner structure

list1 = [2, 66, 5, 8, "ram", "pradeep", [67, 98, 56], 567]
print(list1)

list1.append(89)
print(list1)

list2 =["anil", 78, 89,["pinki", 34 ], 90]
list1.extend(list2)
print(list1)

print(list1.index([67, 98, 56]))
print(list1)

list1.insert(2, "ankit")
print(list1)

list1.remove(8)
print(list1)

list3 = [8, 9, 4, 2, 45, 25, 189, 110 ]
list3.sort()
print(list3)

list3.reverse
print(list3)

tuple1 = (4, 5, 2, ["ankit", "ram"], 67, 56)
print(tuple1)


## Non Liner Structure

dict1 = {"ankit": 34, "anil": 40, "priya": 55, "anuj": 78}
print(dict1)

a = list(dict1.items())
print(a)

dict2 = {"anita": 45, "alisha": 99, "monika": 56}
dict1.update(dict2)
print(dict1)

print(dict1.get("anuj"))

print(dict2.values())

print(dict1.keys())

dict2.pop("anita")
print(dict2)

print(dict1.popitem())


set1 = {4, 7, 2, "aman", "alok"}
print(set1)

set1.add(34)
print(set1)

set1.pop()
print(set1)

set2 = {4, 2,"ajay", 7, 34, 8, "alok"}
set1.difference(set2)
print(set2)
print(set1)

set2.pop()
print(set2)

set2.union(set1)
print(set2)
print(set1)

set2.intersection(set1)
print(set2)
print(set1)

set3 = {5, 67, 56, 78, 99}
set2.update(set3)
print(set2)



