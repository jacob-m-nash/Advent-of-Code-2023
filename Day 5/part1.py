def calcMapping(line,sources):
    
    destination_range_start,source_range_start, range_length = line.split()
    max = source_range_start + range_length
    for source in sources:
        if source >= int(source_range_start) and source < int(max):
            diff = source - int(source_range_start)
            return (int(destination_range_start) + diff)



with open("data.txt") as input:
    _,seeds = input.readline().split(":")
    seeds = seeds.split()
    seeds = [int(item) for item in seeds]
    print(seeds)


    for line in input:
        if line.strip():
            break
    # TODO: auto go through maps
    # seed-to-soil map
    soils = []
    i = 0
    for line in input:
        if line.strip():
            soils.append(calcMapping(line,seeds))
        else:
            break
    print(soils)



