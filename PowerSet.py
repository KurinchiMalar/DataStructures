

def get_power_set(input):

    level = [""]

    for elem in input:
        next_level = []

        for item in level:
            next_level.append(item + elem)

        level.extend(next_level)

    return level

level = get_power_set("ABCDE")
print level










