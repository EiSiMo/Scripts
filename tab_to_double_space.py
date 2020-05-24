fn = input("filename: ")
with open(fn, "r") as file:
    data = file.read()


out = []
for c in list(data):
    if c == "\t":
        out.append("  ")
    else:
        out.append(c)

with open(f"{fn}", "w") as file:
    file.write("".join(out))
