Modded Minecraft Usual Suspects
===============================

This is a list of usual suspects in case of modded minecraft problems.
See also my [Modded Minecraft Crash Database](crash-database.html) for examples of crash reports and logs.
Also [superpowers04's Recommendations On What To Avoid](https://github.com/superpowers04/superpowers04/wiki/MC-Recommendations-On-What-To-Avoid) are a good resource

# Crashing/Incompatibilities

- Optifine (closed source, changes a lot of rendering related code, known for breaking mods)
- Lunar (obfuscated, changes a lot of stuff, known for breaking mods)
- Essential (collects Telemetry (once crashed while doing that), does lan on modded which can break stuff)
- LabyMod
- aynthing popular with a bunch of addons, especially after a recent update
  - Create addons
  - Epicfight addons
  - Relics compatibility/addons
  - cobblemon mega showdown

# Weird Bugs
Stuff you can't describe well, unreadable stacktraces/logs, ...

- Essential
- MCreator mods (this also applies in cases of lags)
- any "clients"

# Slow Datapacks
Some functionality can be implemented via datapacks.
This is not always a good idea, as seen in the datapacks (sometimes packaged as mods) in this section.

## Entity NBT lookup
When a datapack tries to check what item a player/entity is holding, it has to do that via the `nbt` selector.
This causes the entire data of the entity to get serialized.
If this is done every tick, you get a slow and laggy world.
Especially if you have more crafting recipes, since the recipes a player unlocked in their recipe book are part of the players NBT data as well.

Datapacks i know that do this are:

- any dynamic light datapack: to check if you are holding a torch or similar.
  Never use any kind of dynamiclights datapack.
  Use a client-side mod like [LambDynamicLights](https://modrinth.com/mod/lambdynamiclights) instead.
- Enchants Plus: it has a Luminousity enchantment. Same problem as dynamic light datapacks above.
  Also Ice Aspect and Gluttony check nbt data, but they are not as bad as Luminosity.

# Graphically Demanding Mods
If your game is lagging, try disabling graphically demanding mods first, since they are, well, graphically demanding.

- Distant horizons
- Bobby
- Iris/Oculus (or any other shader)

