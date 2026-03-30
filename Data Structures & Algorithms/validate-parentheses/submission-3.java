class Solution {
    /**
    ([{ }])

    next = }
    */

    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char next = s.charAt(i);

            // check if we are adding closing brace
            if (!stack.isEmpty() && lookup(stack.peek()) == next) {
                stack.pop();
            } 
            
            
            // insert next brace
            else {
                stack.push(next);
            }
        }

        // stack should be empty for valid parentheses
        return stack.isEmpty();
    }

    public char lookup(char c) {
        switch (c) {
            case '(': 
                return ')';
            case '{':
                return '}';
            case '[':
                return ']';
            default:
                return 'X';
        }
    }
}
