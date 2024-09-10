def a(n,age=18,*args,**kwargs):
    if age>=18:
        print(n)
        for i in args:
            print(i)
        print(kwargs["ns"])
    else:
        print("no!")
        print(kwargs["nt"])
a(1,196,2,3,6,9,ns=15,nt=16)