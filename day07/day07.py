import re
from .bag_graph import BagGraph, Bag


class Day07:
    # Started 1:48 later than start.
    def __init__(self, data):
        self.raw_data = data
        self.bag_graph = BagGraph()

    def solve_part1(self):
        self.load_input()
        print(self.bag_graph)

        target_color = "shiny gold"

        valid_colors = set()
        for color in self.bag_graph.colors():
            if self.bag_graph.can_contain(color, target_color):
                valid_colors.add(color)

        print(f"Count: {len(valid_colors)}, Valid Colors: {valid_colors}")

    def solve_part2(self):
        self.load_input()
        target_color = "shiny gold"
        target_bag = self.bag_graph.get_bag(target_color)

        print(f"{target_color} holds {target_bag.holds(self.bag_graph) - 1} bags.")

    def load_input(self):

        for line in self.raw_data:

            """
            light red bags contain 1 bright white bag, 2 muted yellow bags.
            dark orange bags contain 3 bright white bags, 4 muted yellow bags.
            bright white bags contain 1 shiny gold bag.
            muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
            shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
            dark olive bags contain 3 faded blue bags, 4 dotted black bags.
            vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
            faded blue bags contain no other bags.
            dotted black bags contain no other bags.
            """
            bag_color_pattern = re.compile(r"^(\w+ \w+) bags contain")
            no_other_pattern = re.compile(r"no other bags.$")

            bag_color = bag_color_pattern.match(line)[1]
            bag = Bag(bag_color)

            if no_other_pattern.match(line):
                pass
            else:
                containing = re.findall(r"(\d+) (\w+ \w+)", line)

                for b in containing:
                    quantity = b[0]
                    color = b[1]
                    bag.add_inner_bag(quantity, color)

            print(f"Added {bag}")
            self.bag_graph.add_bag(bag)
