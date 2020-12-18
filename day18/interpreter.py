class ExpressionItem:
    def is_digit(self):
        return False

    def is_operator(self):
        return False

    def is_expression(self):
        return False


class Expression(ExpressionItem):
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def is_expression(self):
        return True

    def __str__(self):
        return f"{self.items}"

    def __repr__(self):
        return self.__str__()

    def evaluate(self):
        partial = None
        next_operator = None
        for item in self.items:
            if item.is_digit():
                if not partial:
                    partial = item.value
                else:
                    if next_operator.op == "+":
                        partial = partial + item.value
                    elif next_operator.op == "*":
                        partial = partial * item.value
            elif item.is_operator():
                next_operator = item
            elif item.is_expression():
                if partial is None:
                    partial = item.evaluate()
                else:
                    if next_operator.op == "+":
                        partial = partial + item.evaluate()
                    elif next_operator.op == "*":
                        partial = partial * item.evaluate()

        print(f"Expression {self} evaluated to {partial}")
        return partial


class Digit(ExpressionItem):
    def __init__(self, val):
        self.value = int(val)

    def is_digit(self):
        return True

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return self.__str__()


class Operator(ExpressionItem):
    def __init__(self, val):
        self.op = val

    def is_operator(self):
        return True

    def __str__(self):
        return f"{self.op}"

    def __repr__(self):
        return self.__str__()


class Grouping:
    def __init__(self, *group):
        self.group = group


class EqualPrecedenceInterpreter:
    def __init__(self):
        self.characters = set()
        # {'9', '4', '8', '(', ')', '2', '7', '6', '3', '*', '5', '+', ' '}
        self.digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.operators = ["*", "+"]

    def solve(self, line):
        print(line)
        exp = self.build_expression(line)
        return exp.evaluate()

    def build_expression(self, line):
        exp = Expression()
        idx = 0
        while idx < len(line):
            print(f"Looking at idx.{idx}=>{line[idx]}")
            c = line[idx]
            if c == " ":
                idx += 1
                continue
            elif c in self.digits:
                exp.add(Digit(c))
                idx += 1
            elif c in self.operators:
                exp.add(Operator(c))
                idx += 1
            elif c == "(":
                start = idx + 1
                end = start + self.find_group(line[start:])
                print(
                    f"Grouping found: idx.{idx}=> start={start}, end={end} => {line[start:end]}"
                )
                exp.add(self.build_expression(line[start:end]))
                idx = end + 1
            elif c == ")":
                print("Ugh, close paren not stripped?")
                idx += 1
            else:
                print(f"Unexpected character: [{c}]")
        print(f"Built Expression {exp}")
        return exp

    def find_group(self, portion):
        depth = 1
        idx = 0
        while depth > 0:
            if portion[idx] == "(":
                depth += 1
            elif portion[idx] == ")":
                depth -= 1
            idx += 1

        print(f"Group found {portion[:idx-1]}, returning {idx-1}")
        return idx - 1
