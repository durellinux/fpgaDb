import sys

def print2file(board, f):
	for i in board:
		for j in i:
			f.write(j + " ")
		f.write("\n")

if len(sys.argv)<2:
	print "error: missing filename"
	print "type: \"python "+sys.argv[0]+" filename\""
	sys.exit(-1)
try:
	file_input = open(sys.argv[1],"r")
	file_output = open(sys.argv[1]+"_PARSED.txt","w")
except	IOError as e:
	print "error: impossible to open file " + "\""+e.filename+"\""
	sys.exit(-1)

line = file_input.readline()
while 1:
	board = ""
	models = []
	speeds = []
	exclude = []
	if not line:
		break
	if line[0]=='x':
		row = filter(lambda x: x[0]=='x' or x[0]=='-',line.split())
		board = row[0]
		speeds = row[1:]
		line = file_input.readline()
		if not line:
			break
		while line[0]==' ':
			row = line.split()
			models += [row[0]]
			if len(row)>1:
				exclude += [(row[0],x) for x in speeds if x not in row[1:] ]
			line = file_input.readline()
			if not line:
				break
		allComb = [[board, y, z] for y in models for z in speeds if not ((y,z) in exclude)]
		print2file(allComb,file_output)
	else:
		line = file_input.readline()
print "Done"
file_input.close()
file_output.close()
sys.exit(0)
