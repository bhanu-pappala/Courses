class Rectange:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return (self.__length * self.__width)

    def perimeter(self):
        return (2 * (self.__length + self.__width))

obj1 = Rectange(4, 5)
print(f'Area is : { obj1.area() }')
print(f'Perimeter is : {obj1.perimeter() }')


