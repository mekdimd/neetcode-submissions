class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # anagram length -> list of anagrams

        """
        26 letters
        1) 
        for s in strs:
            "acts" -> [1,0,1,...,0]
            insert into sublists with key [1,0,1,...,0]

        3) return values as list

        Time: o(n * k), k = avg of str lengths
        Space: o(n * 26) = o(n)
        
        V1 sorted string

        1) loop through strings
        2) for each string, sort it
        3) insert string s into hashmap using sorted val as key

        return dict.values()

        Time: O(m * nlogn), n = avg str length, m = size of array
        Space: O(m)

        V2 count chars

        1) loop through strings
        2) for each string, count # of occurrences
        3) insert string s into hashmap using # of occurrences as key
            faster than sorting nlogn -> n 


        """

        sublists = {}

        for s in strs:

            sort = ''.join(sorted(s))

            if sort in sublists:
                sublists[sort].append(s)
            else:
                sublists[sort] = [s]


        return sublists.values()

