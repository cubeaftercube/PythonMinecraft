import math
from PyMC.functions import *

# Initialize the class
HOST = "localhost"
PORT = 25575
PASSWD = "12345"
mc = MinecraftCommands(HOST, PORT, PASSWD)


def gear_up_player(player="@a"):
    """Gears up the player with top-tier 26.1.2 equipment."""
    print("Gearing up player...")
    mc.give(player, "minecraft:netherite_helmet", 1)
    mc.give(player, "minecraft:netherite_chestplate", 1)
    mc.give(player, "minecraft:netherite_leggings", 1)
    mc.give(player, "minecraft:netherite_boots", 1)
    mc.give(player, "minecraft:netherite_sword", 1)
    mc.give(player, "minecraft:bow", 1)
    mc.give(player, "minecraft:crossbow", 1)
    mc.give(player, "minecraft:arrow", 64)
    mc.give(player, "minecraft:golden_apple", 16)
    mc.give(player, "minecraft:totem_of_undying", 2)
    print("Gear up complete!")


def build_2d_parabola(start_x, z, length, material="minecraft:glowstone"):
    """Builds a 2D parabola (y = x^2) scaled for Minecraft."""
    print("Building 2D Parabola...")
    for x in range(-length, length):
        # Scale it down so it fits reasonably in the world
        y = int((x ** 2) / 4)
        mc.setblock(start_x + x, 64 + y, z, material)
    print("Parabola built!")


def build_2d_sine_wave(start_x, z, length, material="minecraft:sea_lantern"):
    """Builds a 2D sine wave (y = A * sin(B * x))."""
    print("Building 2D Sine Wave...")
    for x in range(length):
        y = int(5 * math.sin(x / 3.0))
        mc.setblock(start_x + x, 64 + y, z, material)
    print("Sine wave built!")


def build_3d_sphere(center_x, center_y, center_z, radius, material="minecraft:diamond_block"):
    """Builds a hollow 3D sphere using the equation x^2 + y^2 + z^2 = r^2."""
    print("Building 3D Sphere...")
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            for z in range(-radius, radius + 1):
                dist_sq = x ** 2 + y ** 2 + z ** 2
                # Create a shell (hollow sphere) by checking distance bounds
                if radius ** 2 - 2 <= dist_sq <= radius ** 2 + 2:
                    mc.setblock(center_x + x, center_y + y, center_z + z, material)
    print("Sphere built!")


def build_3d_helix(center_x, center_y, center_z, radius, height, material="minecraft:redstone_block"):
    """Builds a 3D helix using parametric equations."""
    print("Building 3D Helix...")
    steps = height * 10
    for i in range(steps):
        t = i / 10.0
        x = int(radius * math.cos(t))
        y = int(t * 2)  # Pitch of the helix
        z = int(radius * math.sin(t))
        mc.setblock(center_x + x, center_y + y, center_z + z, material)
    print("Helix built!")


def build_3d_torus(center_x, center_y, center_z, R, r, material="minecraft:gold_block"):
    """Builds a 3D torus (donut shape) using parametric equations."""
    print("Building 3D Torus...")
    for theta in range(0, 360, 5):
        for phi in range(0, 360, 5):
            theta_rad = math.radians(theta)
            phi_rad = math.radians(phi)

            x = int((R + r * math.cos(phi_rad)) * math.cos(theta_rad))
            y = int(r * math.sin(phi_rad))
            z = int((R + r * math.cos(phi_rad)) * math.sin(theta_rad))

            mc.setblock(center_x + x, center_y + y, center_z + z, material)
    print("Torus built!")


def teleport_to_random_coords(min_val=-1000, max_val=1000):
    """Teleports the player to random coordinates using the new random command."""
    print("Teleporting to random location...")
    # Use the new 26.1 /random command to get values
    try:
        rand_x = int(mc.random("value", f"{min_val}..{max_val}"))
        rand_z = int(mc.random("value", f"{min_val}..{max_val}"))
    except ValueError:
        # Fallback if the wrapper captures raw output differently
        rand_x, rand_z = 0, 0

    # Using execute wrapper to safely teleport the nearest player
    mc.execute("as", "@p", "run", "teleport", str(rand_x), "100", str(rand_z))
    print(f"Teleported to X: {rand_x}, Y: 100, Z: {rand_z}")


def summon_mob_army(mob="minecraft:zombie", count=10, x=100, y=64, z=100):
    """Summons an army of mobs in a perfect circle."""
    print("Summoning mob army...")
    for i in range(count):
        angle = 2 * math.pi * i / count
        offset_x = int(5 * math.cos(angle))
        offset_z = int(5 * math.sin(angle))
        mc.summon(mob, x + offset_x, y, z + offset_z)
    print("Army summoned!")


def light_up_area(x1, z1, x2, z2, spacing=5):
    """Places torches in a grid and grants night vision using execute."""
    print("Lighting up area...")
    # Use the generic execute wrapper to run a complex effect command
    mc.execute("as", "@a", "run", "effect", "give", "@s", "minecraft:night_vision", "9999", "1", "false")

    for x in range(x1, x2, spacing):
        for z in range(z1, z2, spacing):
            mc.setblock(x, 63, z, "minecraft:torch")
    print("Area lit up!")


def create_waypoints():
    """Creates a network of waypoints using the new 26.1 Tiny Takeover features."""
    print("Creating waypoints...")
    mc.waypoint("add", "Spawn_Base", "0", "64", "0")
    mc.waypoint("add", "Diamond_Mine", "500", "11", "-500")
    mc.waypoint("add", "Nether_Portal", "100", "64", "100")
    mc.waypoint("add", "Math_Sphere", "200", "100", "200")
    print("Waypoints created!")


def apply_global_effects():
    """Gives all players cool status effects using execute."""
    print("Applying global effects...")
    mc.execute("as", "@a", "run", "effect", "give", "@s", "minecraft:speed", "9999", "2", "false")
    mc.execute("as", "@a", "run", "effect", "give", "@s", "minecraft:jump_boost", "9999", "2", "false")
    mc.execute("as", "@a", "run", "effect", "give", "@s", "minecraft:health_boost", "9999", "4", "false")
    print("Effects applied!")


def build_3d_pyramid(base_x, base_y, base_z, size, material="minecraft:sandstone"):
    """Builds a 3D stepped pyramid."""
    print("Building 3D Pyramid...")
    for i in range(size):
        current_size = size - i
        for x in range(-current_size, current_size + 1):
            for z in range(-current_size, current_size + 1):
                mc.setblock(base_x + x, base_y + i, base_z + z, material)
    print("Pyramid built!")


def clear_weather_and_time():
    """Sets the world to a sunny morning using generic wrappers."""
    print("Setting weather and time...")
    mc.execute("run", "weather", "clear")
    mc.execute("run", "time", "set", "day")
    mc.say("Let there be light!")
    print("Weather and time set!")


def run_all_demos():
    """Runs all the mathematical and utility functions."""
    gear_up_player()
    apply_global_effects()
    create_waypoints()

    # Math PyMC (Spaced out along the X axis)
    build_2d_parabola(100, 200, 20)
    build_2d_sine_wave(150, 200, 60)
    build_3d_sphere(250, 100, 250, 10)
    build_3d_helix(300, 64, 300, 5, 30)
    build_3d_torus(350, 80, 350, 10, 3)
    build_3d_pyramid(400, 64, 400, 10)

    # Utility PyMC
    summon_mob_army(count=12, x=500, y=64, z=500)
    light_up_area(500, 500, 550, 550)
    clear_weather_and_time()
    teleport_to_random_coords()


if __name__ == "__main__":
    pass