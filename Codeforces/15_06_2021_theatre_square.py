import math

sizes = input().split(" ")

height = int(sizes[0])
width = int(sizes[1])
tile_size = int(sizes[2])

print(math.ceil(height/tile_size) * math.ceil(width/tile_size))
