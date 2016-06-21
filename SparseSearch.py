'''
     Given a sorted array of strings that is interspersed with empty strings, write a method to find the location of a given string.
'''

# O(log n)
def find_start_end_string(Ar, middle):
    left = middle - 1
    result = []

    while left >= 0:
        if Ar[left] != "":
            result.append(left)
            break
        left = left - 1

    if len(result) == 0:
        result.append(None)

    right = middle + 1

    while right < len(Ar):
        if Ar[right] != "":
            result.append(right)
            break

        right = right + 1

    if len(result) == 1:
        result.append(None)

    return result


def find_kstring(Ar, first, last, k):
    if last - first + 1 < 2:
        if Ar[first] == k:
            return first

        elif Ar[last] == k:
            return last
        else:
            return -1

    middle = (first + last) / 2

    if k == Ar[middle]:
        return middle

    if Ar[middle] == "":
        range = find_start_end_string(Ar, middle)

        print range

        if range[0] != None and range[1] != None:

            if k <= Ar[range[0]]:  # go left
                return find_kstring(Ar, first, range[0], k)
            if k >= Ar[range[1]]:
                return find_kstring(Ar, range[1], last, k)

        elif range[0] == None and Ar[range[1]] != None:

            if k < Ar[range[1]]:
                return -1
            else:
                return find_kstring(Ar, range[1], last, k)
        else:
            if k > Ar[range[0]]:
                return -1
            else:
                return find_kstring(Ar, first, range[0], k)
    else:

        if k < Ar[middle]:

            return find_kstring(Ar, first, middle - 1, k)

        else:
            return find_kstring(Ar, middle + 1, last, k)


Ar = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", "", "lion"]
print Ar

for a in Ar:
    if a != "":
        print("Element " + a + " found at : "+str(find_kstring(Ar,0,len(Ar)-1,a)))
