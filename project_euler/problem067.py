def maximum_path_sum():

    array_num  = []
    with open('input067.txt', 'r') as f:
        for line in f:
            array_num.append(map(int, line.split()))
    f.close()

    length = len(array_num)
    total_sum = [0]*length
    total_sum[0] = array_num[0][0]
    i = 0
    for i in range(1,len(array_num)):
        total_sum = calculate(array_num[i], total_sum)

    print max(total_sum)

def calculate(row, total_sum):

        length = len(row)
        temp_sum = list(total_sum)
        for i in range(0, length):
            if i == 0:
                temp_sum[i] += row[i]
            elif i == length - 1:
                temp_sum[i] = total_sum[i-1] + row[i]
            else:
                temp_sum[i] = row[i] + max(total_sum[i-1],total_sum[i])

        return temp_sum


if __name__ == '__main__':
    maximum_path_sum()



