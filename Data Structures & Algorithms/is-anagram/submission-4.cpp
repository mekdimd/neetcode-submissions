class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> sCount;
        std::unordered_map<char, int> tCount;

        // both strings must have the same length
        if (s.size() != t.size()) {
            return false;
        }

        // count # of chars in s and t
        for (int i = 0; i < s.size(); i++) {
            // create entry for new char
            if (!sCount.contains(s[i])) { 
                sCount[s[i]] = 0;
            }

            // count chars in s
            sCount[s[i]] += 1;

            // init t count
            if (!tCount.contains(t[i])) {
                tCount[t[i]] = 0;
            }

            // count chars in t
            tCount[t[i]] += 1;
        }

        // check if 2 maps are the same
        return sCount == tCount;
        
    }
};
