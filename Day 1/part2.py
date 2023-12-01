import itertools
numbers = []
numberWords = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
with open("data.txt") as input:
    for line in input:
        line = line.rstrip()
        split = ["".join(x) for _, x in itertools.groupby(line, key=str.isdigit)]
        i = 0
        j = -1
        num1Flag = False
        num2Flag = False
        while(num1Flag == False or num2Flag == False):
            if(num1Flag == False ):
                element1 = split[i]
                if(element1[0].isnumeric()):
                    num1Flag = True
                    firstNum= element1[0]
                else:
                    firstIndex = float('inf')
                    num = None
                    for index in range(len(numberWords)):
                        subIndex = element1.find(numberWords[index])
                        if(subIndex != -1 and subIndex <= firstIndex):
                            num1Flag = True
                            firstNum = str(index + 1)
                            firstIndex = subIndex
                i +=1
            if(num2Flag == False ):
                element2 = split[j]
                if(element2[-1].isnumeric()):
                    num2Flag = True
                    lastNum = element2[-1]
                else:
                    lastIndex = 0
                    num = None
                    for index in range(len(numberWords)):
                        subIndex = element2.rfind(numberWords[index])
                        if(subIndex != -1 and subIndex >= lastIndex):
                            num = index
                            lastIndex = subIndex
                            num2Flag = True
                            lastNum = str(num + 1)
                j -=1
        number = int(firstNum + lastNum)
        numbers.append(number)
            
print(f"Sum: {sum(numbers)}")