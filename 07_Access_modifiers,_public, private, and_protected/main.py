# 7. Access Modifiers: Public, Private, and Protected
"""
Assignment:
Create a class Employee with:

. a public variable name,

. a protected variable _salary, and

. a private variable __ssn.

Try accessing all three variables from an object of the class and document what happens."""

# Employee naam ka class banaya gaya hai
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public variable (har jagah se directly access ho sakta hai)
        self._salary = salary   # Protected variable (underscore lagaya gaya, convention ke mutabiq sirf class ya subclass mein access karna chahiye)
        self.__ssn = ssn        # Private variable (double underscore lagaya gaya, directly access nahi hota)

# Agar yeh file directly run ki jaye to neeche wala code chalega
if __name__ == "__main__":
    emp = Employee("Ali", 50000, "123-45-6789")  # Employee class ka object banaya gaya

    # Public variable ko access kar rahe hain (yeh work karega)
    print(f"public variable: Name: {emp.name}")  # Output: Ali

    # Protected variable ko access kar rahe hain (yeh bhi work karega lekin directly access karna recommended nahi hai)
    print(f"protected variable: Salary: {emp._salary}")  # Output: 50000

    # Private variable ko direct access karne ki koshish (yeh error dega)
    try:
        print(f"SSN: {emp.__ssn}")  # Yeh line AttributeError raise karegi
    except AttributeError as e:
        print(f"Error: {e}")  # Error message print hoga

    # Private variable ko name mangling ke zariye access kar rahe hain (yeh kaam karega)
    print(f"SSN (using name mangling): {emp._Employee__ssn}")  # Output: 123-45-6789