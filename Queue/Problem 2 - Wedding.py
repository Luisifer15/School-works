men = ['Zack', 'Cloud', 'Barret', 'Vincent', 'Cid', 'Biggs']
women = ['Aerith', 'Tifa', 'Marlene', 'Lucrecia', 'Yuffie', 'Jessie']

class Wedding:
    def Enqueue(List, Data):
        if List == men:
            men.insert(0, Data)
        elif List == women:
            women.insert(0, Data)
        else:
            print('Invalid list')

    def Dequeue(List):
        if List == men :
            return men.pop(len(men)-1)
        elif List == women :
            return women.pop(len(women)-1)
        else:
            print('Invalid list')

    def Announce():
        for i in range(len(men)):
                print(Wedding.Dequeue(men), ' and ' , Wedding.Dequeue(women), "!", sep="")

Wedding.Announce()

