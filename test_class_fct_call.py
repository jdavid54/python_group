class Node:
    
    def __init__(self, left, right):
        #print(left)
        self.left = left
        self.right = right
       
    def f1(self,counter):
        print("f1")
        counter += 5
        return counter
    
    def f2(self, counter):
        #print(self.left)
        if self.left:
            print("f1 from f2", self.left)
            self.left.f1(counter)
        else:
            print("f2")
            self.right.f1(counter)
        return counter
    
l1 = Node(5,6)

class Example(Node):    
    def __init__(self, left, right):
        super().__init__(left, right)
        #self.left = left
        #self.right = right

l1 = Node(15,8)
l2 = Node(5,77)

left = Node(None,l2)
right = Node(l2,l1)
    
ex1 = Example(left, right)

print(ex1.left.f2(5))
print(ex1.right.f1(7))

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)