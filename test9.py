tuple1=(1,2,3,4,5)
print(tuple1)
print(list(tuple1))#元组向列表转换
list1=list(tuple1)#元组不可修改，我将tuple1强制转换为list保存进list1之后，可以对list1中的内容进行修改
list1[4]=0
print(list1)

