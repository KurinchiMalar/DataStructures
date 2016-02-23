'''
Write a function to generate all possible n pairs of balanced parentheses.

For example, if n=1
{}
for n=2
{}{}
{{}}
'''
# Time Complexity : O(n)
# Space Complexity : O(1)

def print_all_combinations_paranthesis(result,n,open,close):

    if close == n:
        print result

        return

    else:
        if close < open:
            #result.append(")") # this is mutable.
            print_all_combinations_paranthesis(result+")",n,open,close+1) # this is immutable., every time new string created.

        if open < n :
            #result.append("(")
            print_all_combinations_paranthesis(result+"(",n,open+1,close)

def print_all_combinations_paranthesis_m2(source,pos,n,open,close):

    if close == n:
        source = "".join(source)
        print source
        return

    else:
        if close < open:
            source[pos] = ")"
            print_all_combinations_paranthesis_m2(source,pos+1,n,open,close+1)

        if open < n :
            #result.append("(")
            source[pos] = "("
            print_all_combinations_paranthesis_m2(source,pos+1,n,open+1,close)
def invoke(n):
    source = [None]* (n*2)
    print "Method1 - without pos tracking"
    print_all_combinations_paranthesis("",n,0,0)
    print "Method2 - with pos tracking"
    print_all_combinations_paranthesis_m2(source,0,n,0,0)


invoke(3)