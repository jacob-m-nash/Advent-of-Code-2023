SYMBOLS = ['@', '*', '$', '&', '=', '/', '-', '+', '#', '%'] 

partNumbers = []
symbol = []
j = 0
with open("data.txt") as input:
    schematic  = [line.rstrip() for line in input]
    j = 0
    while j < len(schematic):
        line = schematic[j]
        p1 = 0
        p2 = 1
        while p1 < len(line) :
            char1 = line[p1]
            num = char1
            windowLength = 3
            p2 = p1 
            if(char1.isnumeric()):
                if(p2 + 1 < len(line)):
                    p2 += 1
                    while (p2 < len(line)):
                        char2 = line[p2]
                        if( not char2.isnumeric()):
                            break
                        num += char2
                        p2 += 1
                        
                adjacentSymbols = ""
                begin = p1
                end = p2 
                if(p1 > 0):
                    begin = p1 - 1
                if(p2 >= len(line)):
                    end = p2 - 1

                if( j > 0):
                    top = schematic[j -1][begin:end + 1]
                    adjacentSymbols += top
                    #search top
                if(p2 < len(line) - 1):
                    right = line[p2]
                    adjacentSymbols += right
                    #search right
                if(j < len(schematic) - 1):
                    bottom = schematic[j + 1][begin:end + 1]
                    adjacentSymbols += bottom
                    # search bottom
                if(p1 > 0):
                    left = line[p1 - 1]
                    adjacentSymbols += left
                    #search left

                if(any(c in SYMBOLS for c in adjacentSymbols)):
                    partNumbers.append(int(num))

            p1 = p2 + 1

        j += 1

print(f"Sum of part numbers: {sum(partNumbers)}")
                