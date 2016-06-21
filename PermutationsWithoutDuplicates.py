def insert_in_all_pos(item, first):
    result = []
    for i in range(len(item)):
        result.append(item[:i] + first + item[i:])
    result.append(item + first)
    return result


def getPerms(input):
    if input == None:
        return None

    if input == "":
        return [""]

    first = input[:1]

    remaining_perms = getPerms(input[1:])

    result = []
    for item in remaining_perms:
        result.extend(insert_in_all_pos(item, first))

    return result

input = "abc"
print(str(getPerms(input)))