with open(input("file1: "), "r", encoding="utf8") as file:
    list1 = file.readlines()

with open(input("file2: "), "r", encoding="utf8") as file:
    list2 = file.readlines()

list1.extend(list2)
out = list(set(list1))
out.sort()

with open(input("file_save: "), "w", encoding="utf8") as file:
    file.writelines(out)
