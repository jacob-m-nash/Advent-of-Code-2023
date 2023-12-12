scores = []

with open("data.txt") as input:
    for line in input:
        score = 0
        game, numbers = line.split(":")
        winningNumbers, myNumbers = numbers.split("|")
        winningNumbers = winningNumbers.split()
        myNumbers = myNumbers.split()
        for number in winningNumbers:
            if number in myNumbers:
                if(score == 0):
                    score = 1
                else:
                    score *= 2
                
        scores.append(score)

print(f"Sum of scores: {sum(scores)}")
