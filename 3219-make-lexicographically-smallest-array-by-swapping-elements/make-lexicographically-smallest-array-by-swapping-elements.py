class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        order = []

        for i in range(n):
            order.append((nums[i], i))
        order = sorted(order, key=lambda x: x[0])

        group = [[order[0]]]
        for i in range(1, n):
            if order[i][0] - order[i - 1][0] <= limit:
                group[-1].append(order[i])
            else:
                group.append([order[i]])

        for i in group:
            index = [y for x, y in i]
            index.sort()
            values = sorted(x for x, y in i)
            for idx, value in zip(index, values):
                nums[idx] = value

        return nums
        