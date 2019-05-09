from baseclass.player import Fighter, Archer, Assassin
from baseclass.tiles import SpawnPoint, Wall, Path, TreasureChest, EnemyRoom
from baseclass import map_generator
import sentry_sdk
import random
sentry_sdk.init("https://42508ae8bd6040a097bca6b8e500dcd8@sentry.io/1439826")

directions = {
    'N': [-1,  0],  # NORTH   ->   UP
    'S': [ 1,  0],  # SOUTH   ->   DOWN
    'W': [ 0, -1],  # WEST    ->   LEFT
    'E': [ 0,  1],  # EAST    ->   RIGHT
}

if __name__ == '__main__':
    # Generate a new world for player.
    wall_only_map = map_generator.create_blank_map(dimensions=25)
    final_map = map_generator.create_tunnel(wall_only_map, max_tunnels=500, max_tunnel_length=5)

    # Set entrance for the map.
    while True:
        coordinate_x = random.randrange(25)
        coordinate_y = random.randrange(25)
        if final_map[coordinate_x][coordinate_y]:
            final_map[coordinate_x][coordinate_y] = SpawnPoint(coordinate_x, coordinate_y)
            player1 = Fighter(name='A', position=[coordinate_x, coordinate_y])
            break

    # Main loop:
    while True:
        # Begin to ask players about their next directions.
        player1_direction = input('Please choose a direction (N/E/W/S): ')

        # If player input wrong character, do loop again.
        if player1_direction not in directions:
            print("You enter a wrong character! Please choose N/E/W/S only!")
            continue

        # If next tile out of map, inform player about that and do loop again.
        next_x, next_y = [sum(element) for element in zip(player1.position, directions[player1_direction])]
        if not final_map[next_x][next_y]:
            print("Out of map! Please choose or directions!")
            continue

        # If next tile is a wall, inform player and do loop again.
        if final_map[next_x][next_y] == Wall:
            print("Stone wall ahead, can't go that way. Please choose another direction!")
            continue

        player1.position = [next_x, next_y]  # If nothing wrong happen then move player to next tile.

        # Now generate properties for the tile player is in.
        if not isinstance(final_map[next_x][next_y], (Path, TreasureChest, EnemyRoom)):
            final_map[next_x][next_y] = map_generator.add_map_element(next_x, next_y)
        print(final_map[next_x][next_y]) if isinstance(final_map[next_x][next_y], object) else print("None")
