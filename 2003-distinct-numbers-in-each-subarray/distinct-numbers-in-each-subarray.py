class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        
        # algo - 
        # 1. create a hashMap m 
        # 2. run a sliding window from start to end 
        # 3. check for distinct elements in each window
        # 4. update the ans accordingly 
        # 5. once you reach the end of the array 
        # 6. return the ans 

        n = len(nums)
        ans = []
        freq = defaultdict(int)

        for i in range(k):
            freq[nums[i]] += 1

        ans.append(len(freq))

        for i in range(k, n):
            freq[nums[i-k]] -= 1
            if freq[nums[i-k]] == 0:
                del freq[nums[i-k]]

            freq[nums[i]] += 1
            ans.append((len(freq)))

        return ans