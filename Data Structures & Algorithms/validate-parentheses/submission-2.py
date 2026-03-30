class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {
            ')' : '(',
            '}' : '{',
            ']': '['
        }
        
        """
        ([{}])
        c = 
        stack = ([{
        
        O(N) time
        O(N) space
        """

        stack = []
        for c in s:    

            # closing brace, check for opening brace
            if c in lookup:
                opening = lookup[c]
                
                # vaid parentheses
                if stack and stack[-1] == opening:
                    stack.pop()
                
                # invalid parentheses e.g. ((]
                else:
                    return False
            else:
                stack.append(c)
        
        # if stack is empty, we have valid parantheses
        return not stack
            
                
            