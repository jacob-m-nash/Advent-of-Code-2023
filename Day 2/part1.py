validGames = []
MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14

def GameValidator(pulls):
    for pull in pulls.split(";"):
            for cube in pull.split(","):
                cubeCount,cubeColour = cube.split()
                if(cubeColour == "red"):
                     if(int(cubeCount) > MAX_RED_CUBES):
                          return False
                if(cubeColour == "green"):
                     if(int(cubeCount) > MAX_GREEN_CUBES):
                          return False
                if(cubeColour == "blue"):
                     if(int(cubeCount) > MAX_BLUE_CUBES):
                          return False
    return True
                 

with open("data.txt") as input:
    for line in input:
        line = line.rstrip()
        game,pulls = line.split(":")
        gameNumber = int(game.split()[1])
        if(GameValidator(pulls) == True):
             validGames.append(gameNumber)
        
print(f"Sum of valid games: {sum(validGames)}")