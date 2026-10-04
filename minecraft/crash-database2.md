Modded Minecraft Crash Database 2
=================================

This file contains crashes I want to be able to search through quickly, followed by messages i can copy and paste into discord for others.
For more info on different kinds of crashes, see the [Modded Minecraft Crash Database](crash-database).

Caused by: java.lang.NoSuchMethodError: 'net.caffeinemc.mods.sodium.client.gui.SodiumGameOptions net.caffeinemc.mods.sodium.client.SodiumClientMod.options()'	at ca.fxco.moreculling.utils.CullingUtils.areLeavesOpaque:L93
update morculling to 1.0.8 or above

Caused by: java.lang.NoSuchMethodError: 'net.caffeinemc.mods.sodium.client.gui.SodiumOptions net.caffeinemc.mods.sodium.client.SodiumClientMod.options()'	at ca.fxco.moreculling.utils.CullingUtils.areLeavesOpaque:L93
downgrade morculling to 1.0.7

java.lang.NoSuchMethodError: 'void net.caffeinemc.mods.sodium.client.gl.shader.GlShader.<init>(net.caffeinemc.mods.sodium.client.gl.shader.ShaderType, net.minecraft.resources.ResourceLocation, java.lang.String)'	at net.irisshaders.iris.pipeline.programs.SodiumPrograms.createGlShaders:L99
your iris version is incompatible with your sodium version. remove iris or update it to 1.8.14-beta.1+1.21.1-neoforge or above

[modloading-worker-0/ERROR] [net.neoforged.fml.javafmlmod.FMLModContainer/LOADING]: Failed to create mod instance. ModID: chiselsandbits, class mod.chiselsandbits.forge.Forgejava.lang.NoClassDefFoundError: com/communi/suggestu/saecularia/caudices/core/block/IBlockWithWorldlyProperties
Downgrade chisels & bits to 21.1.32

at net.minecraft.SystemReport.handler$zoj000$iris$fillSystemDetails:L523
You have iris but not sodium. Install sodium.

java.lang.IllegalStateException: Item: galosphere:silver_ingot does not exist
Galosphere removed the silver ingot in an update, at a time where a bunch of other mods no longer supported/updated their mc 1.20.1 versions.
[Create: Fixed](https://www.curseforge.com/minecraft/mc-mods/create-fixed) fixes this IF you are in mc 1.20.1 AND have create.

java.lang.NoClassDefFoundError: vectorwing/farmersdelight/common/block/ShepherdsPieBlock	at net.fixerlink.alexscavesdelight.alexscavesdelight.<init>:L32
alexcavesdelight is not updated for farmersdelight. remove alexcavesdelight.

java.lang.IllegalArgumentException: Soup base with name minecraft:milk already exists!
https://github.com/KaleidoscopeMods/KaleidoscopeCookery/issues/215
