'''
    Given an array A[], write a function that segregates even and odd numbers.

    The functions should put all even numbers first and then odd numbers.
'''

# Time Complexity : O(n)
def separate_even_odd(Ar):
    even_ptr = 0
    odd_ptr = len(Ar)-1

    while even_ptr < odd_ptr:

        while even_ptr < odd_ptr and Ar[even_ptr] % 2 == 0:
            even_ptr = even_ptr + 1
        while even_ptr < odd_ptr and Ar[odd_ptr] % 2 == 1:
            odd_ptr = odd_ptr -1
        # now odd and even are positioned appropriately.

        #if Ar[odd_ptr] % 2 == 0 and Ar[even_ptr] % 2 == 1:
        Ar[odd_ptr],Ar[even_ptr] = Ar[even_ptr],Ar[odd_ptr]
        odd_ptr = odd_ptr-1
        even_ptr = even_ptr+1
    return Ar

Ar = [12,34,45,9,8,90,3]
#Ar = [1,2]
print ""+str(separate_even_odd(Ar))