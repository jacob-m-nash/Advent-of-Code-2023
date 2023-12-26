def MapSource(source, map):
    for line in map:
        destination_range_start,source_range_start, range_length = line.split()
        max = int(source_range_start) + (int(range_length) - 1) # Range incudes starting number so  -1
        if source >= int(source_range_start) and source < int(max):
            diff = source - int(source_range_start)
            return (int(destination_range_start) + diff)
    # If no mapping return original source
    return(source)

def readMap(sources, input):
    # Skipping over blank lines to get to the start of the Map
    for line in input:
        if line.strip():
            break

    map = []
    output = []
    for line in input:
        if line.strip():
            map.append(line.strip())
        else:
            break
    for source in sources:
        output.append(MapSource(source,map))

    return output

def Main():
    with open("data.txt") as input:
        _,seeds = input.readline().split(":")
        seeds = seeds.split()
        seeds = [int(item) for item in seeds]

        # Seeds to soil
        soil = readMap(seeds,input)
        # Soil to fertilizer 
        fertilizer = readMap(soil,input)
        # Fertilizer to water
        water = readMap(fertilizer,input)
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
    