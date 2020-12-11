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

    def find_combos(self, adapters):
        return self.find_combos_recursive(adapters[0], adapters[1:])

    def find_combos_recursive(self, val, tail):
        # Bah, problem was all the other solutions were caching *every* combo, not just the tail combos.
        if len(tail) == 0:
            return 1

        combo = self.cached_combos.get(str(tail))
        if combo:
            print(f"Cache hit against {str(tail)} = {combo}")
            return combo
        else:
            count = 0
            if val + 3 >= tail[0]:
                portion1 = self.find_combos_recursive(tail[0], tail[1:])
                self.cached_combos[str(tail[1:])] = portion1
                count += portion1
            if len(tail) > 1 and val + 3 >= tail[1]:
                portion2 = self.find_combos_recursive(tail[1], tail[2:])
                self.cached_combos[str(tail[2:])] = portion2
                count += portion2
            if len(tail) > 2 and val + 3 >= tail[2]:
                portion3 = self.find_combos_recursive(tail[2], tail[3:])
                self.cached_combos[str(tail[2:])] = portion3
                count += portion3

            return count

    def find_combos5(self, adapters, partial=None):
        if not partial:
            partial = []
        combo = self.cached_combos.get(str(partial + adapters))
        if combo:
            print(f"Cache hit against {str(partial + adapters)} = {combo}")
            return combo

        if len(adapters) == 1:
            local_combos = 1
            solution = partial + adapters
            print(f"Found leaf node, caching ")
            self.solved_combo_set.add(str(partial + adapters))
        else:
            local_combos = 0
            if adapters[0] + 3 >= adapters[1]:
                partial1 = partial + [adapters[0]]
                local_combo1 = self.find_combos(adapters[1:], partial1)
                self.cached_combos[str(partial1 + adapters[1:])] = local_combo1
                local_combos += local_combo1
            if len(adapters) > 2 and adapters[0] + 3 >= adapters[2]:
                partial2 = partial + [adapters[0]]
                local_combo2 = self.find_combos(adapters[2:], partial2)
                self.cached_combos[str(partial2 + adapters[2:])] = local_combo2
                local_combos += local_combo2
            if len(adapters) > 3 and adapters[0] + 3 >= adapters[3]:
                partial3 = partial + [adapters[0]]
                # local_combos += self.find_combos(adapters[3:], partial3)
                local_combo3 = self.find_combos(adapters[3:], partial3)
                self.cached_combos[str(partial3 + adapters[3:])] = local_combo3
                local_combos += local_combo3

        self.cached_combos[str(partial + adapters)] = local_combos
        return local_combos

    def find_combos4(self, adapters, partial=None):
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
