from org.bukkit import Location

from tower import createTowerAt
class KuerbisPlugin(PythonPlugin):
    def onEnable(self):
        self.getLogger().info("Instantiates KUERBIS plugin")

    def onCommand(self, sender, command, label, args):
        welt = sender.getWorld()
        position = sender.getLocation()
        
        for tuple in createTowerAt(position):
            self.getLogger().info("********************" + str(tuple))
            l = Location (welt, tuple[0], tuple[1], tuple[2])
            block = welt.getBlockAt(l)
            block.setType(bukkit.Material.COBBLESTONE)

        return True