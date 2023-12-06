f = open('day4/day4.txt', 'r')
lines = f.read().splitlines()

def getCardValue(line):
  _, information = line.split(":")
  winningNumbers, numbers = information.split("|")
  winningNumbers = set(filter(lambda s: s != '', winningNumbers.split(" ")))
  numbers = list(filter(lambda s: s != '', numbers.split(" ")))

  value = 0
  for num in numbers:
    if num in winningNumbers:
      if not value:
        value = 1
      else:
        value *= 2

  return value

totalPoints = 0
for line in lines:
  totalPoints += getCardValue(line)

print(totalPoints)
