class A:
    def do_something(self):
        print("Method Defined in: A")

class B(A):
    def do_something(self):
        print("Method Defined in: B")

class C(A):
    pass        

class D(B,C):
    pass

thing = D()        
thing.do_something() # "Method Defined in: B"
