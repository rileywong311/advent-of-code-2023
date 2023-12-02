nums = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
startingLetters = {"o", "t", "f", "s", "e", "n"}

def isOne(line, start):
  if start + 2 < len(line) and line[start:start + 3] == "one":
    return "1"
  return None

def isTwoOrThree(line, start):
  if start + 2 < len(line) and line[start:start + 3] == "two":
    return "2"
  if start + 4 < len(line) and line[start:start + 5] == "three":
    return "3"
  return None

def isFourOrFive(line, start):
  if start + 3 < len(line) and line[start:start + 4] == "four":
    return "4"
  if start + 3 < len(line) and line[start:start + 4] == "five":
    return "5"
  return None

def isSixOrSeven(line, start):
  if start + 2 < len(line) and line[start:start + 3] == "six":
    return "6"
  if start + 4 < len(line) and line[start:start + 5] == "seven":
    return "7"
  return None

def isEight(line, start):
  if start + 4 < len(line) and line[start:start+5] == "eight":
    return "8"
  return None

def isNine(line, start):
  if start + 3 < len(line) and line[start:start+4] == "nine":
    return "9"
  return None

getDigitFromLetter = {"o": isOne, "t": isTwoOrThree, "f": isFourOrFive, "s": isSixOrSeven, "e": isEight, "n": isNine}

def getCalibration(line):
  lo = 0
  while lo < len(line):
    if line[lo] in nums:
      firstDigit = line[lo]
      break
    if line[lo] in startingLetters:
      digit = getDigitFromLetter[line[lo]](line, lo)
      if digit:
        firstDigit = digit
        break
    lo += 1
  
  hi = len(line) - 1
  while hi >= 0:
    if line[hi] in nums:
      lastDigit = line[hi]
      break
    if line[hi] in startingLetters:
      digit = getDigitFromLetter[line[hi]](line, hi)
      if digit:
        lastDigit = digit
        break
    hi -= 1

  twoDigitNumber = firstDigit + lastDigit
  return int(twoDigitNumber)

f = open('day1/day1.txt', 'r')
lines = f.readlines()

sum = 0
for line in lines:
  sum += getCalibration(line)

print(sum)
