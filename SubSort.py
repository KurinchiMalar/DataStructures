'''
SubSort : Given an array of integers write a method to find indicies m and n , if you sort elements m through n the
array would be sorted. Minimize n-m find the smallest such sequeuence.
'''
def find_range(Ar,n):

    for i in range(1,n):

        if Ar[i-1] > Ar[i]:

            left = i - 1
            break


    for i in range(n-2,-1,-1):

        if Ar[i+1]< Ar[i]:

            right = i+1
            break

    min = left
    max = right
    print "left: "+str(left)
    print "right: " + str(right)
    print "min: " + str(min)
    print "max: " + str(max)
    for i in range(left+1,right):

        if Ar[i] < Ar[min]:
            min = i
        elif Ar[i] > Ar[max]:
            max = i

    while left > 0:

        if Ar[left] <= Ar[min]:
            start = left
            break
        left = left -1

    while right < n:

        if Ar[right] >= Ar[max]:
            end = right - 1
            break
        right = right + 1


    print "range : ( "+str(start)+" , "+str(end)+" ) "
    print "range : ( " + str(Ar[start]) + " , " + str(Ar[end]) + " ) "


Ar = [1,2,4,7,10,11,8,12,5,6,16,18,19,3,100]
find_range(Ar,len(Ar))

