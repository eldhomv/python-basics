# while loop to read a number and print sum of its digits

n = int(input('enter a number:'))
p = n
su = 0
while n > 0:
    d = n % 10
    su = d + su
    n = n // 10
print('sum of digits in number', p, 'is', su)
