import itertools

def lex_permutations():
    print ''.join(list(itertools.permutations('0123456789',10))[999999])


if __name__ == '__main__':
    lex_permutations()
