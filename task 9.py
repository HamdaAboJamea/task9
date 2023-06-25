
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangle_perimeter(self):
        return 2*(self.length + self.width)

    def rectangle_area(self):
        return self.length * self.width


    def disply(self):
        print("The length of rectangleb is :",self.length)
        print("The width of rectangleb is :",self.width)
        print("The perimeter of rectangleb is :",self.rectangle_perimeter())
        print("The area of rectangleb is :",self.rectangle_area())

class Parallelepiede(Rectangle) :
    def __init__(self, length, width, height):
        Rectangle.__init__(self, length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

new_rectangle = Rectangle(4 , 3)
new_rectangle.disply()
print("")
new_parallelepipeds = Parallelepiede(4, 3, 2)
print("The volume of new parallelepipeds is :", new_parallelepipeds.volume())