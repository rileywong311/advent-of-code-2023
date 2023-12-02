import re

maxCount = {"red": 12, "green": 13, "blue": 14} 

def isValidGame(line):
  game, information = line.strip().split(": ")
  reveals = re.split("; |, ", information) # we assume two colors aren't listed in the same subset

  for reveal in reveals:
    count, colorName = reveal.split(" ")
    if int(count) > maxCount[colorName]:
      return 0
  
  gameID = int(game[5:])
  return gameID

f = open('day2/day2.txt', 'r')
lines = f.readlines()

sum = 0
for line in lines:
  sum += isValidGame(line)

print(sum)
