from collections import namedtuple

RangeItem = namedtuple("RangeItem", "start itemRange")

# TODO split

# split
#   for each input
#       for each map
#           if input is in map
#               add to output new start and range and the leftover of the input

# Squash - Done!
# sort output
#   for each output
#       if output in prev output
#           add to prev output

def MapSource(source, map):
    for line in map:
        destination_range_start,source_range_start, range_length = line.split()
        max = int(source_range_start) + (int(range_length) - 1) # Range incudes starting number so  -1
        if source >= int(source_range_start) and source < int(max):
            diff = source - int(source_range_start)
            return (int(destination_range_start) + diff)
    # If no mapping return original source
    return(source)

def readMap(input):
    # Skipping over blank lines to get to the start of the Map
    for line in input:
        if line.strip():
            break

    map = []
    for line in input:
        if line.strip():
            map.append(line.strip())
        else:
            break
    return map

def Split():
    output = []
    return output

def Squash(output):
    i = 0
    while i < len(output):
        prev = output[i -1]
        current = output[i]
        if(prev.start + (prev.itemRange - 1) >= current.start):
            newRange = current.start + current.itemRange - prev.start
            output[i - 1] = RangeItem(prev.start,newRange)
            output.pop(i)
        else:
            i +=1

    return output


def Main():
    with open("data.txt") as input:
        _,inputSeeds = input.readline().split(":")
        inputSeeds = inputSeeds.split()
        items = []
        i = 0
        while i < len(inputSeeds) - 1:
            start = int(inputSeeds[i])
            itemRange = int(inputSeeds[i + 1])
            items.append(RangeItem(start,itemRange))
            i +=1
        
        items = sorted(items, key=lambda x: x.itemRange)
        print(items)
        
        # Seeds to soil
        seedMap = readMap(input)
        output = MapSource(items,seedMap)
        soils = Squash(output)
        # Soil to fertilizer 
        output = readMap(output,input)
        # Fertilizer to water
        water = readMap(output,input)
        # Water to light
        light = readMap(water,input)
        # Light to temperature
        temperature = readMap(light,input)
        # Temperature to humidity
        humidity = readMap(temperature,input)
        # Humidity to location
        location = readMap(humidity,input)
        print(f"Min location: {min(location)}")


if __name__ == "__main__":
    Main()
    