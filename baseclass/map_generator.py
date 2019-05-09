import random
import numpy
import matplotlib.pyplot as plt
from scipy import ndimage
import sentry_sdk
sentry_sdk.init("https://42508ae8bd6040a097bca6b8e500dcd8@sentry.io/1439826")
try:
    from tiles import *
except ImportError:
    from .tiles import *


def create_blank_map(dimensions):
    """Create a wall-only square map"""
    array = []
    for i in range(dimensions):
        array.append([])
        for j in range(dimensions):
            temp = Wall(i, j)
            array[i].append(temp)
    return array


def create_tunnel(created_map, max_tunnel_length, max_tunnels):
    """Create tunnel from the wall-only map"""
    # Pickup a random start point
    current_x = random.choice(range(len(created_map)))
    current_y = random.choice(range(len(created_map)))
    created_map[current_x][current_y] = None

    def random_move(current_direction):
        # Define 4 directions which the tunnel point to next turn
        directions = [
            [-1, 0],  # NORTH  ->  UP
            [1, 0],   # SOUTH  ->  DOWN
            [0, -1],  # WEST   ->  LEFT
            [0, 1],   # EAST   ->  RIGHT
        ]
        while True:
            random_direction = directions[random.choice(range(len(directions)))]
            if len([m for m, n in zip(random_direction, current_direction) if m == n]) != 0:
                continue
            return random_direction

    last_direction = []
    number_of_tunnels = 0
    while number_of_tunnels < max_tunnels:
        # Pickup a direction which not match with last direction or hit map edge
        last_direction = random_move(last_direction)
        current_tunnel_length = 0

        # Create tunnel at a direction at random length
        while current_tunnel_length < random.randrange(max_tunnel_length):
            if (last_direction[0] + current_x) not in range(len(created_map)) \
                    or (last_direction[1] + current_y) not in range(len(created_map)):
                last_direction = random_move(last_direction)
                continue
            current_x, current_y = [x + y for x, y in zip(last_direction, [current_x, current_y])]
            created_map[current_x][current_y] = None
            current_tunnel_length += 1

        # Repeat until we get max tunnel
        number_of_tunnels += 1
    return created_map


def add_map_element(x_axis, y_axis, player_level, weights=None):
    """Generate random map element like Path, Enemy, Treasure."""
    map_elements = [Path(x=x_axis, y=y_axis),
                    EnemyRoom(x=x_axis, y=y_axis, player_level=player_level),
                    TreasureChest(x=x_axis, y=y_axis, player_level=player_level)]
    # Change of an element appear, from left -> right: Path, Enemy, Treasure.
    # This argument can be change defend on player level.
    if weights is None:
        weights = [0.8, 0.15, 0.05]
    return numpy.random.choice(map_elements, p=weights)


def render_map(map_data):
    """Render a digital map into a graphic map."""
    plt.imshow(map_data, clim=(0.064, 0.068))
    mod_img = ndimage.median_filter(map_data, 20)
    plt.imshow(mod_img)
