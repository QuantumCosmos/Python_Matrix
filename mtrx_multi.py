def inp(n):
    try:
        return [float(i) for i in input('Enter row '+str(n+1)+'\t Type "." to stop giving rows\n').
        split(',') if i!='.']
    except ValueError:
        print('Illegal CCharacter')
        return inp(n)

def get_val(s):
    print(s)
    a = []
    s = inp(len(a))
    l = len(s)
    a.append(s)
    while True:
        s = inp(len(a))
        if s==[]:
            break
        else:
            if len(s) == l and s[len(s)-1] != '':
                a.append(s)
            else:
                print('All Rows should have same number of Numbers.........')
                print('Enter numbers correctly\n')
    return a

def mtrx_multi(a,b):
    if len(a[0]) == len(b):
        c = []
        for _ in range(len(a)):
            c.append([0 for _ in range(len(b[0]))])
        for k in range(len(a)):
                for i in range(len(b[0])):
                    for j in range(len(a[0])):
                            c[k][i] = c[k][i] + a[k][j]*b[j][i]
    else:
        print('Matrixes can\'t be multiplied')
    return c

a = get_val('Enter the first matrix rows....\n')
b = get_val('Enter the second matrix rows....\n')
c = mtrx_multi(a,b)
print('First Matrix is...')
for r in a:
    print(r)
print('Second Matrix is...')
for r in b:
    print(r)
print('The New Matrix after addition is...')
for r in c:
    print(r)
print('The New Matrix after substraction is...')



# Enter the first matrix rows....

# Enter row 1      Type "." to stop giving rows
# 1,2,3
# Enter row 2      Type "." to stop giving rows
# 2,3,
# Illegal CCharacter
# Enter row 2      Type "." to stop giving rows
# 2,3
# All Rows should have same number of Numbers.........
# Enter numbers correctly

# Enter row 2      Type "." to stop giving rows
# 2,3,4
# Enter row 3      Type "." to stop giving rows
# .
# Enter the second matrix rows....

# Enter row 1      Type "." to stop giving rows
# 1,2,3
# Enter row 2      Type "." to stop giving rows
# 2,3,4
# Enter row 3      Type "." to stop giving rows
# 3,4,5
# Enter row 4      Type "." to stop giving rows
# .
# [0, 0, 0]
# [0, 0, 0]
# First Matrix is...
# [1.0, 2.0, 3.0]
# [2.0, 3.0, 4.0]
# Second Matrix is...
# [1.0, 2.0, 3.0]
# [2.0, 3.0, 4.0]
# [3.0, 4.0, 5.0]
# The New Matrix after Multiplication of First with Second is...
# [14.0, 20.0, 26.0]
# [20.0, 29.0, 38.0]
# The New Matrix after substraction is...
