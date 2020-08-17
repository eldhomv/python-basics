# while loop - check if a number is a palindrome

n = int(input('enter a number:'))
temp = n
rev = 0
while n > 0:
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
if rev == temp:
    print('the number is a palindrome')
else:
    print('the number isnt a palindrome')
