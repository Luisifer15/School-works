men = []
women = []

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

Wedding.Enqueue(men, 'Sephiroth')
Wedding.Enqueue(women, 'Jenova')
Wedding.Enqueue(men, 'Biggs')
Wedding.Enqueue(women, 'Jessie')
Wedding.Enqueue(men, 'Cid')
Wedding.Enqueue(women, 'Yuffie')
Wedding.Enqueue(men, 'Vincent')
Wedding.Enqueue(women, 'Lucrecia')
Wedding.Enqueue(men, 'Barret')
Wedding.Enqueue(women, 'Marlene')
Wedding.Enqueue(men, 'Cloud')
Wedding.Enqueue(women, 'Tifa')
Wedding.Enqueue(men, 'Zack')
Wedding.Enqueue(women, 'Aerith')

Wedding.Dequeue(men)
Wedding.Dequeue(women)

Wedding.Announce()

