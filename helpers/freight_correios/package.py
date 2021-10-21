from .constants import PACKAGE_OR_BOX
from .item import Item
from functools import reduce


class Package(object):

    def __init__(self, format=PACKAGE_OR_BOX):
        self.format = format
        self.items = []
        self.reduced_item = Item()

    def add_item(self, **item_args):
        item = Item(**item_args)
        self.items.append(item)
        self.reduced_item = reduce(lambda a, b: a + b, self.items, Item())

        return item

    @property
    def weight(self):
        return self.reduced_item.weight

    @property
    def height(self):
        return self.reduced_item.height

    @property
    def width(self):
        return self.reduced_item.width

    @property
    def length(self):
        return self.reduced_item.length
