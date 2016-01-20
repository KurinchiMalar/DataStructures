'''
Number of railway-platforms:

    At a rail-station, we have time-table of trains arrival and departure.
    We need to find the minimum number of platforms so that all the trains can be accomodated as per their schedule.
'''

# Time Complexity : O(n)
# Space Complexity : O(n)

def get_max_platforms_required(arr,dep):

    final = sorted(arr+dep,key=sort_key)# invisible argument is passed , which is every item in list.
    print "Sorted: "+str(final)


    count = []

    for item in final:
        if item in arr:
            count.append(1)
        else:
            count.append(-1)

    print count

    for i in range(1,len(count)):

        count[i] = count[i-1] + count[i]
    print count

    max_val = -1
    for i in range(0,len(count)):
        if count[i] > max_val:
            max_val = count[i]

    return max_val   # this indicates the optimal number of platforms required.


def sort_key(time):
    hour,minute = time.split(':')
    return int(hour),int(minute)

arr  = ['9:00',  '9:40', '9:50',  '11:00', '15:00', '18:00']
dep  = ['9:10', '12:00', '11:20', '11:30', '19:00', '20:00']

print "Max platforms required: "+str(get_max_platforms_required(arr,dep))