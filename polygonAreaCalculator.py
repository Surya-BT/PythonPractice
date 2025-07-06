# this is the next project in the free code camp
# use Object oriented programming language

class Rectangle:
    
    def __init__(self, width=None, height=None):
        self.width = width
        self.height = height

    def set_width(self,w):
        self.width = w
        if isinstance(self,Square):
            self.height = w

    def set_height(self,h):
        self.height = h
        if isinstance(self, Square):
            self.width = h

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2*self.width + 2*self.height
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5
    
    def get_picture(self):

        if (self.height > 50) or (self.width > 50):
            return f"Too big for picture."
        
        else:
            pic = "".join(["*" for _ in range(self.width)])
            #pic = "*"
            pic_str = ""

            for _ in range(self.height):
                pic_str += f"{pic}\n"

            return pic_str

    def get_amount_inside(self,other):
        #check if it belongs to class REctange or Square
        if isinstance(other, (Rectangle,Square)):
            print(f"The passed in object has the correct class")
            if other.get_area() < self.get_area():
                return int(self.get_area()/other.get_area())
            else:
                return 0
            
        elif isinstance(other, (int, float)):
            return NotImplemented
        else:
            raise ValueError("The passed object is not from the correct class")
            return NotImplemented
        
        

    def __str__(self):
        if self.__class__.__name__ == "Rectangle":
            return f"Rectangle(width={self.width}, height={self.height})"
        elif self.__class__.__name__ == "Square":
            return f"Square(side={self.width})"
            


class Square(Rectangle):
    def __init__(self,side):
        super().__init__(width=side,height=side)

    def set_side(self,s):
        self.width = s
        self.height = s

## Actual code ##

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

