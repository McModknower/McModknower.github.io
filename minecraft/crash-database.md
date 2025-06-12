Modded Minecraft Crash Database
===============================

This file will contain a bunch of error messages from modded minecraft crashes, with the intent that you can use your browsers search function to quickly search for your problem.

Most of the stuff i write about here is stuff i found in logs people asked for help with on the [Modded Minecraft Discord](https://discord.gg/moddedmc). If you need more help than this guide can provide, i can only recommend asking over there.

## What to search for

To search for an error, you need to know what part of the crash report you should search for.
On this site i will mostly only include the exception itself as text, so get that one.

### `crash-<DATE>_<TIME>-<SIDE>.txt`
In a crash report (for example a file like `crash-2025-03-29_13.24.00-client.txt`, which begins with `---- Minecraft Crash Report ----`), the exception is normally pretty close to the top and contains `Exception` or `Error`. Check the following image for an example.

![](crash-report-where-is-the-error.png)

### `latest.log`
In a `latest.log`, the excpetion is normally close to the bottom of the log, as seen in the following image, and contains `Exception` or `Error` like in a crash report.

![](latest-log-where-is-the-error.png)

However it can also happen that the latest log contains lines like the following:
```
[04Apr2025 22:53:51.730] [Render thread/ERROR] [net.neoforged.fml.ModLoader/]: Cowardly refusing to send event net.neoforged.neoforge.client.event.TextureAtlasStitchedEvent to a broken mod state
```
If you see any line like this (starting with `Cowardly refusing to send event` and ending with `to a broken mod state`), that means the real error happened before the first one of these lines. Scroll up or use you editors/log viewers search feature to go to the first one, then go up to the closest exception.

Sometimes the latest log does not contain the error, then you have to get one of the other files listed here.

### `launcher_log.txt`
Launcherlogs have the error message normally near the last line that contains `MinecraftJavaLoggingContext`, as shown in the following image.

### `hs_err_pid<number>.log`
JVM crash reports (`hs_err_pid<number>.log`) are very different and will be listed here sometime in the future, but are not the focus for now.

## The errors that are not actually the error

`Exception in thread "main" java.lang.RuntimeException: java.lang.reflect.InvocationTargetException`
`Caused by: java.lang.reflect.InvocationTargetException`

### `java.lang.RuntimeException: null`
This one is a generic error and means you need to look further down for lines starting with `Suppressed` or `Caused by` to find the real error

### `java.lang.Exception: Mod Loading has failed`
This one is a generic error and means you have to go below the `A detailed walkthrough of the error, its code path and all known details is as follows:` line to find the real cause. Like above, check for lines starting with `Suppressed` or `Caused by`. Additionally, lines containing `Failure message:` or `Exception message:` can mark interesting points.

### `java.lang.IllegalStateException: Failed to load registries due to above errors`
This means some registry errors occured. Those are only visible in the latest log, so check it.
I personally search for `>>` in the log, but make sure to find the correct entry. I don't have an example currently, so i will add an example how it looks later.

## Incompatibilities

### `java.lang.NoClassDefFoundError` and `java.lang.ClassNotFoundException`

This error normally means one of the following things:

- You have a mod which needs some other mod (dependency) which is not installed.
  In this case, install the dependency or remove the mod.
- You have a mod (A) which has compatibility with some other mod (B) build in, but A was made for a different version of B.
  In this case, change the version(s) of these mods until it works. Normally updating both (or just A) works
- you have a mixin error somewhere before in the latest log
  In this case go to that error (it will contain `mixin` somewhere) and search for that exception message.

#### Create 6
Create 6 broke a bunch of compatibilities that mods had buildin. if you get any of the exceptions listed here, check what mod is listed directly below that error and update it to a version that supports create 6, or disable that mod.

For Example in the following case, computercraft (aka `cc: tweaked`) is the mod that needs to be updated:
```
 Suppressed: java.lang.NoClassDefFoundError: com/simibubi/create/content/contraptions/BlockMovementChecks$AttachedCheck
	at dan200.computercraft.shared.integration.CreateIntegration.setup:L23
```

- `Suppressed: java.lang.NoClassDefFoundError: com/simibubi/create/content/contraptions/BlockMovementChecks$AttachedCheck`
  `Caused by: java.lang.ClassNotFoundException: com.simibubi.create.content.contraptions.BlockMovementChecks$AttachedCheck`
  known mods that can cause this: computercraft

- `Caused by 0: java.lang.NoClassDefFoundError: Could not initialize class com.simibubi.create.AllBlocks`
  known mods that can cause this: railways (aka Create: Steam 'n' Rails)

- `Caused by: java.lang.NoClassDefFoundError: com/simibubi/create/api/registry/CreateRegistries`
  known mods that can cause this issue: adastra

### `java.lang.UnsupportedClassVersionError`
This one means you have a .jar which was made for a newer java version than the one you have.
It is caused by having a mod for a newer minecraft version, using the wrong java version ([MultiMC Wiki Page on using the right Java](https://github.com/MultiMC/Launcher/wiki/Using-the-right-Java)), or having a mod author provide a faulty mod.

Most likely it will be the first case, like in the following example where someone had a newer version of cloth config:
```
		java.lang.UnsupportedClassVersionError: me/shedaniel/clothconfig/ClothConfigForge has been compiled by a more recent version of the Java Runtime (class file version 65.0), this version of the Java Runtime only recognizes class file versions up to 61.0
```

### mixin errors
`org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError: An unexpected critical error was encountered`
`Caused by: org.spongepowered.asm.mixin.injection.throwables.InjectionError: Critical injection failure:`
`Caused by: java.lang.RuntimeException: org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError: An unexpected critical error was encountered`
`Caused by: org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError: An unexpected critical error was encountered`


These errors are from the mixin system, which is made to allow changing code from other mods or minecraft itself.
They normally indicate incompatibilities between different mods, but can also mean you are running a mod on a minecraft version it doesn't work with.
Skim through the rest of the line(s) for mod names, those are the ones involved. Try disabling them. If it works, check for up/downgrades, like above for the `NoClassDefFoundError`.
If there is no mod in the first line with one of these errors, check the `Caused by` lines below it for mod names.


## RAM problems

### `java.lang.OutOfMemoryError: Java heap space`
That means you need to allocate more ram (-Xmx) to your modpack, or you have to reduce the load by using less shaders, resource packs, mods, etc.

## Uncategorized

### `java.lang.NullPointerException: Registry Object not present:`
This can be caused by a mod that is installed on your client but not on your server. If that is the case, you can simply remove the mod from your client to fix the problem.

The mod in question is the one named directly after the colon in that line, for example in the following line it is hardcore_torches.
```
java.lang.NullPointerException: Registry Object not present: hardcore_torches:lit_torch
```

### `com.google.gson.JsonSyntaxException: Expected a com.google.gson.JsonArray but was com.google.gson.JsonObject; at path $`
Some json file is broken. If this happens on a server, check if your `banned-ips.json` and `banned-players.json` contain `{}`. If yes, simply delete the file(s) containing just `{}`.
