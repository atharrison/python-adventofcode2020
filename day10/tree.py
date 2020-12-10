class AdapterTree:
    def __init__(self, adapters):
        self.root = AdapterNode(adapters[0])
        self.nodelist = {}
        self.nodelist[self.root.val] = self.root
        self.fill_tree(adapters)

        self.global_count = 0

    def __str__(self):
        return f"Tree: {self.root}"

    def get_node(self, val):
        return self.nodelist.get(val)

    def print_tree(self):
        for nodeval in self.nodelist.keys():
            print(f"Node {nodeval} -> {list(self.nodelist[nodeval].nodes.keys())}")

    def fill_tree(self, adapters):
        for val in adapters[1:]:
            new_node = AdapterNode(val)
            self.nodelist[val] = new_node
            for nodeval in self.nodelist.keys():
                existing_node = self.nodelist[nodeval]
                if existing_node.val != new_node.val and val <= existing_node.val + 3:
                    existing_node.add_node(new_node)

    def traverse_tree(self):
        count = self.node_count_from(self.root, [self.root.val])
        print(f"Traverse count: {count}")
        print(f"Traverse global_count: {self.global_count}")

    def node_count_from(self, node, path):
        # print(f"node_count_from {node.val}")
        if len(node.nodes) > 0:
            for nodeval in node.nodes.keys():
                child = node.nodes[nodeval]
                # print(f"Traversing {node.val} -> {child.val} ...")
                self.node_count_from(child, path + [child.val])
        else:
            # print(f"Leaf node {node.val} with path {path}")
            self.global_count += 1
            if (self.global_count % 100000) == 0:
                print(self.global_count)

    def node_count_from2(self, node, path):
        # print(f"node_count_from {node.val}")
        if len(node.nodes) > 0:
            count = 0
            for nodeval in node.nodes.keys():
                child = node.nodes[nodeval]
                # print(f"Traversing {node.val} -> {child.val} ...")
                count += self.node_count_from(child, path + [child.val])
            return count
        else:
            print(f"Leaf node {node.val} with path {path}")
            return 1


class AdapterNode:
    def __init__(self, val):
        print(f"Creating node {val}")
        self.val = val
        self.nodes = {}

    def add_node(self, node):
        print(f"----> Adding {node.val} to {self.val}")
        self.nodes[node.val] = node

    def __str__(self):
        return f"Node: {self.val} -> {list(self.nodes.keys())}"

    def __repr__(self):
        return self.__str__()
