# Minecraft 26.1.2 + Python example
from functions import *

# Initialize the class
HOST = "localhost"
PORT = 25575
PASSWD = "12345"
mc = MinecraftCommands(HOST, PORT, PASSWD)

# Use print if you want to get errors back to console
print(mc.say("Hello, 26.1.2 World!"))
print(mc.setblock(100, 64, 200, "diamond_block"))
print(mc.give("@a", "minecraft:netherite_sword", 1))

print(mc.swing("@a")) # Makes all players swing their hands
print(mc.random("value", "1..10")) # Generates a random value between 1 and 10

# Using complex commands like execute using the generic wrappers
print(mc.execute("as", "@a", "at", "@s", "run", "say", "I am here"))
mc._execute(f"setblock 0 70 0 minecraft:chest[facing=north]")