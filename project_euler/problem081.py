#import pdb

def prob_81():

    with open('p081_matrix.txt', 'r') as f:

        DP = []
        for i, line in enumerate(f.readlines()):
            DP.append(map(int, line.split(',')))
            for j in range(0, len(DP[i])):
                if i == 0 and j == 0:
                    pass
                elif i == 0:
                    DP[i][j] += DP[i][j-1]
                elif j == 0:
                    DP[i][j] += DP[i-1][j]
                else:
                    DP[i][j] += min(DP[i-1][j], DP[i][j-1])
        print DP[-1][-1]
#        pdb.set_trace()


if __name__ == '__main__':
    prob_81()
