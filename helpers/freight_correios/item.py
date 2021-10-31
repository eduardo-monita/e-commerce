class Item(object):

    def __init__(self, weight=0.0, height=0.0, width=0.0, length=0.0):
        self.weight = weight
        self.height = height
        self.width = width
        self.length = length

    def __add__(self, other):
        return Item(
            weight=self.weight + float(other.weight),
            height=self.height + float(other.height),
            width=max(self.width, other.width),
            length=max(self.length, other.length)
        )
