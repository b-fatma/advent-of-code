from part1 import read_file

def create_antinode(loc1, loc2, n, m):
    d_row = loc2[0] - loc1[0]
    d_col = loc2[1] - loc1[1]
    
    valid_antinodes = []

    # Calculate antinodes upper part
    i = loc1[0] - d_row
    j = loc1[1] - d_col
    
    while 0 <= i < n and 0 <= j < m:
        valid_antinodes.append((i, j))
        i = i - d_row
        j = j - d_col

    i = loc2[0] + d_row
    j = loc2[1] + d_col
    while 0 <= i < n and 0 <= j < m:
        valid_antinodes.append((i, j))
        i = i + d_row
        j = j + d_col        
    
    
    return valid_antinodes
            
def count_unique_antinodes(filename):
    # get antenna locations
    n, m, antenna_locations = read_file(filename)

    unique_antinodes = set()
    
    # Iterate over each frequency
    for freq, locations in antenna_locations.items():
        # Generate all pairs of antennas for the current frequency
        if len(locations) > 1:  # Only include if there are at least two
            unique_antinodes.update(locations)

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


    