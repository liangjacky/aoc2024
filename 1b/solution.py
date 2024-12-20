from collections import Counter

col1 = []
col2 = []

with open("input.txt") as f:
    input_data = f.readlines()

    for line in input_data:
        split = line.split("   ")
        col1.append(split[0].strip())
        col2.append(split[1].strip())

    col2_counts = Counter(col2)

    res = 0
    for a in col1:
        res += int(a) * col2_counts[a]

    print(res)
