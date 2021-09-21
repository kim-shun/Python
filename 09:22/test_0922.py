for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            break
        else:
            print(n,'is a prime number')
#3 is a prime number
#4 equals 2 * 2
#5 is a prime number
#5 is a prime number
#5 is a prime number
#6 equals 2 * 3
#7 is a prime number
#7 is a prime number
#7 is a prime number
#7 is a prime number
#7 is a prime number
#8 equals 2 * 4
#9 is a prime number
#9 equals 3 * 3

print()

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            break
    else:
        print(n,'is a prime number')

#2 is a prime number
#3 is a prime number
#4 equals 2 * 2
#5 is a prime number
#6 equals 2 * 3
#7 is a prime number
#8 equals 2 * 4
#9 equals 3 * 3

print()

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            continue
    else:
        print(n,'is a prime number')
'''
2 is a prime number
3 is a prime number
4 equals 2 * 2
4 is a prime number
5 is a prime number
6 equals 2 * 3
6 equals 3 * 2
6 is a prime number
7 is a prime number
8 equals 2 * 4
8 equals 4 * 2
8 is a prime number
9 equals 3 * 3
9 is a prime number
'''
print()

from datetime import date
now = date.today()

#優先度の低さ順
#DEBUG INFO WARNING ERROR CRITICAL
print(now) #2021-09-22
