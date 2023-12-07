f = open('day5/day5.txt', 'r')
lines = f.read().splitlines()

# get seeds
seeds = [int(x) for x in lines[0].split(": ")[1].split(" ")]

# get maps
maps = [[] for _ in range(7)] # seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation

currMap = 0
lineIndex = 2
while lineIndex < len(lines):
  if lines[lineIndex] == "":
    currMap += 1
    lineIndex += 1
    continue

  if "map" in lines[lineIndex]:
    lineIndex += 1
    continue
  
  mapDest, mapSource, mapRange = lines[lineIndex].split(" ")
  maps[currMap].append({"mapDest": int(mapDest), "mapSource": int(mapSource),  "mapRange": int(mapRange)})
  lineIndex += 1

# map seeds to locations
for i in range(len(seeds)):
  for currMap in maps:
    for mapping in currMap:
      if mapping["mapSource"] <= seeds[i] and seeds[i] < mapping["mapSource"] + mapping["mapRange"]:
        seeds[i] = mapping["mapDest"] + seeds[i] - mapping["mapSource"] 
        break

print(min(seeds))
