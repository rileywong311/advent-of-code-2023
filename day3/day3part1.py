nums = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

f = open('day3/day3.txt', 'r')
lines = f.read().splitlines()

def isSymbol(char):
  if char not in nums and char != ".":
    return True
  return False

def isNextToSymbol(indicesToCheck, row):
  if indicesToCheck[0] > 0:
    left = indicesToCheck[0] - 1
    if isSymbol(lines[row][left]):
      return True
    indicesToCheck.insert(0, left)

  if indicesToCheck[-1] < len(lines[row]) - 1:
    right = indicesToCheck[-1] + 1
    if isSymbol(lines[row][right]):
      return True
    indicesToCheck.append(right)

  for index in indicesToCheck:
    if row > 0:
      above = lines[row - 1][index]
      if isSymbol(above):
        return True

    if row < len(lines) - 1:
      below = lines[row + 1][index]
      if isSymbol(below):
        return True

  return False

validNumbersFound = []
for row in range(len(lines)):
  currNumber = ""
  currNumberIndices = []
  for col in range(len(lines[row])):
    char = lines[row][col]
    if char in nums:
      currNumber += char
      currNumberIndices.append(col)

    if char not in nums and currNumber:
      if isNextToSymbol(currNumberIndices, row):
        validNumbersFound.append(int(currNumber))
      currNumber = ""
      currNumberIndices = []

  if currNumber:
    if isNextToSymbol(currNumberIndices, row):
      validNumbersFound.append(int(currNumber))

print(sum(validNumbersFound))
