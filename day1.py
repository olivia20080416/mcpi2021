from mcpi.minecraft import Minecraft
mc=Minecraft.create()


while True:
    x,y,z=mc.player.getTilePos
    mc.postToChat('X:'+str(x)+'Y:'+str(y)+'Z:'+str(z)
    
    
x,y,z=mc.player.getTilePos()
mc.setBlock(x,y,z,20)
mc.setBlock(x,y+1,z,20)
mc.setBlock(x,y+2,z,20)
mc.setBlock(x,y+3,z,20)
mc.setBlock(x,y+4,z,20)

x,y,z=mc.player.getTilePos()
mc.setBlock(x+1,y,z,20)           
mc.setBlock(x-1,y,z,20)         
mc.setBlock(x,y,z+1,20)            
mc.setBlock(x,y,z-1,20)          
mc.setBlock(x+1,y,z+1,20)            
mc.setBlock(x-1,y,z+1,20)        
mc.setBlock(x-1,y,z-1,20)           
            
x,y,z=mc.player.getTilePos()            
mc.setBlocks(x+10,y,z+10,x-10,y,z-10,20)            
            











            
            
            
            