'''
You are given n petrol pumps arranged in a circle.
There is a certain quantity of petrol that is available at each pump.
And you are given the amount of petrol required to reach from each station to the next.
You have to find out the petrol pump starting at which you can go around and come back to that particular petrol pump.
'''

# Time Complexity : O(n)
# Space Complexity : O(1)

def get_start_of_tour_petrol_pump(petrol,dist):

    start = len(petrol) - 1
    end = 0

    available = 0
    required = 0

    while end < start:

        if available - required > 0: # we can keep moving
            available += petrol[end]
            required += dist[end]
            end = end + 1
        else:
            start = start - 1  # go back
            available += petrol[start]
            required += dist[start]



    return petrol[start]

#petrol = [3,6,9,5]
#dist = [10,5,2,6]

petrol = [4,3,5,6]
dist = [3,5,2,7]
print "Start from station: "+str(get_start_of_tour_petrol_pump(petrol,dist))
