class BagGraph:
    def __init__(self):
        self.bag_colors = {}

    def add_bag(self, bag):
        self.bag_colors[bag.color] = bag

    def get_bag(self, color):
        return self.bag_colors.get(color)

    def __str__(self):
        return f"{self.bag_colors}"

    def colors(self):
        return self.bag_colors.keys()

    def can_contain(self, color, target_color):
        if color == target_color:
            return False

        bag = self.get_bag(color)
        can_contain = False
        for c in bag.containing_colors():
            if c == target_color:
                return True
            else:
                can_contain = can_contain | self.can_contain(c, target_color)

        return can_contain


class Bag:
    def __init__(self, color):
        self.color = color
        self.inner_bag_count = {}

    def add_inner_bag(self, quantity, color):
        self.inner_bag_count[color] = quantity

    def containing_colors(self):
        return self.inner_bag_count.keys()

    def __str__(self):
        return f"{self.color}: {self.inner_bag_count}"

    def __repr__(self):
        return self.__str__()
