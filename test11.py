set1={2,3,1,5,4}
set2=set((2,3,4,1))
print(set1)
print(set2)#{1, 2, 3, 4}
set1.add(0)
print(set1)
set1.discard(1)
print(set1)#{0, 2, 3, 4, 5}
print(set1.difference(set2))#集合1有的0和5是集合2没有的
print(set2.difference(set1))#集合2有的1是集合1没有的
print(set1)