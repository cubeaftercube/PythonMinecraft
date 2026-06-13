from rcon.source import Client

class MinecraftCommands:
    def __init__(self, host: str, port: int, passwd: str):
        self.host = host
        self.port = port
        self.passwd = passwd

    def _execute(self, command: str) -> str:
        """Connects to the server, executes the command, and closes the connection."""
        with Client(self.host, self.port, passwd=self.passwd) as client:
            return client.run(command)

    def raw(self, command: str) -> str:
        """Fallback to execute any arbitrary Minecraft command string."""
        return self._execute(command)

    # ==========================================
    # --- Core World & Block Manipulation ---
    # ==========================================
    def setblock(self, x: int, y: int, z: int, block_name: str) -> str:
        return self._execute(f"setblock {int(x)} {int(y)} {int(z)} {block_name}")

    def fill(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int, block_name: str) -> str:
        return self._execute(f"fill {int(x1)} {int(y1)} {int(z1)} {int(x2)} {int(y2)} {int(z2)} {block_name}")

    def clone(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int, x: int, y: int, z: int, mode: str = "") -> str:
        return self._execute(f"clone {int(x1)} {int(y1)} {int(z1)} {int(x2)} {int(y2)} {int(z2)} {int(x)} {int(y)} {int(z)} {mode}")

    def setworldspawn(self, x: int, y: int, z: int) -> str:
        return self._execute(f"setworldspawn {int(x)} {int(y)} {int(z)}")

    def spawnpoint(self, target: str, x: int, y: int, z: int) -> str:
        return self._execute(f"spawnpoint {target} {int(x)} {int(y)} {int(z)}")

    def weather(self, weather_type: str, duration: int = 0) -> str:
        return self._execute(f"weather {weather_type} {duration}") if duration > 0 else self._execute(f"weather {weather_type}")

    def time(self, action: str, value: str = "") -> str:
        return self._execute(f"time {action} {value}")

    def gamerule(self, rule: str, value: str = "") -> str:
        return self._execute(f"gamerule {rule} {value}") if value else self._execute(f"gamerule {rule}")

    def difficulty(self, level: str) -> str:
        return self._execute(f"difficulty {level}")

    def fillbiome(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int, biome: str) -> str:
        return self._execute(f"fillbiome {int(x1)} {int(y1)} {int(z1)} {int(x2)} {int(y2)} {int(z2)} {biome}")

    # ==========================================
    # --- Player, Entity & Item Management ---
    # ==========================================
    def say(self, message: str) -> str:
        return self._execute(f"say {message}")

    def tell(self, target: str, message: str) -> str:
        return self._execute(f"tell {target} {message}")

    def tp(self, target: str, destination: str) -> str:
        return self._execute(f"tp {target} {destination}")

    def kill(self, target: str = "@e") -> str:
        return self._execute(f"kill {target}")

    def gamemode(self, mode: str, target: str = "@s") -> str:
        return self._execute(f"gamemode {mode} {target}")

    def give(self, target: str, item: str, amount: int = 1) -> str:
        return self._execute(f"give {target} {item} {amount}")

    def clear(self, target: str, item: str = "", amount: int = -1) -> str:
        cmd = f"clear {target}"
        if item:
            cmd += f" {item}"
            if amount >= 0:
                cmd += f" {amount}"
        return self._execute(cmd)

    def effect(self, action: str, target: str, effect_name: str = "", *args) -> str:
        return self._execute(f"effect {action} {target} {effect_name} {' '.join(map(str, args))}")

    def summon(self, entity: str, x: int = 0, y: int = 0, z: int = 0, nbt: str = "") -> str:
        return self._execute(f"summon {entity} {int(x)} {int(y)} {int(z)}")

    # ==========================================
    # --- 26.1 "Tiny Takeover" New Commands ---
    # ==========================================
    def swing(self, target: str = "@s") -> str:
        """Swings the hands of an entity. (Added in 26.1)"""
        return self._execute(f"swing {target}")

    def fetchprofile(self, player: str) -> str:
        """Fetches a player profile. (Added in 26.1)"""
        return self._execute(f"fetchprofile {player}")

    def dialog(self, action: str, *args) -> str:
        """Shows dialog to clients. (Added in 26.1)"""
        return self._execute(f"dialog {action} {' '.join(map(str, args))}")

    def stopwatch(self, action: str, *args) -> str:
        """Creates and modifies real-time stopwatches. (Added in 26.1)"""
        return self._execute(f"stopwatch {action} {' '.join(map(str, args))}")

    def random(self, action: str, *args) -> str:
        """Draw a random value or control the random number sequence. (Added in 26.1)"""
        return self._execute(f"random {action} {' '.join(map(str, args))}")

    def rotate(self, target: str, *args) -> str:
        """Changes the rotation of an entity. (Added in 26.1)"""
        return self._execute(f"rotate {target} {' '.join(map(str, args))}")

    def waypoint(self, action: str, *args) -> str:
        """Manages waypoints displayed on the locator bar. (Added in 26.1)"""
        return self._execute(f"waypoint {action} {' '.join(map(str, args))}")

    def tick(self, action: str, *args) -> str:
        """Controls the tick rate of the game."""
        return self._execute(f"tick {action} {' '.join(map(str, args))}")

    # ==========================================
    # --- Remaining Commands (Generic) ---
    # ==========================================
    def advancement(self, *args): return self._execute(f"advancement {' '.join(map(str, args))}")
    def attribute(self, *args): return self._execute(f"attribute {' '.join(map(str, args))}")
    def ban(self, *args): return self._execute(f"ban {' '.join(map(str, args))}")
    def ban_ip(self, *args): return self._execute(f"ban-ip {' '.join(map(str, args))}")
    def banlist(self, *args): return self._execute(f"banlist {' '.join(map(str, args))}")
    def bossbar(self, *args): return self._execute(f"bossbar {' '.join(map(str, args))}")
    def damage(self, *args): return self._execute(f"damage {' '.join(map(str, args))}")
    def data(self, *args): return self._execute(f"data {' '.join(map(str, args))}")
    def datapack(self, *args): return self._execute(f"datapack {' '.join(map(str, args))}")
    def debug(self, *args): return self._execute(f"debug {' '.join(map(str, args))}")
    def defaultgamemode(self, *args): return self._execute(f"defaultgamemode {' '.join(map(str, args))}")
    def deop(self, *args): return self._execute(f"deop {' '.join(map(str, args))}")
    def enchant(self, *args): return self._execute(f"enchant {' '.join(map(str, args))}")
    def execute(self, *args): return self._execute(f"execute {' '.join(map(str, args))}")
    def experience(self, *args): return self._execute(f"experience {' '.join(map(str, args))}")
    def forceload(self, *args): return self._execute(f"forceload {' '.join(map(str, args))}")
    def function(self, *args): return self._execute(f"function {' '.join(map(str, args))}")
    def help(self, *args): return self._execute(f"help {' '.join(map(str, args))}")
    def item(self, *args): return self._execute(f"item {' '.join(map(str, args))}")
    def jfr(self, *args): return self._execute(f"jfr {' '.join(map(str, args))}")
    def kick(self, *args): return self._execute(f"kick {' '.join(map(str, args))}")
    def list_players(self): return self._execute("list")
    def locate(self, *args): return self._execute(f"locate {' '.join(map(str, args))}")
    def loot(self, *args): return self._execute(f"loot {' '.join(map(str, args))}")
    def me(self, *args): return self._execute(f"me {' '.join(map(str, args))}")
    def msg(self, *args): return self._execute(f"msg {' '.join(map(str, args))}")
    def op(self, *args): return self._execute(f"op {' '.join(map(str, args))}")
    def pardon(self, *args): return self._execute(f"pardon {' '.join(map(str, args))}")
    def pardon_ip(self, *args): return self._execute(f"pardon-ip {' '.join(map(str, args))}")
    def particle(self, *args): return self._execute(f"particle {' '.join(map(str, args))}")
    def perf(self, *args): return self._execute(f"perf {' '.join(map(str, args))}")
    def place(self, *args): return self._execute(f"place {' '.join(map(str, args))}")
    def playsound(self, *args): return self._execute(f"playsound {' '.join(map(str, args))}")
    def publish(self, *args): return self._execute(f"publish {' '.join(map(str, args))}")
    def recipe(self, *args): return self._execute(f"recipe {' '.join(map(str, args))}")
    def reload(self): return self._execute("reload")
    def return_cmd(self, *args): return self._execute(f"return {' '.join(map(str, args))}") # 'return' is a Python keyword
    def ride(self, *args): return self._execute(f"ride {' '.join(map(str, args))}")
    def save_all(self): return self._execute("save-all")
    def save_off(self): return self._execute("save-off")
    def save_on(self): return self._execute("save-on")
    def schedule(self, *args): return self._execute(f"schedule {' '.join(map(str, args))}")
    def scoreboard(self, *args): return self._execute(f"scoreboard {' '.join(map(str, args))}")
    def seed(self): return self._execute("seed")
    def setidletimeout(self, *args): return self._execute(f"setidletimeout {' '.join(map(str, args))}")
    def spectate(self, *args): return self._execute(f"spectate {' '.join(map(str, args))}")
    def spreadplayers(self, *args): return self._execute(f"spreadplayers {' '.join(map(str, args))}")
    def stop(self): return self._execute("stop")
    def stopsound(self, *args): return self._execute(f"stopsound {' '.join(map(str, args))}")
    def tag(self, *args): return self._execute(f"tag {' '.join(map(str, args))}")
    def team(self, *args): return self._execute(f"team {' '.join(map(str, args))}")
    def teammsg(self, *args): return self._execute(f"teammsg {' '.join(map(str, args))}")
    def teleport(self, *args): return self._execute(f"teleport {' '.join(map(str, args))}")
    def tellraw(self, *args): return self._execute(f"tellraw {' '.join(map(str, args))}")
    def test(self, *args): return self._execute(f"test {' '.join(map(str, args))}")
    def title(self, *args): return self._execute(f"title {' '.join(map(str, args))}")
    def tm(self, *args): return self._execute(f"tm {' '.join(map(str, args))}")
    def transfer(self, *args): return self._execute(f"transfer {' '.join(map(str, args))}")
    def trigger(self, *args): return self._execute(f"trigger {' '.join(map(str, args))}")
    def unpublish(self, *args): return self._execute(f"unpublish {' '.join(map(str, args))}")
    def version(self): return self._execute("version")
    def w(self, *args): return self._execute(f"w {' '.join(map(str, args))}")
    def whitelist(self, *args): return self._execute(f"whitelist {' '.join(map(str, args))}")
    def worldborder(self, *args): return self._execute(f"worldborder {' '.join(map(str, args))}")
    def xp(self, *args): return self._execute(f"xp {' '.join(map(str, args))}")