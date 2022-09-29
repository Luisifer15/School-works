y = [[1, 2, 3], [5, 6, 7], [9, 10, 11]]
z = [[31, 32, 33], [55, 56, 57], [19, 10, 11]]

#goes through x axis
for i in range(len(z)):
    #goes through y axis
    for j in range(len(z[i])):
        #checks if element in array is even (value modulo 2 always equals to zero if even)
        if (z[i][j]%2 == 0):
            print('z[',i,'][',j,'] is',z[i][j],'It is an even number!')
        #if not then it defaults to odd
        else: 
            print('z[',i,'][',j,'] is',z[i][j],'It is an odd number!')