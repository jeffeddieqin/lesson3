string1="this is test7."
print(len(string1))
print(string1.capitalize())#第一个字母变成了大写
print(string1.upper())#全部大写
print(string1.lower())#全部小写
print(string1.replace("test","TEST"))
print(string1)#string1本身并没有被replace
print(string1.find("is"))#返回值是2，代表从字符串的第三个字符开始
print(string1.islower())
print((string1.upper()).isupper())#检查是否全是大写