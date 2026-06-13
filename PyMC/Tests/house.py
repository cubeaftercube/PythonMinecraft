from functions import *

# Initialize the class
HOST = "localhost"
PORT = 25575
PASSWD = "12345"
mc = MinecraftCommands(HOST, PORT, PASSWD)

print("Starting construction of the big house...")

# --- Base Coordinates ---
# Building at Y=64 is perfect as it aligns with standard sea-level terrain in the Overworld.
x1, y1, z1 = 100, 64, 100
x2, y2, z2 = 130, 70, 130

# --- Materials ---
wall_block = "minecraft:stone_bricks"
floor_block = "minecraft:polished_andesite"
roof_block = "minecraft:dark_oak_slab"
window_block = "minecraft:glass"
corner_block = "minecraft:deepslate"

# 1. Floor
print(mc.fill(x1, y1 - 1, z1, x2, y1 - 1, z2, floor_block))

# 2. Main Walls (Outer shell)
# Front and Back walls
mc.fill(x1, y1, z1, x2, y2, z1, wall_block)
mc.fill(x1, y1, z2, x2, y2, z2, wall_block)
# Left and Right walls
mc.fill(x1, y1, z1, x1, y2, z2, wall_block)
mc.fill(x2, y1, z1, x2, y2, z2, wall_block)

# 3. Hollow out the inside (leaving 1 block thick walls)
mc.fill(x1 + 1, y1, z1 + 1, x2 - 1, y2, z2 - 1, "minecraft:air")

# 4. Corner pillars for better aesthetics
mc.fill(x1, y1, z1, x1, y2, z1, corner_block)
mc.fill(x2, y1, z1, x2, y2, z1, corner_block)
mc.fill(x1, y1, z2, x1, y2, z2, corner_block)
mc.fill(x2, y1, z2, x2, y2, z2, corner_block)

# 5. Windows
# Front wall windows
mc.fill(x1 + 4, y1 + 2, z1, x1 + 8, y1 + 3, z1, window_block)
mc.fill(x1 + 12, y1 + 2, z1, x1 + 16, y1 + 3, z1, window_block)
# Back wall windows
mc.fill(x1 + 4, y1 + 2, z2, x1 + 8, y1 + 3, z2, window_block)
mc.fill(x1 + 12, y1 + 2, z2, x1 + 16, y1 + 3, z2, window_block)
# Left wall windows
mc.fill(x1, y1 + 2, z1 + 4, x1, y1 + 3, z1 + 8, window_block)
mc.fill(x1, y1 + 2, z1 + 12, x1, y1 + 3, z1 + 16, window_block)
# Right wall windows
mc.fill(x2, y1 + 2, z1 + 4, x2, y1 + 3, z1 + 8, window_block)
mc.fill(x2, y1 + 2, z1 + 12, x2, y1 + 3, z1 + 16, window_block)

# 6. Doorway
door_x = x1 + 15
# Carve out the space for the door
mc.fill(door_x, y1, z1, door_x, y1 + 1, z1, "minecraft:air")
# Place the door (using execute to handle block states properly)
mc._execute(f"setblock {door_x} {y1} {z1} minecraft:oak_door[facing=south,half=lower]")
mc._execute(f"setblock {door_x} {y1 + 1} {z1} minecraft:oak_door[facing=south,half=upper]")

# 7. Flat Overhanging Roof
mc.fill(x1 - 1, y2 + 1, z1 - 1, x2 + 1, y2 + 1, z2 + 1, roof_block)

# 8. Chimney
mc.fill(x2 - 3, y2 + 1, z2 - 3, x2 - 1, y2 + 5, z2 - 1, "minecraft:bricks")
mc.fill(x2 - 2, y2 + 1, z2 - 2, x2 - 2, y2 + 5, z2 - 2, "minecraft:air")
mc.setblock(x2 - 2, y2 + 5, z2 - 2, "minecraft:campfire") # Creates a nice smoke effect

# 9. Interior Details & Furniture
# Ceiling Lights
mc.setblock(x1 + 5, y2, z1 + 5, "minecraft:glowstone")
mc.setblock(x1 + 15, y2, z1 + 15, "minecraft:glowstone")
mc.setblock(x1 + 5, y2, z1 + 15, "minecraft:glowstone")
mc.setblock(x1 + 15, y2, z1 + 5, "minecraft:glowstone")

# Functional Blocks
print(mc._execute(f"setblock {x1 + 2} {y1} {z1 + 2} minecraft:crafting_table"))
mc._execute(f"setblock {x1 + 3} {y1} {z1 + 2} minecraft:furnace[facing=south]")
mc._execute(f"setblock {x1 + 4} {y1} {z1 + 2} minecraft:smoker[facing=south]")
mc._execute(f"setblock {x1 + 2} {y1} {z1 + 25} minecraft:chest[facing=north]")
mc._execute(f"setblock {x1 + 4} {y1} {z1 + 25} minecraft:barrel[facing=north]")

# 10. Entrance Path
mc.fill(door_x - 1, y1 - 1, z1 - 5, door_x + 1, y1 - 1, z1 - 1, "minecraft:gravel")

print("Big house built successfully!")