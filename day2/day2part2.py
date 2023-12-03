import re

def getMinimumGame(line):
  maxCount = {"red": 0, "green": 0, "blue": 0} 

  _, information = line.strip().split(": ")
  reveals = re.split("; |, ", information) # we assume two colors aren't listed in the same subset

  for reveal in reveals:
    count, colorName = reveal.split(" ")
    if int(count) > maxCount[colorName]:
      maxCount[colorName] = int(count)
  
  power = 1
  for val in maxCount.values():
    power *= val

  return power

f = open('day2/day2.txt', 'r')
lines = f.readlines()

sum = 0
for line in lines:
  sum += getMinimumGame(line)

print(sum)
