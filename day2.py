sum = 0

#split do primeiro e ultimo elemento
def splitID(ids):
       
    ids2 = ids.split('-')
    print(f"todos os ids: {ids2}")
    findID(ids2[0], ids2[1])

#encontra os ids que tem 2 num iguais seguidos
def findID(id1, id2):
    id1 = int(id1)
    id2 = int(id2)

    diff = id2 - id1
    #verifyingFlag = False
    falseIds = []
    
    while diff > -1:

        num1 = str(id1)[0:len(str(id1))//2]
        #print(f"num1: {num1}")
        num2 = str(id1)[len(str(id1))//2:]
        #print(f"num2: {num2}")

        if num1 == num2:
            falseIds.append(id1)
            print(falseIds)
        id1 += 1
        diff -= 1

    sumIds(falseIds)

    return 0

def sumIds(falseIds):
    global sum

    for id in falseIds:
        sum += int(id)

    return sum

def main():

    global sum
    file = open('day2input.txt', 'r')

    megaLine = file.readline()

    file.close()

    ids = megaLine.split(',')
    print(f"ids: {ids}")

    for id in ids:
        splitID(id)
    
    print(sum)

if __name__ == "__main__":
    main()
