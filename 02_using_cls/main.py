# 2. Using cls
"""
Assignment:
Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count."""

# Counter naam ka class banaya gaya hai
class Counter:
    count = 0  # class variable jo total objects ka count rakhega

    def __init__(self):
        # jab bhi naya object banega, count 1 se barh jayega
        Counter.count += 1  

    @classmethod
    def display_count(cls):
        # class method hai jo total objects ka count print karega
        print(f"Total Counter created: {cls.count}")

# agar yeh file directly run ki jaye to neeche wala code execute hoga
if __name__ == "__main__":
   
    counter1 = Counter()  # pehla object banaya gaya, count = 1

    counter2 = Counter()  # doosra object banaya gaya, count = 2

    counter3 = Counter()  # teesra object banaya gaya, count = 3

    # total count display kiya gaya
    Counter.display_count()  # Output: Total Counter created: 3
