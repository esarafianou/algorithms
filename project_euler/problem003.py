'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def largest_prime_factor(num):
    cur_div = 2
    while num > cur_div:
        if num % cur_div == 0:
            num = num / cur_div
            cur_div = 2
        else:
            cur_div += 1
    print cur_div


if __name__ == '__main__':
    largest_prime_factor(600851475143)

