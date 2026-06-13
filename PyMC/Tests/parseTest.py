from functions import *
from parse_func import parse_minecraft_data

HOST = "localhost"
PORT = 25575
PASSWD = "12345"
mc = MinecraftCommands(HOST, PORT, PASSWD)

data = mc.data("get entity @r")
parsed_data = parse_minecraft_data(data)

for name, value in parsed_data.items():
    print(f"{name}: {value}")