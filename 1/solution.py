col1 = []
col2 = []

with open("input.txt") as f:
    input_data = f.readlines()

    for line in input_data:
        split = line.split("   ")
        col1.append(split[0])
        col2.append(split[1])

    col1.sort()
    col2.sort()
    res = 0
    for a, b in zip(col1, col2):
        res += abs(int(a) - int(b))

    print(res)
