import os
from fpgaManager import *

os.system("partgen -i > inputs/boards")
os.system("python scripts/parser_boards.py inputs/boards")

fd_boards=open("inputs/boards_PARSED.txt")
while 1:
	line = fd_boards.readline()
	if not line:
		break
	fpgaName = ("").join(line.split())
	fpga = Fpga()
	fpga.loadFpga(fpgaName)

print "Done: entire database created"
