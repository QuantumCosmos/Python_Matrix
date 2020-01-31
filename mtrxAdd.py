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

a = get_val('Enter the first matrix rows....\n')
b = get_val('Enter the second matrix rows....\n')
if len(a) == len(b) and len(a[0]) == len(b[0]):
    c = [[a[i][j]+b[i][j] for j in range(len(a[i]))] for i in range(len(a))]
    d = [[a[i][j]-b[i][j] for j in range(len(a[i]))] for i in range(len(a))]
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
    for r in d:
        print(r)
else:
    print('Matrixes can\'t be added')