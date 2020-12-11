from .tree import AdapterTree


class Day10:
    def __init__(self, data):
        self.raw_data = data
        self.adapters = [int(i) for i in self.raw_data]

        self.cached_combos = {}
        self.solved_combo_set = set()

    def solve_part1(self):

        adapters = sorted(self.adapters)

        last_joltage = 0
        one_jumps = 0
        three_jumps = 0
        while len(adapters) > 0:
            if last_joltage == adapters[0] - 1:
                one_jumps += 1
            elif last_joltage == adapters[0] - 3:
                three_jumps += 1
            else:
                print(f"What? {last_joltage} -> {adapters[0]}")

            last_joltage = adapters[0]

            adapters = adapters[1:]

        # add 3:
        three_jumps += 1

        print(f"One: {one_jumps} * Three: {three_jumps} = {one_jumps*three_jumps}")

    def solve_part2(self):
        adapters = sorted(self.adapters)
        print(adapters)
        adapters = [0] + adapters

        combinations = self.find_combos(adapters)
        print(f"Combinations: {combinations}")
        # print(f"Solutions count: {len(self.solved_combo_set)}")
        # Sample1 expects 8
        # Sample2 expects 19208

    def find_combos_tree(self, adapters):
        print(f"len(adapters): {len(adapters)}")
        tree = AdapterTree(adapters)
        tree.print_tree()
        tree.traverse_tree()

    def find_combos(self, adapters, partial=None):
        if not partial:
            partial = []
        combo = self.cached_combos.get(str(partial + adapters))
        if combo:
            # print(f"Cached {partial+adapters} = {combo}")
            return combo

        if len(adapters) == 1:
            local_combos = 1
            solution = partial + adapters
            self.solved_combo_set.add(str(solution))
            # print(f"Added {solution}")

        else:
            local_combos = 0
            if adapters[0] + 3 >= adapters[1]:
                partial1 = partial + [adapters[0]]
                local_combos += self.find_combos(adapters[1:], partial1)
            if len(adapters) > 2 and adapters[0] + 3 >= adapters[2]:
                partial2 = partial + [adapters[0]]
                local_combos += self.find_combos(adapters[2:], partial2)
            if len(adapters) > 3 and adapters[0] + 3 >= adapters[3]:
                partial3 = partial + [adapters[0]]
                local_combos += self.find_combos(adapters[3:], partial3)

        # print(f"Combos for {partial} | {adapters}: {local_combos}")
        self.cached_combos[str(adapters)] = local_combos
        return local_combos

    def find_combos3(self, adapters, partial=None):
        if not partial:
            partial = []
        combo = self.cached_combos.get(str(partial + adapters))
        if combo:
            print(f"Cached {partial+adapters} = {combo}")
            return combo

        if len(adapters) == 1:
            local_combos = 1
            solution = partial + adapters
            self.solved_combo_set.add(str(solution))
            print(f"Added {solution}")
        else:
            local_combos = 0
            if len(partial) == 0:
                local_combos = self.find_combos(adapters[1:], [adapters[0]])
                if adapters[0] + 2 >= adapters[2]:
                    local_combos += self.find_combos(adapters[2:], [adapters[0]])
                if adapters[0] + 3 >= adapters[3]:
                    local_combos += self.find_combos(adapters[3:], [adapters[0]])
            else:
                if adapters[0] + 3 >= adapters[1]:
                    partial1 = partial + [adapters[0]]
                    local_combos += self.find_combos(adapters[1:], partial1)
                if len(adapters) > 2 and adapters[0] + 3 >= adapters[2]:
                    partial2 = partial + [adapters[0]]
                    local_combos += self.find_combos(adapters[2:], partial2)
                if len(adapters) > 3 and adapters[0] + 3 >= adapters[3]:
                    partial3 = partial + [adapters[0]]
                    local_combos += self.find_combos(adapters[3:], partial3)

        print(f"Combos for {partial} | {adapters}: {local_combos}")
        self.cached_combos[str(adapters)] = local_combos
        return local_combos

    def find_combos2(self, adapters, partial=None):
        if not partial:
            partial = []
        combo = self.cached_combos.get(str(partial + adapters))
        if combo:
            print(f"Cached {partial+adapters} = {combo}")
            # solution = partial + adapters
            # self.solved_combo_set.add(str(solution))
            # print(f"Added {solution}")
            return combo

        if len(adapters) == 1:
            local_combos = 1
            solution = partial + adapters
            self.solved_combo_set.add(str(solution))
            # print(f"Added {solution}")
        else:
            local_combos = 0
            if adapters[0] + 3 >= adapters[1]:
                partial1 = partial + [adapters[0]]
                local_combos += self.find_combos(adapters[1:], partial1)
            if len(adapters) > 2 and adapters[0] + 3 >= adapters[2]:
                partial2 = partial + [adapters[0]]
                local_combos += self.find_combos(adapters[2:], partial2)
            if len(adapters) > 3 and adapters[0] + 3 >= adapters[3]:
                partial3 = partial + [adapters[0]]
                local_combos += self.find_combos(adapters[3:], partial3)

        # print(f"Combos for {partial} | {adapters}: {local_combos}")
        self.cached_combos[str(adapters)] = local_combos
        return local_combos

    def find_combos1(self, adapters):
        combo = self.cached_combos.get(str(adapters))
        if combo:
            print(f"Cached {adapters} = {combo}")
            return combo

        if len(adapters) == 1:
            local_combos = 1
        else:
            local_combos = 0
            if adapters[0] + 3 >= adapters[1]:
                local_combos += self.find_combos(adapters[1:])
            if len(adapters) > 2 and adapters[0] + 3 >= adapters[2]:
                local_combos += self.find_combos(adapters[2:])
            if len(adapters) > 3 and adapters[0] + 3 >= adapters[3]:
                local_combos += self.find_combos(adapters[3:])

        print(f"Combos for {adapters}: {local_combos}")
        self.cached_combos[str(adapters)] = local_combos
        return local_combos
