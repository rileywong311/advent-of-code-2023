nums = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}

def getCalibration(line):
  lo = 0
  while line[lo] not in nums and lo < len(line):
    lo += 1
  firstDigit = line[lo]

  hi = len(line) - 1
  while line[hi] not in nums and hi >= 0:
    hi -= 1
  lastDigit = line[hi]

  twoDigitNumber = firstDigit + lastDigit
  return int(twoDigitNumber)

f = open('day1/day1.txt', 'r')
lines = f.readlines()

sum = 0
for line in lines:
  sum += getCalibration(line)

print(sum)
