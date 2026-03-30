class Solution {
public:
    bool isPalindrome(string s) {
        
        /**

        ???Was it a car or a cat I saw?
        s                             e


        */
        
        int l = 0;
        int r = s.size() - 1;

        while (l < r) {

            // skip invalid chars from start
            while (l < r && !isalnum(s[l])) {
                l++;
            }

            // skip invalid chars from end
            while (l < r && !isalnum(s[r])) {
                r--;
            }

            // check if chars match 
            if (tolower(s[l]) != tolower(s[r])) {
                return false;
            }

            // increment pointers
            l++;
            r--;
        }

        return true;
    }
};
