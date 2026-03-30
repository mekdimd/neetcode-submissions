class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1) store counts in hashmap
        2) sort dict.values and pop k largest values

        k = # of distinct elems
        n = length of arr

        {
            1: 1 (count)
            2: 4 (count)
            3: 3 (count)
        }

        time: O(n + klogk)
        space: O(k)
        """

        count = defaultdict(int)  # default vals of 0
        
        # count # of occurrences per element
        for num in nums:
            count[num] += 1
    
        # Sort by most frequent value
        freq = dict(sorted(count.items(), # (key, value)
            key=lambda item: item[1],     # sort by val i.e. idx 1 of tuple above
            reverse=True))
        

        # return k most frequent elems
        # ALTERNATE list(freq.keys())[:k]
        return [*freq][:k]  # list of keys, range 0-k
