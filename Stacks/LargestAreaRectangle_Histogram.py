'''
Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars.

For simplicity, assume that all bars have same width and the width is 1 unit.

For example, consider the following histogram with 7 bars of

heights {6, 2, 5, 4, 5, 2, 6}. The largest possible rectangle possible is 12
'''

import Stack

# Time Complexity : O(n)
# Space Complexity : O(n)

def find_largest_rect_area_histogram(heights):

    i = 0
    stack = Stack.Stack()
    area = -1
    max_area = -1
    while i < len(heights):

        if stack.size == 0 or heights[stack.peek()] <= heights[i]: # stack is empty of current height greater than stack top
            stack.push(i)
            i = i + 1   # if steadily increasing, keep pushing and incrementing i.
        else:
            top = stack.pop()   # dont increment i.

            # AREA = height * width
            # FINDING AREA OF TOP
            # all elements until top are greater than top. ie) top can fit into the complete range upto i.
            if stack.size == 0:
                area = heights[top.get_data()] * i
            else:
                area = heights[top.get_data()] * (i - stack.peek() - 1)
                # height[i] is not greater than top--> this is hurdle of right
                # top-1 is already captured ---> hurdle of left.
                # Inbetween range = RIGHT - LEFT - 1

        if area > max_area:
            max_area = area

    print max_area

heights = [6,2,5,4,5,2,6]
find_largest_rect_area_histogram(heights)