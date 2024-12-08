from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def helper(cur):
            if cur > n:
                return []

            res = []
            for i in range(10):
                if cur + i > n or (cur == 1 and i == 9):
                    return res

                res.append(cur + i)
                child = helper((cur + i) * 10)
                res.extend(child)

            return res
        return helper(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.lexicalOrder(13) == [1,10,11,12,13,2,3,4,5,6,7,8,9])
    print(sol.lexicalOrder(2) == [1, 2])
    print(sol.lexicalOrder(113) == [1,10,100,101,102,103,104,105,106,107,108,109,11,110,111,112,113,12,13,14,15,16,17,18,19,2,20,21,22,23,24,25,26,27,28,29,3,30,31,32,33,34,35,36,37,38,39,4,40,41,42,43,44,45,46,47,48,49,5,50,51,52,53,54,55,56,57,58,59,6,60,61,62,63,64,65,66,67,68,69,7,70,71,72,73,74,75,76,77,78,79,8,80,81,82,83,84,85,86,87,88,89,9,90,91,92,93,94,95,96,97,98,99])