import re
from .foods import Allergen, Food, Ingredient
import copy


class Day21:
    def __init__(self, data):
        self.raw_data = data
        self.ingredient_map = {}
        self.food_map = {}
        self.allergen_map = {}
        self.determined_allergen_map = {}

        self.load_foods()

    def solve_part1(self):
        no_allergens_count = 0
        no_allergens_food = set()
        # for food in self.food_map.items():
        #     print(food)

        # for ing in self.ingredient_map.items():
        #     print(ing)

        for allergy, a in self.allergen_map.items():
            print(allergy)
        #     if len(food.possible_allergens) == 0:
        #         print(f"---> food {food} has no allergens")
        #         no_allergens_count += food.seen
        #         no_allergens_food.add(food.name)

        # print(f"Total non-allergens: {no_allergens_count} from {no_allergens_food}")

        made_new_determination = False
        loop_count = 0
        while len(self.determined_allergen_map) != len(self.allergen_map):
            loop_count += 1
            print(f"--> Looping over Allergens Time {loop_count}...")
            made_new_determination = self.determine_allergens()

        for _, a in self.allergen_map.items():
            if a.determined_allergy_ingredient:
                print(
                    f"Allergy {a.allergy} must be from {a.determined_allergy_ingredient.name}"
                )

        seen = 0
        for ing, i in self.ingredient_map.items():
            if i.determined_allergy:
                continue
            else:
                seen += i.seen
                # print(f"Ingredient {ing} not an allergen. Seen {i.seen}")

        print(f"Total Seen: {seen}")

    def determine_allergens(self):
        made_new_determination = False
        for _, a in self.allergen_map.items():
            if a.determined_allergy_ingredient is not None:
                continue

            ingredient_intersection = a.intersect_ingredients(self)
            if len(ingredient_intersection) == 1:
                i = self.ingredient_map[list(ingredient_intersection)[0]]
                a.determined_allergy_ingredient = i
                i.determined_allergy = a
                made_new_determination = True
                self.determined_allergen_map[a.allergy] = a
                print(f"DETERMINED(1) that {a.allergy} is from {i.name}")
            else:
                print(f"Looking at intersection {ingredient_intersection}...")
                potential_singles = set()
                for ing in ingredient_intersection:
                    i = self.ingredient_map[ing]
                    if i.determined_allergy is None:
                        potential_singles.add(ing)
                if len(potential_singles) == 1:
                    i = self.ingredient_map[list(potential_singles)[0]]
                    a.determined_allergy_ingredient = i
                    i.determined_allergy = a
                    made_new_determination = True
                    self.determined_allergen_map[a.allergy] = a
                    print(f"DETERMINED(2) that {a.allergy} is from {i.name}")
                else:
                    print(
                        f"Itersection of {ingredient_intersection} undterminable. Potential singles: {potential_singles}"
                    )
        return made_new_determination

    def solve_part2(self):
        # Assume part 1 solved
        allergy_ingredients = [
            a.determined_allergy_ingredient.name
            for a in self.determined_allergen_map.values()
        ]
        allergy_ingredients.sort()

        allergy_ingredient = []
        for a in self.determined_allergen_map.values():
            print(f"{a.allergy} : {a.determined_allergy_ingredient.name}")
            allergy_ingredient.append((a.allergy, a.determined_allergy_ingredient.name))

        print(allergy_ingredient)
        sorted_allergy_ingredient = sorted(allergy_ingredient, key=lambda x: x[0])
        print(sorted_allergy_ingredient)
        sorted_ingredients = [t[1] for t in sorted_allergy_ingredient]
        print(",".join(sorted_ingredients))

    def load_foods(self):
        # food_ingredient_pattern = re.compile("(w+)? \(contains (w+)?,\)$")
        for food_number, line in enumerate(self.raw_data):
            line_split = line.split("(contains ")
            ingredient_section = line_split[0]
            allergen_section = line_split[1][0:-1]

            ingredients = ingredient_section.strip().split(" ")
            allergens = allergen_section.strip().split(" ")
            allergens = [a.replace(",", "") for a in allergens]

            # print(f"Food {food_number}: {ingredients}, Allergens: {allergens}")
            f = Food(food_number, ingredients, allergens)
            self.food_map[f.number] = f
            for ing in ingredients:
                if ing in self.ingredient_map.keys():
                    # print(f"Food {food_number} has ingredient {ing} seen again.")
                    i = self.ingredient_map[ing]
                    i.seen += 1
                    i.seen_with.update(ingredients)
                    i.part_of_foods.add(f.number)

                else:
                    i = Ingredient(ing, ingredients, food_number)
                    self.ingredient_map[ing] = i
                    self.food_map[f.number] = f

            for allergy in allergens:
                if allergy in self.allergen_map.keys():
                    a = self.allergen_map[allergy]
                    a.part_of_foods.add(food_number)
                    a.possible_ingredients.update(ingredients)
                else:
                    a = Allergen(allergy, food_number, ingredients)
                    self.allergen_map[allergy] = a

    def list_union(self, l1, l2):
        final = [item for item in l1 if item in l2]
        print(f"Union of {l1} and {l2} is {final}")
        return final
