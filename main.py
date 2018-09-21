from math import sqrt
def get_bin(code):
    code = str(code)
    lens = len(code)
    bin_to_dec = lambda m, i: 2 ** m
    result = 0
    for i, j in enumerate(code):
        m = lens - i - 1
        if (int(j) == 1):
            result += bin_to_dec(m, j)

    return bin(result)


def get_P_len(code):
    code = str(code)
    n = len(code)

    for i in range(10):
        if(2**i >= i+n+1):
            return i,n

def get_dict(H,code):
    result = {}
    code_index = 0
    for i in range(H):
        index = H - i
        if(sqrt(index) % 1==0 or index==2):
            result[index] = 0
        elif(code_index < len(str(code))):
            result[index] = str(code)[code_index]
            code_index += 1
    return result


code = input('需要转化的二进制:')
P = get_P_len(code)
H = P[0]+P[1]
info =  get_dict(H,code)

m = P[0]-1
arr={}

while m >= 0:
    n = 2**m
    arr[n]=-m-1
    m-=1

# print(info)

sum = 0
for i in arr:
    for j in info:
        if not j <= i:
            if sqrt(j) % 1 != 0 and j != 2:
                if bin(j)[2:][arr[i]] == '1':
                    sum += int(info[j])

        else:
            info[j] =sum % 2
            sum = 0
            break


s=''
for i in info.values():
    s += str(i)

print('信息位：',P[1])
print('校验位：',P[0])
print(s)












