print('enter a expression:')
n1, opr, n2 = [(x) for x in input('  ').split()]
n1 = int(n1)
n2 = int(n2)
print(n1, opr, n2, '=', end='')
if opr == '+':
    print(n1 + n2)
elif opr == '-':
    print(n1 - n2)
elif opr == '*':
    print(n1 * n2)
elif opr == '/':
    print(n1 / n2)
elif opr == '%':
    print(n1 % n2)
else:
    print('invalid')
