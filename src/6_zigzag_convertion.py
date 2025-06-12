class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zigzag = [[] for _ in range(numRows)]
        r = None
        for i, c in enumerate(s):
            r = i % (2 * numRows - 2)
            if r >= numRows:
                r = 2 * numRows - r - 2
            zigzag[r].append(c)
        return "".join(c for row in zigzag for c in row)