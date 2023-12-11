import collections

def determineHandValue(hand):
  types = {'fiveOfAKind': 'z',
           'fourOfAKind': 'y',
           'fullHouse': 'x',
           'threeOfAKind': 'w',
           'twoPair': 'v',
           'onePair': 'u',
           'highCard': 't'
           }

  cardCounter = collections.Counter(hand)
  if 'J' in cardCounter.keys():
    jCount = cardCounter['J']
  else:
    jCount = 0

  if 'J' in cardCounter.keys():
    cardCounter.pop('J')
  cardCount = list(cardCounter.values())

  if jCount == 5:
    return types['fiveOfAKind']

  for count in cardCount:
    if count + jCount == 5:
      return types['fiveOfAKind']

  for count in cardCount:
    if count + jCount == 4:
      return types['fourOfAKind']

  if cardCount.count(2) == 2:
    if jCount:
      return types['fullHouse']
    return types['twoPair']

  if 3 in cardCount and 2 in cardCount:
    return types['fullHouse']
  
  for count in cardCount:
    if count + jCount == 3:
      return types['threeOfAKind']
  
  for count in cardCount:
    if count + jCount == 2:
      return types['onePair']
  
  return types['highCard']


def determineSecondaryValue(card):
  faceConversions = {'A': 'z',
                     'K': 'y',
                     'Q': 'x',
                     'J': 'w', 
                     'T': 'v',
                     'J': '0'}

  if card in faceConversions.keys():
    return faceConversions[card]
  return card


def applyValues(hand):
  res = determineHandValue(hand)
  for card in hand:
    res += determineSecondaryValue(card)
  return res


f = open('day7/day7.txt', 'r')
lines = f.read().splitlines()

hands = []
for line in lines:
  hand, value = line.split(' ')
  hands.append((hand, int(value)))

hands.sort(key = lambda tuple: applyValues(tuple[0]))

totalWinnings = 0
for i in range(len(hands)):
  rank = i + 1
  totalWinnings += rank * hands[i][1]

print(totalWinnings)
