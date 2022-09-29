y = [[1, 2, 3], [5, 6, 7], [9, 10, 11]]
z = [[31, 32, 33], [55, 56, 57], [19, 10, 11]]

def sum():
    for i in range(len(z)):
        for ii in range(len(z[i])):
            print('y[',i,'][',ii,'] + z[',i,'][',ii,'] =',y[i][ii]+z[i][ii])

def diff():
    for i in range(len(z)):
        for ii in range(len(z[i])):
            print('z[',i,'][',ii,'] - y[',i,'][',ii,'] =',z[i][ii]-y[i][ii])

def prod():
    for i in range(len(z)):
        for ii in range(len(z[i])):
            print('y[',i,'][',ii,'] * z[',i,'][',ii,'] =',y[i][ii]*z[i][ii])

print('FUNCTION A:')
sum()

print('\nFUNCTION B:')
diff()

print('\nFUNCTION C:')
prod()