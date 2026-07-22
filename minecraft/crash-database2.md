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
