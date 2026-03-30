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
        """

        sublists = {}

        for s in strs:
            # count chars in s as an array
            # count_arr = [0] * 26
            # for i in range(len(s)):
            #     count_arr[i] += 1

            # # insert into dictionary
            # if count_arr in sublists:
            #     sublists[count_arr].append(count_arr)

            # sublists[count_arr] = count_arr
            
            # ALTERNATE, use sorted str as the key
            sort = ''.join(sorted(s))

            if sort in sublists:
                sublists[sort].append(s)
            else:
                sublists[sort] = [s]


        return sublists.values()

