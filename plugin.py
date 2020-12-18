class KuerbisPlugin(PythonPlugin):
    def onEnable(self):
        pass

    def onCommand(self, sender, command, label, args):
        welt = sender.getWorld()
        position = sender.getLocation()
        position.setX(position.getX() + 2)
        ursprungY = position.getY()
        
        for i in range(0,10):
            position.setY(ursprungY + i)
            block = welt.getBlockAt(position)
            block.setType(bukkit.Material.PUMPKIN)

        return True