numbers = []
with open("data.txt") as input:
    for line in input:
        num1Flag = False
        num2Flag = False
        i = 0
        j = -1
        while(num1Flag == False or num2Flag == False):
            if(num1Flag == False ):
                char1 = line[i]
                if(char1.isnumeric()):
                    num1Flag = True
                else:
                    i += 1
            if(num2Flag == False):
                char2 = line[j]
                if(char2.isnumeric()):
                    num2Flag = True
                else:
                    j -= 1
        number = int(char1 + char2)
        numbers.append(number)

print(f"Sum: {sum(numbers)}")