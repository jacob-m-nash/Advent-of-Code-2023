powersSum = 0
with open("data.txt") as input:
    for line in input:
        line = line.rstrip()
        game,pulls = line.split(":")
        minRedCubes = 0
        minGreenCubes = 0
        minBlueCubes = 0
        for pull in pulls.split(";"):
            for cube in pull.split(","):
                cubeCount,cubeColour = cube.split()
                if(cubeColour == "red"):
                     if(int(cubeCount) > minRedCubes):
                        minRedCubes = int(cubeCount)
                if(cubeColour == "green"):
                     if(int(cubeCount) > minGreenCubes):
                        minGreenCubes = int(cubeCount)
                if(cubeColour == "blue"):
                     if(int(cubeCount) > minBlueCubes):
                        minBlueCubes = int(cubeCount)

        powersSum += minRedCubes * minGreenCubes * minBlueCubes

print(f"Sun of powers: {powersSum}")