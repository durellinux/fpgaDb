from fpgaManager import *

board=Fpga()
board.loadFpga("sample")

board=Fpga()
board.loadFpga("sample2")

#board=Fpga()
#board.loadFpga("sample")

tile = board.getTileByXY(1,0)
print tile.a2

board.addSubClasses(tile)
print tile.subClasses[0].a0

board.addFather(tile)
print tile.father.a0
