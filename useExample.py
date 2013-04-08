from fpgaManager import *

x=Fpga()
x.loadFpga("sample")

x=Fpga()
x.loadFpga("sample2")

x=Fpga()
x.loadFpga("sample")
x.getTileByXY(0,88).generalType
x.getTileByXY(0,88).specificType
