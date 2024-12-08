def read_file(filename: str):
    f = open(filename, 'r')
    i = 0
    antenna_locations = {}
    for line in f.readlines():
        line = list(line.strip())
        m = len(line)
        for j in range(m):
            loc = line[j]
            if loc != '.':
                if loc not in antenna_locations:
                    antenna_locations[loc] = []
                antenna_locations[loc].append((i, j))
        i += 1
    return i, m, antenna_locations


def create_antinode(loc1, loc2, n, m):
    """
    Calculate the antinodes for two antenna locations.
    """
    d_row = loc2[0] - loc1[0]
    d_col = loc2[1] - loc1[1]
    
    # Calculate antinodes
    antinode1 = (loc1[0] - d_row, loc1[1] - d_col)  # loc1 - d
    antinode2 = (loc2[0] + d_row, loc2[1] + d_col)  # loc2 + d
    
    valid_antinodes = []
    
    # Check if antinode1 is within bounds
    if 0 <= antinode1[0] < n and 0 <= antinode1[1] < m:
        valid_antinodes.append(antinode1)
    
    # Check if antinode2 is within bounds
    if 0 <= antinode2[0] < n and 0 <= antinode2[1] < m:
        valid_antinodes.append(antinode2)
    
    return valid_antinodes


            
def count_unique_antinodes(filename):
    # get antenna locations
    n, m, antenna_locations = read_file(filename)

    unique_antinodes = set()
    
    # Iterate over each frequency
    for freq, locations in antenna_locations.items():
        # Generate all pairs of antennas for the current frequency
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                loc1, loc2 = locations[i], locations[j]
                antinodes = create_antinode(loc1, loc2, n, m)
                
                unique_antinodes.update(antinodes)
    return len(unique_antinodes)


if __name__ == "__main__":
    filename = "input"
    result = count_unique_antinodes(filename)
    print(f"Number of unique antinode locations: {result}")


    