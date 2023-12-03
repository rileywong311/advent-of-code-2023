nums = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

f = open('day3/day3.txt', 'r')
lines = f.read().splitlines()

def getEntireNumber(row, col):
  lo = hi = col
  while lo > 0 and lines[row][lo - 1] != "." and lines[row][lo - 1] != "*":
    lo -= 1
  while hi < len(lines[row]) and lines[row][hi] != "." and lines[row][hi] != "*":
    hi += 1

  return int(lines[row][lo:hi])

def getGearRatio(row, col):
  adjacentNumbers = []

  aboveMiddleExists = False
  if row > 0:
    above = row - 1
    if lines[above][col] in nums:
      adjacentNumbers.append((above, col))
      aboveMiddleExists = True

  belowMiddleExists = False
  if row < len(lines) - 1:
    below = row + 1
    if lines[below][col] in nums:
      adjacentNumbers.append((below, col))
      belowMiddleExists = True

  if col > 0:
    left = col - 1
    if lines[row][left] in nums:
      adjacentNumbers.append((row, left))

    if row > 0 and not aboveMiddleExists:
      above = row - 1
      if lines[above][left] in nums:
        adjacentNumbers.append((above, left))
    
    if row < len(lines) - 1 and not belowMiddleExists:
      below = row + 1
      if lines[below][left] in nums:
        adjacentNumbers.append((below, left))

  if col < len(lines[row]) - 1:
    right = col + 1
    if lines[row][right] in nums:
      adjacentNumbers.append((row, right))

    if row > 0 and not aboveMiddleExists:
      above = row - 1
      if lines[above][right] in nums:
        adjacentNumbers.append((above, right))
    
    if row < len(lines) - 1 and not belowMiddleExists:
      below = row + 1
      if lines[below][right] in nums:
        adjacentNumbers.append((below, right))

  if len(adjacentNumbers) == 2:
    return getEntireNumber(adjacentNumbers[0][0], adjacentNumbers[0][1]) * getEntireNumber(adjacentNumbers[1][0], adjacentNumbers[1][1])
  return None  
  
gearRatiosFound = []
for row in range(len(lines)):
  for col in range(len(lines[row])):
    char = lines[row][col]
    if char == "*":
      gearRatio = getGearRatio(row, col)
      if gearRatio:
        gearRatiosFound.append(gearRatio)

print(sum(gearRatiosFound))
