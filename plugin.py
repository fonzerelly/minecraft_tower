from org.bukkit import Location

from tower import createTowerAt
class TowerPlugin(PythonPlugin):
    def onEnable(self):
        self.getLogger().info("Instantiates TOWER plugin")

    def onCommand(self, sender, command, label, args):
        welt = sender.getWorld()
        position = sender.getLocation()
        self.getLogger().info("creating a tower of height: " + args[0])
        height = 0
        try:
            height = int(args[0])
        except Exception as e:
            self.getLogger().info("!!!!!!!!!!!! Failed to convert param:" + args[0])
            self.getLogger().info("!!!!!!!!!!!! Ignored to build Tower")

        material = bukkit.Material.COBBLESTONE
        if len(args) > 1:
            if args[1] == "WOOD":
                self.getLogger().info("Found WOOD")
                material = bukkit.Material.WOOD
            elif args[1] == "GOLD":
                self.getLogger().info("FOUND GOLD")
                material = bukkit.Material.GOLD_BLOCK
            elif args[1] == "TNT":
                self.getLogger().info("FOUND TNT")
                material = bukkit.Material.TNT
            elif args[1] == "OBSIDIAN":
                self.getLogger().info("FOUND OBSIDIAN")
                material = bukkit.Material.OBSIDIAN
            elif args[1] == "COAL":
                self.getLogger().info("FOUND COAL")
                material = bukkit.Material.COAL_ORE
            elif args[1] == "GLASS":
                self.getLogger().info("FOUND GLASS")
                material = bukkit.Material.GLASS
            elif args[1] == "AIR":
                self.getLogger().info("FOUND AIR")
                material = bukkit.Material.AIR
            elif args[1] == "GRAVEL":
                self.getLogger().info("FOUND GRAVEL")
                material = bukkit.Material.GRAVEL
            elif args[1] == "SAND":
                self.getLogger().info("FOUND SAND")
                material = bukkit.Material.AIR
            elif args[1] == "REDSTONE":
                self.getLogger().info("FOUND REDSTONE")
                material = bukkit.Material.REDSTONE_BLOCK
            elif args[1] == "CHEST":
                self.getLogger().info("FOUND CHEST")
                material = bukkit.Material.CHEST
            elif args[1] == "DIAMOND":
                self.getLogger().info("FOUND DIAMOND")
                material = bukkit.Material.DIAMOND_ORE
            elif args[1] == "WATER":
                self.getLogger().info("FOUND WATER")
                material = bukkit.Material.WATER
            elif args[1] == "IRON":
                self.getLogger().info("FOUND IRON")
                material = bukkit.Material.IRON_ORE
            elif args[1] == "DIAMOND":
                self.getLogger().info("FOUND DIAMOND")
                material = bukkit.Material.DIAMOND_ORE
            else:
                self.getLogger().info("!!!!!!!! Material unknown: ", args[1])
                height = 0
                self.getLogger().info("Ignored Tower")

        for tuple in createTowerAt(position, height):
            l = Location (welt, tuple[0], tuple[1], tuple[2])
            block = welt.getBlockAt(l)
            block.setType(material)

        return True