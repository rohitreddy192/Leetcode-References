class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = list()
        prev = list()
        for i in range(numRows):
            row = list()
            for j in range(i+1):
                if j==0 or j==i:
                    row.append(1)
                else:
                    row.append(prev[j]+prev[j-1])
            prev = row[:]
            res.append(row[:])
        return res
