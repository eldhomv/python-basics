# break statement , else suite - program to check a no is prime or not

num = int(input('enter a number:'))
i = 2
while i <= num / 2:
    if num % i == 0:
        print(num, 'is not prime')
        break
    i += 1
else:
    print(num, 'is prime')
