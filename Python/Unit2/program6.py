# Program 6: Infix to Postfix

def convert(exp):
    stack = []
    result = ""
    priority = {'+': 1, '-': 1, '*': 2, '/': 2}

    for ch in exp:
        if ch.isalnum():
            result += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            if stack:
                stack.pop()
        else:
            while (stack and stack[-1] != '(' and
                   priority.get(stack[-1], 0) >= priority.get(ch, 0)):
                result += stack.pop()
            stack.append(ch)

    while stack:
        result += stack.pop()

    return result

exp = input("Enter infix expression: ")
print("Postfix:", convert(exp))