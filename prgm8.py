# nested loop - read a list and print sum of digits of all numbers in list

lst = [121, 450, 671, 2345, 442]
print('', 'number\tsum of digits')
for n in lst:
    temp = n
    s = 0
    while n > 0:
        d = n % 10
        s = s + d
        n = n // 10
    print('', '%d\t%d' % (temp, s))
