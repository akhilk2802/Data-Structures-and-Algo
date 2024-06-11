class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        output = []
        counter = Counter(arr1)

        for num in arr2:
            if num in counter:
                output.extend([num] * counter.pop(num))
        
        rem_elements = sorted(counter.elements())
        output.extend(rem_elements)
            

        return output
