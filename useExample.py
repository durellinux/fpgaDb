from fpgaManager import *

board=Fpga()
board.loadFpga("sample")

board=Fpga()
board.loadFpga("sample2")

board=Fpga()
board.loadFpga("sample")

tile = board.getTileByXY(1,0)
print t.generalType

board.addSubClasses(t)
print t.subClasses[0].a0

board.addFather(t)
print t.father.a0
