def print_paranthesis(result,pos,open,close,n):

	if close == n:
		print "".join(result)

	if close < open:
		result [pos] = "}"
		print_paranthesis(result,pos+1,open,close+1,n)

	if open < n:
		result[pos] = "{"
		print_paranthesis(result,pos+1,open+1,close,n)

N = 4
Ar = [None]*(2*N)
print_paranthesis(Ar,0,0,0,N)