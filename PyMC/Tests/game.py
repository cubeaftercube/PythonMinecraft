from functions import *
import time
import random  # Python's built-in random module to calculate drop offsets

# --- Initialization ---
HOST = "localhost"
PORT = 25575
PASSWD = "12345"
mc = MinecraftCommands(HOST, PORT, PASSWD)


def meteor_shower(rounds=5):
    # 1. Introduction and Setup
    print(mc.say("§a§lWelcome to Meteor Shower!"))
    time.sleep(1)
    print(mc.say("§eYou will receive a Diamond Chestplate."))

    # Give all players a chestplate to make survival slightly easier
    print(mc.give("@a", "minecraft:diamond_chestplate", 1))

    # Force them to wear it using execute
    mc.execute("as", "@a", "at", "@s", "run", "replaceitem", "entity", "@s", "armor.chest",
               "minecraft:diamond_chestplate")

    time.sleep(2)
    print(mc.say("§c§lDodge the falling anvils! Starting in 3..."))
    time.sleep(1)
    print(mc.say("§c2..."))
    time.sleep(1)
    print(mc.say("§c1..."))
    time.sleep(1)

    # 2. The Game Loop
    for current_round in range(1, rounds + 1):
        print(mc.say(f"§b--- Round {current_round} ---"))

        # Drop 5 random anvils near every player
        for _ in range(5):
            # Generate a random X and Z offset (between -4 and 4 blocks relative to the player)
            x_off = random.randint(-4, 4)
            z_off = random.randint(-4, 4)
            y_off = 12  # 12 blocks above the player's head

            # We use local coordinates '^' so the block spawns relative to where the player is looking/standing
            # execute as @a at @s run setblock ^x ^y ^z minecraft:anvil
            command = f"setblock ^{x_off} ^{y_off} ^{z_off} minecraft:anvil"

            mc.execute("as", "@a", "at", "@s", "run", command)

            time.sleep(0.4)  # Slight delay between meteor spawns so they don't all drop at the exact same millisecond

        time.sleep(2.5)  # Wait for the anvils to actually fall and hit the ground before the next round

    # 3. Conclusion
    print(mc.say("§a§lGame Over! Let's check who survived..."))
    print(mc.swing("@a"))  # Victory swing for anyone still alive!


# Execute the game!
print("Starting game loop...")
meteor_shower(rounds=5)