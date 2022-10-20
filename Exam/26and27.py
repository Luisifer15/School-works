x=[2, 5, 10, 12, 3, 9, 8, 7, 4, 1, 11, 6]

class array:
    def Custominsert(AData, AIndex):
        x.insert(AIndex, int(AData))

    def CustomDelete(AData):
        x.remove(AData)

    def CustomSearch(AData):
        for i in range(len(x)):
            if AData == x[i]:
                print(AData, 'is found at x[', i,']')
                return x[i]

    def CustomSorter():
        lowestvalue=None
        SorterContainer=[]
        for i in range(len(x)):
            lowestvalue=x[0]
            for j in range(len(x)):
                if x[j] < lowestvalue:
                    lowestvalue = x[j]
            SorterContainer.append(lowestvalue)
            x.remove(lowestvalue)
        for i in range(len(SorterContainer)):
            x.append(SorterContainer[i])
        print('The sorted array is ', x)
        

array.CustomSorter()
array.CustomDelete(1)
print(x)
array.Custominsert(13, 12)
print(x)
array.CustomSearch(5)

