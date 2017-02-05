def double_base_palindromes():

    sum_pal = 0
    for i in range(0,1000000):
        bin_num = '{0:b}'.format(i)
        if str(i) == str(i)[::-1] and bin_num == bin_num[::-1]:
            sum_pal += i
    print sum_pal


if __name__ == '__main__':
    double_base_palindromes()

