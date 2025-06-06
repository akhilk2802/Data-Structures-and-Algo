class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        '''
        array of string -> words
        int -> k
        return k most frequent strings

        ans -> [] freq from highest to lowest
        Same Freq ? sort by lexicographical order
        '''

        '''
        example -> words = ["i","love","leetcode","i","love","coding"]
        i -> 2
        love -> 2
        leetcode -> 1
        coding -> 1

        return i, love, since both have same fre
        '''

        '''
        approach 1 -> 
        1. Build a freq map 
        2. sort them based on coditions
        3. return the k most elements

        time comp -> build -> O(n), sort -> O(nlogn)
        space comp -> map -> O(n), worst case to build the result array -> O(n)


        approach 2 -> 
        1. Build the freq map
        2. Heapify based on the freq and second priority as sorting the word - of size k
        3. Return the heap

        time comp -> O(n) heapify -> O(klogn)
        space comp -> map -> O(n), heap -> k
        '''

        count = Counter(words)
        heap = []

        for key, freq in count.items():
            heappush(heap, (-freq, key))

        print("heap -> ", heap)
        result = []
        for i in range(k):
            result.append(heappop(heap)[1])

        return result

        # count = Counter(words)
        # max_heap = []

        # for key, val in count.items():
        #     heappush(max_heap, (-val, key))

        # print("max_heap -> ", max_heap)
        # return [heappop(max_heap)[1] for _ in range(k)]