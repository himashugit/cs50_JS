class Point():
    def __init__(self, input1, input2): # this is how we define argument in the class. self is bydefault other we need to store info
        self.x = input1 
        self.y = input2

p = Point(1,2)
print(p.x)
print(p.y)

# storing 2 numbers using class. 