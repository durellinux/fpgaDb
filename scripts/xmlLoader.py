import types
#import gc

class XmlLoader():
	class XmlTree():
		def __init__(self):
			self.subtree = list()
			self.data = None

	def __init__(self,filename):
		self.filename = filename
		self.fd = None
		self.rootXml = XmlLoader.XmlTree()
		self.allClass = dict()
		self.allClassName = list()
		self.i=0
		self.perc=0
		self.totalNumLines=0

	def __analize(self,rootXml):
		while 1:
			line = self.fd.readline()
			if self.i/(self.totalNumLines/100) == 1:
#				if self.perc % 10 == 0:
#					gc.collect()
				self.perc += 1
				self.i=0	
				print str(self.perc)+"%\t"+line,
			self.i+=1
			if not line:
				return
			words = line.split()
			if words[0][0] == '<':
				if words[0][1] != '/' and words[0][1] != '?' and words[0][1] != '!':
					# if not exist create class in self.allClass with type()
					if words[0][1:] not in self.allClassName:
						self.allClassName.append(words[0][1:])
						self.allClass[words[0][1:]] = type(words[0][1:],(),{})						
					#create an instance of class with attrs and methods, load in current rootXml
					t = XmlLoader.XmlTree()
					t.data = (self.allClass[words[0][1:]])()
					for w in words[1:len(words)-1]:
						att=w.split('=')[0]
						val=w.split('"')[1]
						t.data.__dict__[att]=val
					rootXml.subtree.append(t)
					if words[-1][-1] == '>' and len(words[-1])==1:
						# continue with depth search
						self.__analize(t)
						continue
					else:
						# continue with breadth search
						continue
				elif words[0][1] == '/':
					return
				else:
					continue

	def loadXml(self):
		try:
			self.fd = open(self.filename,"r")
			num=0
			while 1:
				if not self.fd.readline():
					break
				num+=1
			self.totalNumLines = num
			self.fd.close()
			self.fd = open(self.filename,"r")
		except	IOError as e:
			print "error: impossible to open file " + "\""+e.filename+"\""
			return False
		print str(self.perc)+"%"
		self.__analize(self.rootXml)
		self.fd.close()
		return True

	def __create_method_as_string(name,par_list,body):
		method = "def " + name + "(" + ",".join(par_list) + "): \n" + body
		return method


