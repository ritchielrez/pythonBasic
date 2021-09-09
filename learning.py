import math as Math

def isFloat(num, index):
    while index != len(num):
        if(num[index] == '0'):
            index = index + 1
        else:
            return False

    return True

if __name__ == '__main__':
    T = int(input())

    for i in range(T):
        N = float(input())

        n = str(Math.sqrt(N))

        index = n.find('.') + 1

        if isFloat(n, index):
            print('YES')
        else:
            print('NO')

        

            


        

        
        

        

