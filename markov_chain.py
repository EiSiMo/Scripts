import random


class MarkovChain:
    def __init__(self, fn):
        self.table = {}
        self.ACCURACY = 1000

        print("[*] reading file")
        with open(fn, "r", encoding="utf8") as file:
            self.data = list(file.read())

    def generate_table(self):
        print("[*] generating table")
        for index, char_ in enumerate(self.data[:-1]):
            next_char = self.data[index + 1]
            if char_ not in self.table.keys():
                self.table[char_] = {}
            if next_char not in self.table[char_].keys():
                self.table[char_][next_char] = 0
            self.table[char_][next_char] += 1
        # convert total amounts to relative values
        for key_char in self.table.keys():
            total = sum(self.table[key_char].values())
            for key_next_char in self.table[key_char].keys():
                absolute = self.table[key_char][key_next_char]
                self.table[key_char][key_next_char] = round(absolute / total * self.ACCURACY)

    def print_table(self):
        print("[*] printing table")
        for key_char in self.table.keys():
            print(f"{repr(key_char)}:")
            for key_next_char in self.table[key_char].keys():
                print(f"\t{repr(key_next_char)}: {self.table[key_char][key_next_char]}")

    def get(self, length):
        print(f"[*] getting {length} chars from table")
        result = [random.choice(list(self.table.keys()))]
        for _ in range(length):
            temp_list = []
            for char_ in self.table[result[-1]].keys():
                probability = self.table[result[-1]][char_]
                temp_list.extend(char_ * probability)
            result.append(random.choice(temp_list))
        return "".join(result)


if __name__ == "__main__":
    chain = MarkovChain(input("file to open: "))
    chain.generate_table()
    print(chain.get(int(input("characters to generate: "))))
