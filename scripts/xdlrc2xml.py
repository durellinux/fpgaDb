import sys

pushdown = []

def add_attr(line):
	words = line.split()
	entity = words[0]
	words = words[1:-1]
	i=0	
	for w in words:
		line = line.replace(w,"!",1)
		i+=1

'''	# create generalType for entity
	tile_att = ['x','y','generalType','specificType','num']
	if entity == '<tile':
		tag = words[2]
		generalType = ""
		count = len(tag)-1
		for c in tag[::-1]:
			if c=='X':
				break
			else:
				count -= 1
		generalType = tag[0:count-1]
		tileX = tag[count+1:].split('Y')[0]
		tileY = tag[count+1:].split('Y')[1]
		words.remove(tag)
		words.insert(2,generalType + "\" tileX=\""+tileX+"\" tileY=\""+tileY)
	#####
'''
	i=0
	for w in words:
		line = line.replace("!","a"+str(i)+"=\""+w+"\"",1)
'''		if entity == '<tile':
			line = line.replace("!",tile_att[i]+"=\""+w+"\"",1)
		else:
			line = line.replace("!","a"+str(i)+"=\""+w+"\"",1) '''
		i+=1
	return line

def replace(line,numLine):
	if line.count("<")+line.count(">")+line.count("&") > 0 :
		#print str(numLine)+" "+ line,
		line=line.replace("<","LESS")
		line=line.replace(">","GREATER")
		line=line.replace("&","AMPERSAND")
	words = line.split()
	if words[0][0]=='(' :
		pushdown.append(words[0][1:])
		line = line.replace('(','<',1) # changed
		if words[len(words)-1][len(words[len(words)-1])-1] == ')' :
			pushdown.pop()
			line = line[0:len(line)-2] + ' />\n' #changed
		else:
			line = line.replace('\n',' >\n')
		line = add_attr(line)
	elif words[0][0]==')':
		line = line.replace(')','</'+pushdown.pop()+'>')
	elif words[0][0] == '#':
		line = line.replace('#','<!-- #')
		line = line.replace('\n',' -->\n')
	else:
		line = "\n"
	return line
		

if len(sys.argv)<2:
	print "error: missing filename"
	print "type: \"python "+sys.argv[0]+" filename\""
	sys.exit(-1)
try:
	file_input = open(sys.argv[1],"r")
	outFile=sys.argv[1].split(".")[0]
	file_output = open(outFile+".xml","w")
except	IOError as e:
	print "error: impossible to open file " + "\""+e.filename+"\""
	sys.exit(-1)

file_output.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n")
line = file_input.readline()
i=0
while 1:
	if not line:
		break
	newline = replace(line,i)
	file_output.write(newline)
	line = file_input.readline()
	i+=1

print "Done: xml from xdlrc created"
file_input.close()
file_output.close()
sys.exit(0)
