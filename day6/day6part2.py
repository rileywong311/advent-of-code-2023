import re

f = open('day6/day6.txt', 'r')
lines = f.read().splitlines()

time = int(lines[0].split(":")[1].replace(" ", ""))
record = int(lines[1].split(":")[1].replace(" ", ""))

def countWinnings(time, record):
  hold = 0
  while (time - hold) * hold <= record:
    hold += 1
  return time - (2 * hold) + 1

ways = countWinnings(time, record)
print(ways)
