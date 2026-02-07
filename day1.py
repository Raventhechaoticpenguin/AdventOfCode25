answer = 0

def changeValues(actValue, rotation, rotValue):
    #como o 0 é considerado como um pointer, ele também ira fazer parte da contagem
    #sendo essa a razão de ser de recomeçar ou 1 antes ou 1 depois dp suposto
    if rotation == 'L':
        for i in range(rotValue):
            if actValue == 0:
                actValue = 100
            actValue -= 1
    elif rotation == 'R':
        for i in range(rotValue):
            if actValue == 99:
                actValue = -1
            actValue += 1

    #print(f"Valor atual: {actValue}")
    return actValue

#versao para 2 estrelas, errada porque está a contar numeros 
#a mais neste caso 20

def changeValues2(actValue, rotation, rotValue):
    global answer

    if rotation == 'L':
        for i in range(rotValue):
            if actValue == 0:
                actValue = 100
                answer += 1
            actValue -= 1
    elif rotation == 'R':
        for i in range(rotValue):
            if actValue == 99:
                actValue = -1
                answer += 1
            actValue += 1

def changeValues3(actValue, rotation, rotValue):
    global answer

    if rotation == 'L':
        actValueAux =  actValue - rotValue
        if actValueAux < 0:
            actValue = 100 + actValueAux
            while actValue < 0:
                actValue += 100
                answer += 1
            answer += 1
        else:
            actValue = actValueAux
    elif rotation == 'R':
        actValueAux = actValue + rotValue
        if actValueAux > 99:
            actValue = 100 - actValueAux
            while actValue > 99:
                actValue -= 100
                answer += 1
            answer += 1
        else:
            actValue = actValueAux

    #print(f"Valor atual: {actValue}")
    return actValue 

#solução para 2 estrelas sem dar 20 a mais -.-
#portanto mesma logica ue o primeiro que fiz, mas deixa chegar 
#às estremidades e só altera aí
def changeValues4(actValue, rotation, rotValue):
    global answer

    if rotation == 'L':
        for i in range(rotValue):
            actValue -= 1
            if actValue == -1:
                actValue = 99

            if actValue == 0:
                answer += 1

    elif rotation == 'R':
        for i in range(rotValue):
            actValue += 1
            if actValue == 100:
                actValue = 0

            if actValue == 0:
                answer += 1

    return actValue


def main():
    actValue = 50
    global answer
    
    file = open('day1input', 'r')

    for ln in file:
        rotation = ln[0]
        rotValue = int(ln[1:])

        actValue = changeValues4(actValue, rotation, rotValue)

        #descomentar para 1 estrela
        '''
        if actValue == 0:
            answer += 1
        '''

    file.close()
    print(answer)

if __name__ == "__main__":
    main()




