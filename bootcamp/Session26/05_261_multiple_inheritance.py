class A:
    def do_something(self):
        print("Method Defined in: A")

class B(A):
    def do_something(self):
        print("Method Defined in: B")

class C(A):
    def do_something(self):
        print("Method Defined in: C")        

class D(B,C):
    pass

thing = D()        
thing.do_something() # "Method Defined in: B"
print(D.__mro__)
print(D.mro())
help(D) 
# D,B,C,A