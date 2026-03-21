Modded Minecraft Usual Suspects
===============================

This is a list of usual suspects in case of modded Minecraft problems.
See also my [Modded Minecraft Crash Database](crash-database.html) for examples of crash reports and logs.
Also [superpowers04's Recommendations On What To Avoid](https://github.com/superpowers04/superpowers04/wiki/MC-Recommendations-On-What-To-Avoid) are a good resource

# Crashing/Incompatibilities

- Optifine (closed source, changes a lot of rendering related code, known for breaking mods)
- Lunar (obfuscated, changes a lot of stuff, known for breaking mods)
- Essential (collects Telemetry (once crashed while doing that), does LAN on modded which can break stuff)
- LabyMod
- anything popular with a bunch of add-ons, especially after a recent update
  - Create add-ons
  - Epic Fight add-ons
  - Relics compatibility/add-ons
  - cobblemon mega showdown

# Weird Bugs
Stuff you can't describe well, unreadable stack traces/logs, ...

- Essential
- MCreator mods (this also applies in cases of lags)
- any "clients"

# Slow Data Packs
Some functionality can be implemented via data packs.
This is not always a good idea, as seen in the data packs (sometimes packaged as mods) in this section.

## Entity NBT lookup
When a data pack tries to check what item a player/entity is holding, it has to do that via the `nbt` selector.
This causes the entire data of the entity to get serialized.
If this is done every tick, you get a slow and laggy world.
Especially if you have more crafting recipes, since the recipes a player unlocked in their recipe book are part of the players NBT data as well.

Data packs i know that do this are:

- any dynamic light data pack: to check if you are holding a torch or similar.
  Never use any kind of dynamic lights data pack.
  Use a client-side mod like [LambDynamicLights](https://modrinth.com/mod/lambdynamiclights) instead.
- Enchants Plus: it has a Luminosity enchantment. Same problem as dynamic light data packs above.
  Also Ice Aspect and Gluttony check nbt data, but they are not as bad as Luminosity.

# Graphically Demanding Mods
If your game is lagging, try disabling graphically demanding mods first, since they are, well, graphically demanding.

- Distant horizons
- Bobby
- Iris/Oculus (or any other shader)

