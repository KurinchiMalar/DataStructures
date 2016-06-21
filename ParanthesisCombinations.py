
def print_paranthesis(result, pos, open, close, n):
    if close == n:
        print "".join(result)
        return
    if close < open:
        result[pos] = "}"
        print_paranthesis(result, pos + 1, open, close + 1, n)

    if open < n:
        result[pos] = "{"
        print_paranthesis(result, pos + 1, open + 1, close, n)


def printParenthesis(n, open, close, result):
    if close >= n:
        print result
        return

    if open < n:
        printParenthesis(n, open + 1, close, result + "(")

    if open > close:
        result = result + ")"
        printParenthesis(n, open, close + 1, result+ ")")


N = 4
Ar = [None] * (2 * N)
# print_paranthesis(Ar,0,0,0,N)

printParenthesis(N, 0, 0,"")

