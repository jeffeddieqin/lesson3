def a(n,age,*args):
    if age>=18:
        print(n)
        for i in args:
            print(i)
    else:
        print("no!")

a(2,19,7,8,9)
