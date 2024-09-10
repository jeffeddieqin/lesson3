class Person:
    def __init__(self,name,length,weight):
        self.name=name
        self.length=length
        self.weight=weight
    def print_name(self):
        print("This is my name"+self.name)
    def print_sayhello(self,newname):
        print("My name is"+self.name+"nice to see you"+newname)

person1=Person("秦烁",178,60)
person1.print_name()
person1.print_sayhello("张三")
