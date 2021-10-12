class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        shape = ''
        if self.width > 50 or self.height > 50:
            shape = 'Too big for picture.'
        else:
            for i in range(0, self.height):
                shape += '*'*self.width + '\n'
        print(shape)
        return shape

    def get_amount_inside(self, shape):
        amount = 0
        for y in range(0, self.height, shape.height):
            for x in range(0, self.width, shape.width):
                if (shape.width + x) <= self.width and (shape.height + y) <= self.height:
                    amount += 1
        return amount

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

    def set_width(self, side):
        super().set_width(side)
        super().set_height(side)

    def set_height(self, side):
        super().set_height(side)
        super().set_width(side)

    def __str__(self):
        return f'Square(side={self.width})'

