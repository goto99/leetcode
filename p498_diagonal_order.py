class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        result = []
        m = len(mat)
        n = len(mat[0])
        for i in range(m + n):
            if i % 2 == 0:
                for j in range(min(i + 1, n)):
                    if i - j < m:
                        result.append(mat[i-j][j])

            else:
                for j in range(min(i + 1, m)):
                    if i - j < n:
                        result.append(mat[j][i-j])

        return result

def main():
    s = Solution()
    res = s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])
    print(res)

if __name__ == '__main__':
    main()