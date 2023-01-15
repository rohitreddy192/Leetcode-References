class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        S =(n*(n+1))//2
        P = (n*(n+1)*(2*n+1))//6
        for i in range(n):
            S -= A[i]
            P -= (A[i]*A[i])
        miss = int((S+P/S)/2)
        rep = miss - S
        return [rep, miss]
