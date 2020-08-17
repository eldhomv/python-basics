# while loop to count number of digits in a number


n = int(input('enter a number:'))
count = 0
while n > 0:
    n = n // 10
    count = count + 1
print('the number of digits in the number are:', count)
