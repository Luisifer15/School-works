x = [2, 5, 13, 17, 3, 89, 3, 5, 2, 90, 5, 65]
y = [69, 420, 21, 6969, 420, 5, 10, 69, 69]
z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = int(input('Enter value: '))
arr = input('Select Array [x] [y] [z]: ')


if arr == 'x':
    counter = x.count(n)
    print('Value:', n, 'in Array:', arr, 'appears', counter, 'times')
elif arr == 'y':
    counter = y.count(n)
    print('Value:', n, 'in Array:', arr, 'appears', counter, 'times')
elif arr == 'z':
    counter = z.count(n)
    print('Value:', n, 'in Array:', arr, 'appears', counter, 'times')
else: 
    print('Array not found')

input("Press Enter to exit")