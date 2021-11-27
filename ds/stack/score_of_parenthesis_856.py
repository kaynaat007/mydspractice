

def scoreOfParentheses(S) -> int:

    stack = []
    ans = 0

    for ch in S:
        if ch == '(':
            stack.append(ch)

        elif ch == ')':

            t = stack[-1]
            if t == '(':
                stack.pop()
                stack.append(1)
            else:
                v = t
                stack.pop()
                while stack and stack[-1] != '(':
                    v = v + stack[-1]
                    stack.pop()
                v = 2 * v
                if stack:
                    stack.pop()
                stack.append(v)

    while stack:
        ans = ans + stack[-1]
        stack.pop()

    return ans

S = '((())(()))'
# S = ''
print(scoreOfParentheses(S))
