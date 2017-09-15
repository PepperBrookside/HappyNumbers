'''A happy number is defined by the following process.
Starting with any positive integer,
replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers,
while those that do not end in 1 are unhappy numbers.'''

def start():
    try:
        a = int(input("Enter a number: "))
        print(happy(a))
    except ValueError:
        start()

def happy(num):
    if num == 4 or num == 0: return "Unhappy"
    if num == 1: return "Happy"
    num = str(num)
    total = 0
    for i in num:
        total += int(i)**2
    return happy(total)

start()
