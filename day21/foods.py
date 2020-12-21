class Food:
    def __init__(self, number, ingredients, possible_allergens):
        self.number = number
        self.ingredients = ingredients
        self.possible_allergens = set()
        self.possible_allergens.update(possible_allergens)

    def __str__(self):
        return f"Food [{self.number}] Ingredients {self.ingredients}, Poss.Allergy {self.possible_allergens}"

    def __repr__(self):
        return self.__str__()


class Ingredient:
    def __init__(self, name, next_to_ingredients, part_of_food):
        self.name = name
        self.seen = 1
        self.seen_with = set(next_to_ingredients)
        self.part_of_foods = set([part_of_food])
        self.determined_allergy = None

    def __str__(self):
        return f"Ingredient [{self.name}] Seen {self.seen}, Seen With {self.seen_with}, Part Of {self.part_of_foods}"

    def __repr__(self):
        return self.__str__()


class Allergen:
    def __init__(self, allergy, part_of_food, possible_ingredients):
        self.allergy = allergy
        self.part_of_foods = set([part_of_food])
        self.possible_ingredients = set(possible_ingredients)
        self.determined_allergy_ingredient = None

    def intersect_ingredients(self, kitchen):
        ing_sets = [
            kitchen.food_map[food_number].ingredients
            for food_number in self.part_of_foods
        ]
        intersected = list(ing_sets[0])
        for ings in ing_sets[1:]:
            intersected = list(set(intersected) & set(ings))

        return set(intersected)

    def __str__(self):
        return f"Allergen [{self.allergy}], Possibly in {self.possible_ingredients}, Part Of {self.part_of_foods}"

    def __repr__(self):
        return self.__str__()
