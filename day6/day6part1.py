import re

f = open('day6/day6.txt', 'r')
lines = f.read().splitlines()

times = [int(x) for x in filter(lambda s: s!= '', re.split("\s+", lines[0].split(":")[1]))]
records = [int(x) for x in filter(lambda s: s!= '', re.split("\s+", lines[1].split(":")[1]))]

def countWinnings(time, record):
  hold = 0
  while (time - hold) * hold <= record:
    hold += 1
  return time - (2 * hold) + 1

ways = 1
for i in range(len(times)):
  ways *= countWinnings(times[i], records[i])

print(ways)
