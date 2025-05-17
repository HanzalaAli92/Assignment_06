# 15. Method Resolution Order (MRO) and Diamond Inheritance
"""
Assignment:
Create four classes:

A with a method show(),

B and C that inherit from A and override show(),

D that inherits from both B and C.

Create an object of D and call show() to observe MRO."""

class A:
    def show(self):
        # Class A ka show method
        print("A's show() method")

class B(A):
    def show(self):
        # Class B ka show method, jo A ko override karta hai
        print("Method from class B")
    
class C(A):
    def show(self):
        # Class C ka show method, jo A ko override karta hai
        print("Method from class C")

class D(B, C):
    # Class D, jo B aur C dono se inherit karta hai (Diamond Inheritance)
    pass

if __name__ == "__main__":
    d = D()  # D ka object banaya

    d.show()  # show method call kiya, MRO ke mutabiq execute hoga

    print(D.mro())  # Method Resolution Order print karega (inheritance ka order)