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
        print(f"{self.color} adding {quantity}:{color}")
        self.inner_bag_count[color] = int(quantity)

    def containing_colors(self):
        return self.inner_bag_count.keys()

    def holds(self, bag_graph):
        sum = 0
        for color, quantity in self.inner_bag_count.items():
            bag = bag_graph.get_bag(color)
            print(f"Looking at {bag}...")
            subcount = bag.holds(bag_graph)
            if subcount == 0:
                print(
                    f"{color} holds no bags. But we({self.color}) hold {quantity} of them."
                )
                sum += quantity
            else:
                print(
                    f"{color} holds {subcount} bags, and we({self.color}) hold {quantity} of them."
                )
                sum += quantity * subcount

        print(f"{self.color} contains {sum} bags.")
        # Also include ourselves in sum:
        return sum + 1

    def __str__(self):
        return f"{self.color}: {self.inner_bag_count}"

    def __repr__(self):
        return self.__str__()
