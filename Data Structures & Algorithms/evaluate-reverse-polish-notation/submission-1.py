class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = ('+', "-", "*", "/")
        
        for t in tokens:
            # operation
            if t in symbols:
                right = int(stack.pop())
                left = int(stack.pop())
                
                match t: 
                    case '+':
                        stack.append(left + right)
                    case '-':
                        stack.append(left - right)
                    case '*':
                        stack.append(left * right)
                    case '/':
                        # assuming division by 0 will not occur
                        # e.g. -3 // 2 = -2, but we want -1
                        # so use int(-3/2)
                        stack.append(int(left/right))
            # number
            else:
                stack.append(t)

        # top of stack has result
        return int(stack[0])