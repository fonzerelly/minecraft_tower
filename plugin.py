from org.bukkit import Location

from tower import createTowerAt
class KuerbisPlugin(PythonPlugin):
    def onEnable(self):
        self.getLogger().info("Instantiates KUERBIS plugin")

    def onCommand(self, sender, command, label, args):
        welt = sender.getWorld()
        position = sender.getLocation()
        self.getLogger().info("************** creating a tower of height: " + args[0])
        height = 0
        try:
            height = int(args[0])
        except Exception as e:
            self.getLogger().info("!!!!!!!!!!!! Failed to convert param:" + args[0])
            self.getLogger().info("!!!!!!!!!!!! Ignored to build Tower")
        
        for tuple in createTowerAt(position, height):
            l = Location (welt, tuple[0], tuple[1], tuple[2])
            block = welt.getBlockAt(l)
            block.setType(bukkit.Material.COBBLESTONE)

        return True