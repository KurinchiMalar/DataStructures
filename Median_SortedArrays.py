# Find the median of two sorted arrays


def calc_length(first1, last1, first2, last2):
    return ((last1 - first1 + 1) + (last2 - first2 + 1))


def median_iterative(Ar1,Ar2,first1, last1, first2, last2, length):
    mid = length / 2
    ptr1 = first1
    ptr2 = first2
    median = Ar1[ptr1]
    for i in range(mid):
        if Ar1[ptr1] < Ar2[ptr2]:
            median = Ar1[ptr1]
            ptr1 = ptr1 + 1
        else:
            median = Ar2[ptr2]
            ptr2 = ptr2 + 1

    return median


def median_binary_search(Ar1, Ar2, first1, last1, first2, last2):

    print("(first1,last1): "+str(first1)+" , "+str(last1))
    print("(first2,last2): "+str(first2)+" , "+str(last2))
    length = calc_length(first1, last1, first2, last2)

    if length <= 4:
        return median_iterative(Ar1,Ar2,first1, last1, first2, last2, length)

    middle1 = (first1 + last1) / 2
    middle2 = (first2 + last2) / 2

    print("Comparing : "+str(Ar1[middle1])+" and "+str(Ar2[middle2]))
    if Ar1[middle1] < Ar2[middle2]:
        return median_binary_search(Ar1, Ar2, middle1, last1, first2, middle2)
    else:
        return median_binary_search(Ar1, Ar2, first1, middle1, middle2, last2)



Ar1 = [1, 7], 9, 10]
Ar2 = [2, [5, 8, 11]


#Ar1 = [1,3,7,9,10,25]
#Ar2 = [2,5,6,8,11,13]


temp = Ar1 + Ar2
print(sorted(temp))

# 1 2 3 5 6 7 8 9 10 11
n1 = len(Ar1)
n2 = len(Ar2)

print("Median: "+str(median_binary_search(Ar1,Ar2,0,n1-1,0,n2-1)))
