from tile import tile
from xml.dom.minidom import Node
		
		
class tiles():
	def __init__(self):
		self.moduleName='tiles'
		self.a1=None
		self.a0=None
		self.tile=list()
		self._text=None
		
		
	def cleanName(self, string):
		newName=string
		if newName=='class' or newName=='xml':
			newName=newName.capitalize()
		newName=newName.replace('-','_')
		newName=newName.replace(':','_')
		
		return newName
	def get_a1(self):
		return self.a1
		
		
	def get_a0(self):
		return self.a0
		
		
	def set_a1(self,value):
		self.a1=str(value)
		
		
	def set_a0(self,value):
		self.a0=str(value)
		
		
	def get_tile(self):
		return self.tile
		
		
	def set_tile(self,tag):
		self.tile.append(tag)
		
		
	def getById(self,id):
		if hasattr(self,"id") and self.id==id:
			return self
		
		result=None
		for el in self.tile:
			result=el.getById(id)
			if result!=None:
				return result
		
		return None
		
		
	def getByAttrValues(self,className,tuples,foundList=None):
		if foundList==None:
			foundList=list()
		found=True
		if self.moduleName==self.cleanName(className):
			for t in tuples:
				attrName=self.cleanName(t[0])
				attrVal=t[1]
				if not(hasattr(self,attrName) and eval('self.'+attrName)==attrVal):
					found=found and False
			if found:
				foundList.append(self)
		
		for el in self.tile:
			el.getByAttrValues(className, tuples, foundList)
		
		return foundList
		
	def getText(self,nodeList):
		for node in nodeList:
			if node.nodeType == node.TEXT_NODE:
				if self._text == None:
					self._text=''
				self._text+=node.data
		
		
	def loadXml(self,node):
		self.getText(node.childNodes)
		if node.nodeType!=Node.ELEMENT_NODE:
			for n in node.childNodes:
				if n.nodeType==Node.ELEMENT_NODE and n.localName == 'xdl_resource_report':
					self.loadXml(n)
		else:
			for n in node.childNodes:
				if n.nodeType==Node.ELEMENT_NODE and n.localName == 'tile':
					el=tile()
					el.loadXml(n)
					self.set_tile(el)
		
			if node.hasAttributes():
				attrs=node.attributes
				attrId='a1'
				if attrId in attrs.keys():
					self.a1=str(attrs[attrId].value)
		
				attrId='a0'
				if attrId in attrs.keys():
					self.a0=str(attrs[attrId].value)
		
		
		
	def addToXmlString(self, attr, name, string):
		if attr!=None:
			string+=' '+name+'="'+attr+'"'
		return string
		
		
	def writeXml(self,outFile,indent):
		string='<'+self.moduleName
		string=self.addToXmlString(self.a1,'a1',string)
		string=self.addToXmlString(self.a0,'a0',string)
		string+='>'
		outFile.write(indent+string+'\n')
		
		indent+='	'
		for el in self.tile:
			if hasattr(el, 'writeXml'):
				el.writeXml(outFile,indent)
		
		indent=indent[:-1]
		outFile.write(indent+'</'+self.moduleName+'>\n')
		
		
