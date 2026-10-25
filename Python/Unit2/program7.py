# Program 7: Postfix Evaluation

def evaluate(exp):
    stack = []

    for ch in exp:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(a // b)

    return stack.pop()

exp = input("Enter postfix expression: ")
print("Result:", evaluate(exp))