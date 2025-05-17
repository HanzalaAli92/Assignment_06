# 4. Class Variables and Class Methods
"""
Assignment:
Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances."""

# Bank naam ka class banaya gaya hai
class Bank:
    bank_name = "Default Bank"  # Class variable (yeh sab instances ke liye common hoti hai)

    @classmethod
    def change_bank_name(cls, name):
        # Class method jo bank_name ko change karega
        cls.bank_name = name
     
# Agar yeh file directly run ki jaye to neeche wala code chalega
if __name__ == "__main__":
    # Bank class ke do objects banaye gaye
    user1 = Bank()
    user2 = Bank()

    # Shuru mein dono ka bank_name default hoga
    print(f"Initial bank name: {user1.bank_name}")

    # Bank name ko class method ke zariye change kiya gaya
    Bank.change_bank_name("Meezan Bank")

    # Change hone ke baad dono instances mein updated name show hoga
    print(f"Updated bank name for bank1: {user1.bank_name}")
    print(f"Updated bank name for bank2: {user2.bank_name}")