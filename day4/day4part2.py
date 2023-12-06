f = open('day4/day4.txt', 'r')
lines = f.read().splitlines()

def getWinningAmount(line):
  _, information = line.split(":")
  winningNumbers, numbers = information.split("|")
  winningNumbers = set(filter(lambda s: s != '', winningNumbers.split(" ")))
  numbers = list(filter(lambda s: s != '', numbers.split(" ")))

  value = 0
  for num in numbers:
    if num in winningNumbers:
        value += 1


  return value

instances = [1 for _ in range(len(lines))]

for j in range(len(lines)):
  for k in range(getWinningAmount(lines[j])):
    instances[j + k + 1] = instances[j + k + 1] + instances[j]

print(sum(instances))
