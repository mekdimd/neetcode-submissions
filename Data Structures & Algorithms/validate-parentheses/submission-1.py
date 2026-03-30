class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        """
        ([{}])
        c = }
        stack = ([{
        
        O(N) time
        O(N) space
        """

        stack = [s[0]]  # start with first char
        for c in s[1:]:    
            # check if top element is in dict
            top = stack[-1] if stack else None
            closing_brace = lookup.get(top, None)
        
            # found closing brace
            if closing_brace == c:
                stack.pop()
            else:
                stack.append(c)
        
        # if stack is empty, we have valid parantheses
        return not stack
            
                
            