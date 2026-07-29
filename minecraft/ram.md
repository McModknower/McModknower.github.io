McModknower's Ram Recommendation
================================

Start with the ram suggested by the modpack author/your launcher/4 gigs.
Also make sure you have the usual optimization mods, especially [FerriteCore](https://modrinth.com/mod/ferrite-core).

Then test it and depending on what happens change stuff.

1. If Minecraft/your pc starts lagging and your systems task manager shows you that your ram is (nearly) full,  
   you are using up all the ram on your pc. Allocate less ram to mc and/or close other programs to free up some ram.

2. If Minecraft crashes during starting / world loading and the `latest.log` contains `java.lang.OutOfMemoryError: Java heap space`,  
   you need to allocate more ram or lower what mc needs.

3. Once you get into a world, check the ram allocation in your debug (aka F3) screen.  
   If its constantly near 100%, and every time it drops you have a (minor) lag spike, you have allocated too little ram to mc.  
   If its constantly below 70%, you probably allocated too much.

4. If rule 2 or 3 say you should allocate more, but your ram is full (rule 1) and you can't close more programs,  
   you need to lower the ram load of minecraft. This can be done by  
   - lowering the render/simulation distance
   - lowering the render distance of mods like Distant Horizons, Voxy, or Bobby (if you have them)
   - using a less demanding shader, or no shader at all
   - disabling mods like Distant Horizons, Voxy, or Bobby (if you have them)
   - making a backup and disabling content mods
