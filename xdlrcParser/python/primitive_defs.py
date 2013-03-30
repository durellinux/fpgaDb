from primitive_def import primitive_def
from xml.dom.minidom import Node
		
		
class primitive_defs():
	def __init__(self):
		self.moduleName='primitive_defs'
		self.a0=None
		self.primitive_def=list()
		self._text=None
		
		
	def cleanName(self, string):
		newName=string
		if newName=='class' or newName=='xml':
			newName=newName.capitalize()
		newName=newName.replace('-','_')
		newName=newName.replace(':','_')
		
		return newName
	def get_a0(self):
		return self.a0
		
		
	def set_a0(self,value):
		self.a0=str(value)
		
		
	def get_primitive_def(self):
		return self.primitive_def
		
		
	def set_primitive_def(self,tag):
		self.primitive_def.append(tag)
		
		
	def getById(self,id):
		if hasattr(self,"id") and self.id==id:
			return self
		
		result=None
		for el in self.primitive_def:
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
		
		for el in self.primitive_def:
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
				if n.nodeType==Node.ELEMENT_NODE and n.localName == 'primitive_def':
					el=primitive_def()
					el.loadXml(n)
					self.set_primitive_def(el)
		
			if node.hasAttributes():
				attrs=node.attributes
				attrId='a0'
				if attrId in attrs.keys():
					self.a0=str(attrs[attrId].value)
		
		
		
	def addToXmlString(self, attr, name, string):
		if attr!=None:
			string+=' '+name+'="'+attr+'"'
		return string
		
		
	def writeXml(self,outFile,indent):
		string='<'+self.moduleName
		string=self.addToXmlString(self.a0,'a0',string)
		string+='>'
		outFile.write(indent+string+'\n')
		
		indent+='	'
		for el in self.primitive_def:
			if hasattr(el, 'writeXml'):
				el.writeXml(outFile,indent)
		
		indent=indent[:-1]
		outFile.write(indent+'</'+self.moduleName+'>\n')
		
		
