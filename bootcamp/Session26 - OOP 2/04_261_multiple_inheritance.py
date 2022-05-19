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
    def do_something(self):
        print("Method Defined in: D")

thing = D()        
thing.do_something()