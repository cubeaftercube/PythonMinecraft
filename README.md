# PythonMinecraft

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Minecraft](https://img.shields.io/badge/Minecraft-Any%20version-brightgreen.svg)](https://www.minecraft.net/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **Python + Minecraft Connector** that allows you to execute Python code directly on a Minecraft server.

---

## Installation

Youtube Tutorial: [Not uploaded yet](https://www.youtube.com)
Or you can continue here:

1. Download [minecraft server](https://www.minecraft.net/en-us/article/minecraft-java-edition-26-1-2) (click cross-platform server jar)
    *or google for your desired version*
2. Install dependencies
    `pip install -r requirements.txt`
3. Start server and accept eula
4. Change the **server/server.properties** file:
- enable-rcon=true
- rcon.port=25575
- rcon.password=your_secure_password
5. Code!

### Notes:

> `rcon.port` can be any you want, just make sure its opened

> if you agree to Minecraft® eula you can do `eula=true` in eula.txt

---

# You can start by writing this example:

```python
# Minecraft 26.1.2 + Python example
from PyMC.functions import *

# Initialize the class
HOST = "localhost"
PORT = 25575
PASSWD = "12345"
mc = MinecraftCommands(HOST, PORT, PASSWD)

# Run commands
mc.say("Hello world!")
mc._execute("say Hello Minecraft!")
```

# And try out other examples:

```bash
python PyMC/Tests/game.py
# And others..
```

---

## Project Structure

```
PythonMinecraft/
├── PyMC/                 
│   ├── functions.py      # Main functions
|   └── parse_func.py     # Parse player data (Position, inventory, etc.)
├── examples/...          # Examples
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

---

## Compatibility

Currently only tested on Minecraft Java 26.1.2
You can try other versions and share with us

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- Inspired by `mcpi`
- Minecraft® is a trademark of Mojang Studios. This project is not affiliated with Mojang.
- Some code and examples are AI generated, so it can contain bugs (sorry, im lazy :P)

---

> 🔧 **Repository Maintainer**: [@CubeAfterCube](https://github.com/cubeaftercube)
> 🐛 **Issues**: [Report a bug](https://github.com/cubeaftercube/PythonMinecraft/issues)  
> 💡 **Ideas**: [Request a feature](https://github.com/cubeaftercube/PythonMinecraft/issues)

*Last updated: June 2026*


