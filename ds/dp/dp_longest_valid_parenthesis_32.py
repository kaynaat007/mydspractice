
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        max_length = 0
        i = 0
        n = len(s)
        while i < n:
            ch = s[i]
            if not stack:
                stack.append(ch)
            else:
                top = stack[-1]
                if top == '(' and ch == '(':
                    stack.append(ch)
                elif top == '(' and ch == ')':
                    stack.pop()
                    if stack and stack[-1].isdigit():
                        val = int(stack.pop())
                        val += 2
                        stack.append(str(val))
                    else:
                        stack.append(str(2))
                elif top == ')' and ch == ')':
                    stack.append(ch)
                elif top == ')' and ch == '(':
                    stack.append(ch)
                elif top.isdigit() and ch == ')':
                    val = int(stack.pop())
                    if not stack:
                        stack.append(str(val))
                        stack.append(ch)
                    else:
                        current_ch = stack[-1]
                        if current_ch == '(':
                            stack.pop()
                            val += 2
                            stack.append(str(val))
                        elif current_ch == ')':
                            stack.append(str(val))
                            stack.append(ch)
                elif top.isdigit() and ch == '(':
                    stack.append(ch)
            i += 1

        n = len(stack)
        for i in range(n):
            count = 0
            while i < n and stack[i].isdigit():
                count += int(stack[i])
                i += 1
            max_length = max(max_length,  count)
        print(stack)
        return max_length


s = Solution()

string = "(()()))))()()()()()()()()()()"
# string = "())()()"
# string = "())()()"
# string = "(()()))))()()()()"
# string = "()(()"
# string = "()())((()"
# string = "())(((()()" # 4
# string = "(()(((()" # 2
# string = "())(((()()" # 4

x = '(())()())'
# x = '())(())()))))))))))))'

# x = "()(())"
# x = "()((()))"

x = ")(((((()())()()))()(()))("
print(s.longestValidParentheses(x))
