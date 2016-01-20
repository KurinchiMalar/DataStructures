
'''
You are given n activities with their start and finish times.
Select the maximum number of activities that can be performed by a single person,
    assuming that a person can only work on a single activity at a time.
'''

# Time Complexity : O(n)

def get_max_activities_performed_by_single_person(start,finish):


    result = []

    result.append(start[0])

    j = 0 # for the finish

    for i in range(1,len(start)):

        if start[i] >= finish[j]:
            result.append(start[i])
            j = i


    return result

s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 7 , 9 , 9]

#s = [ 5 , 8 , 5 , 0, 3 , 1]
#f = [ 9 , 9 , 7 , 6, 4, 2]

start_sortedbasedonfinish = [x for (y,x) in sorted(zip(f,s))]
finish_sorted = sorted(f)

print start_sortedbasedonfinish
print finish_sorted
print "Max activities by single person: "+str(get_max_activities_performed_by_single_person(start_sortedbasedonfinish,finish_sorted))



