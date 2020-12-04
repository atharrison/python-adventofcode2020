import re


class Day04:
    def __init__(self, data):
        self.raw_data = data
        self.passports = self.load_passports()

    def solve_part1(self):
        valid = 0
        for p in self.passports:
            valid += self.passport_valid(p)

        print(valid)

    def solve_part2(self):
        valid = 0
        for p in self.passports:
            if self.passport_valid(p):
                valid += self.passport_really_valid(p)

        print(valid)

    def passport_valid(self, p):

        required = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
        for code in required:
            if code not in p:
                print("INVALID: " + p)
                return 0

        print("VALID: " + p)
        return 1

    def passport_really_valid(self, p):
        required = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]

        parts = p.split(" ")

        for portion in parts:
            if len(portion) == 0:
                continue
            if not self.validate_portion(portion):
                print("INVALID: " + str(parts) + "\n\n")
                return 0

        print("VALID: " + str(parts) + "\n\n")
        return 1

    def validate_portion(self, portion):
        print(portion)
        kv = portion.split(":", 2)

        if kv[0] == "byr":
            return self.validate_year(kv[1], 1920, 2002)
        elif kv[0] == "iyr":
            return self.validate_year(kv[1], 2010, 2020)
        elif kv[0] == "eyr":
            return self.validate_year(kv[1], 2020, 2030)
        elif kv[0] == "hgt":
            return self.validate_hgt(kv[1])
        elif kv[0] == "hcl":
            return self.validate_hcl(kv[1])
        elif kv[0] == "ecl":
            return self.validate_ecl(kv[1])
        elif kv[0] == "pid":
            return self.validate_pid(kv[1])
        elif kv[0] == "cid":
            return True

    def validate_year(self, v, first, last):
        if len(v) != 4:
            return False

        vint = int(v)
        return vint >= first and vint <= last

    def validate_hgt(self, v):
        if v.endswith("cm"):
            vint = int(v[:-2])
            return vint >= 150 and vint <= 193
        if v.endswith("in"):
            vint = int(v[:-2])
            return vint >= 59 and vint <= 76
        return False

    def validate_hcl(self, v):
        return bool(re.match(r"^\#[0-9a-f]{6}", v))

    def validate_ecl(self, v):
        eye_colors = "amb blu brn gry grn hzl oth".split(" ")
        return v in eye_colors

    def validate_pid(self, v):
        return bool(re.match(r"^[0-9]{9}$", v))

    def load_passports(self):
        passports = []
        multiline = ""
        for line in self.raw_data:
            if len(line) == 0:
                passports.append(multiline)
                multiline = ""
            else:
                multiline = multiline + " " + line

        return passports
