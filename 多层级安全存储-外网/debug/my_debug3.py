class Solution:
    def generateMatrix(self, n: int):
        res = [[0 for _ in range(n)] for _ in range(n)]
        up, left, num = 0, 0, 1
        down, right = n - 1, n - 1
        while True:
            for i in range(left, right + 1):
                res[up][i] = num
                num += 1
            up += 1
            if up > down:
                break
            for i in range(up, down + 1):
                res[i][right] = num
                num += 1
            right -= 1
            if right < left:
                break
            for i in range(left, right + 1)[::-1]:
                res[down][i] = num
                num += 1
            down -= 1
            if down < up:
                break
            for i in range(up, down + 1)[::-1]:
                res[i][left] = num
                num += 1
            left += 1
            if left > right:
                break
        return res


a = Solution()
print(a.generateMatrix(3))
