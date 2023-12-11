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
  
  cardCount = list(collections.Counter(hand).values())

  if 5 in cardCount:
    return types['fiveOfAKind']
  
  if 4 in cardCount:
    return types['fourOfAKind']

  if 3 in cardCount and 2 in cardCount:
    return types['fullHouse']
  
  if 3 in cardCount:
    return types['threeOfAKind']
  
  if cardCount.count(2) == 2:
    return types['twoPair']
  
  if cardCount.count(2) == 1:
    return types['onePair']
  
  return types['highCard']


def determineSecondaryValue(card):
  faceConversions = {'A': 'z',
                     'K': 'y',
                     'Q': 'x',
                     'J': 'w', 
                     'T': 'v'}

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
