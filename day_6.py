from math import prod

def race_margin_product(races):
    race_data = races.split("\n")[1:-1]
    # times = [int(i) for i in race_data[0].strip().split()[1:]]
    # distances = [int(i) for i in race_data[1].strip().split()[1:]]
    times = int("".join(race_data[0].strip().split()[1:]))
    distances = int("".join(race_data[1].strip().split()[1:]))
    margins = 0
    for j in range(times):
        distance = j * (times - j)
        if distance > distances:
            margins += 1

    return margins


input1 = """
Time:      7  15   30
Distance:  9  40  200
"""

input2 = """
Time:        42     89     91     89
Distance:   308   1170   1291   1467
"""

print(race_margin_product(input2))
