import math
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,new_width):
        self.__width = new_width
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, new_height):
        self.__height = new_height

    def get_area(self):
        return self.height* self.width
    
    def get_perimeter(self):
        return 2*(self.height+self.width)
    
    def get_diagonal(self):
        return math.sqrt(self.height**2 + self.width**2)
    
    def get_picture_no_pinted(self):
        if self.width > 50 or self.height >50:
            return "Too big for picture."
        
        picture = self.width*'*'
        for i in range(0, self.height-2):
            picture += f"\n*{(self.width-2)*' '}*"
        picture += f"\n{self.width*'*'}"

        return picture
    
    def get_picture(self):
        if self.width > 50 or self.height >50:
            return "Too big for picture."
        
        picture = self.width*'*'
        for i in range(0, self.height-1):
            picture += f"\n{self.width*'*'}"
        return picture

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        
        super().__init__(side, side)
        
    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, new_side):
        self.__side = new_side

    @property
    def width(self):
        return self.side

    @width.setter
    def width(self, new_side):
        self.side = new_side
    @property
    def height(self):
        return self.side

    @height.setter
    def height(self, new_side):
        self.side = new_side


    def __str__(self):
        return f"Square(side={self.side})"

r1 = Rectangle(3,6)
print(r1.width, r1.height)
print(r1.get_perimeter())
print(r1.get_picture())
print(r1.get_area())
print(r1.get_diagonal())
print(r1)
print("=================================")
sq = Square(5)
sq.width = 6
print(sq.get_perimeter())
print(sq.get_picture())
print(sq.get_area())
print(sq)