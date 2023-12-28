from functools import reduce
from operator import mul

def Main():
    with open("data.txt") as input:
        times = input.readline().split()[1:]
        times = [int(time) for time in times]

        distances = input.readline().split()[1:]
        distances = [int(distance) for distance in distances]

        recordPermutations = []
        for i in range(len(times)):
            time = times[i]
            distance = distances[i]
            # We will never get the record if we hold down for 0 or the full time hence 1 and record - 1 
            min = 1
            minFlag = False
            max = time - 1
            maxFlag = False

            while min < max:
                print(f"min: {min}")
                # min
                if not minFlag:
                    remainingTime = time - min
                    if min * remainingTime > distance:
                        minFlag = True
                    else:
                        min += 1 
                print(f"max: {max}")
                if not maxFlag:
                    remainingTime = time - max
                    if max * remainingTime > distance:
                        maxFlag = True
                    else:
                        max -= 1
                if minFlag and maxFlag:
                    break
            
            permutations = max - min + 1
            if permutations > 0:
                recordPermutations.append(permutations)

    print(recordPermutations)
    result = reduce(mul, recordPermutations)
    print(result)


if __name__ == "__main__":
    Main()
