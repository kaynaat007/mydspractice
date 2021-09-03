
def longestValidParentheses(self, s: str) -> int:
    stack = []
    i = 0
    n = len(s)
    max_len = 0
    curr_len = 0
    while i < n:

        max_len = max(curr_len, max_len)
        if not stack:
        ch = s[i]
        if ch == ')' and not stack:
            i = i + 1
            continue
        elif ch == ')' and stack and stack[-1] == ')':
            stack.append(ch)
            i = i + 1
            continue
        elif ch == ')' and stack and stack[-1] == '(':
            stack.append(ch)
            stack.pop()
            curr_len += 2
            i = i + 1
            continue
        elif ch == '(' and not stack:
            stack.append('(')
            i = i + 1
        elif ch == '(' and stack and stack[-1] == '(':
            stack.append('(')
            i = i + 1
        elif ch == '(' and stack and stack[-1] == ')':
            stack.append('(')
            i = i + 1

    max_len = max(curr_len, max_len)
    return max_len





