'''
2520 is the smallest number that can be divided by each
of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20
'''

def gcd(a,b):
    while (b):
        a, b =  b, a % b
    return a

def lcm():
    lcm = 1
    for i in range(1,20):
        lcm = (i*lcm) // gcd(i,lcm)
    print lcm
    return



if __name__ == '__main__':
    lcm()

'''
Note:
    The smallest number evenly divisable by a set of
    numbers is the least common multiple(LCM) of these numbers.
    The LCM of N numbers is defined by recurively computing the
    LCM of 2 numbers:
    LCM (a, b, c)  = LCM(a, LCM(b,c))
'''
