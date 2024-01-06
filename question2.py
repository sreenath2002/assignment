def calculate_load(platform):
    total_load = 0
    rows = len(platform)
    cols = len(platform[0])

    for row in range(rows):
        for col in range(cols):
            if platform[row][col] == 'O':  # Check for rounded rocks
                total_load += rows - row  # Calculate load based on the distance to the south edge

    return total_load

def tilt_platform(platform):
    tilted_platform = []
    rows = len(platform)
    cols = len(platform[0])

    # Tilt the platform northward (move all rounded rocks towards the top)
    for col in range(cols):
        current_col = ''.join(platform[row][col] for row in range(rows))
        # Reverse the current column to move rocks in the reverse direction (north)
        tilted_platform.append(current_col[::-1])

    return tilted_platform

# Example platform configuration
platform = [
    "O....#....",
    "O.OO#....#",
    ".....##...",
    "OO.#O....O",
    ".O.....O#.",
    "O.#..O.#.#",
    "..O..#O..O",
    ".......O..",
    "#....###..",
    "#OO..#...."
]

# Tilt the platform to move rounded rocks north
tilted_platform = tilt_platform(platform)

# Calculate the total load on the north support beams
total_load = calculate_load(tilted_platform)

print("Total load on the north support beams after tilting the platform:", total_load)

