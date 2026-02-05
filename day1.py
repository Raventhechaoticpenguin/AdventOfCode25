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

def main():
    actValue = 50
    answer = 0
    
    file = open('day1input', 'r')

    for ln in file:
        rotation =ln[0]
        rotValue = int(ln[1:])

        actValue = changeValues(actValue, rotation, rotValue)

        if actValue == 0:
            answer += 1

    file.close()
    print(answer)

if __name__ == "__main__":
    main()




