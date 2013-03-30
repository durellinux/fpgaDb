from pin import pin
from conn import conn
from cfg import cfg
from xml.dom.minidom import Node
		
		
class element():
	def __init__(self):
		self.moduleName='element'
		self.a1=None
		self.a0=None
		self.a3=None
		self.a2=None
		self.pin=list()
		self.conn=list()
		self.cfg=list()
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
		
		
	def get_a3(self):
		return self.a3
		
		
	def get_a2(self):
		return self.a2
		
		
	def set_a1(self,value):
		self.a1=str(value)
		
		
	def set_a0(self,value):
		self.a0=str(value)
		
		
	def set_a3(self,value):
		self.a3=str(value)
		
		
	def set_a2(self,value):
		self.a2=str(value)
		
		
	def get_pin(self):
		return self.pin
		
		
	def get_conn(self):
		return self.conn
		
		
	def get_cfg(self):
		return self.cfg
		
		
	def set_pin(self,tag):
		self.pin.append(tag)
		
		
	def set_conn(self,tag):
		self.conn.append(tag)
		
		
	def set_cfg(self,tag):
		self.cfg.append(tag)
		
		
	def getById(self,id):
		if hasattr(self,"id") and self.id==id:
			return self
		
		result=None
		for el in self.pin:
			result=el.getById(id)
			if result!=None:
				return result
		
		for el in self.conn:
			result=el.getById(id)
			if result!=None:
				return result
		
		for el in self.cfg:
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
		
		for el in self.pin:
			el.getByAttrValues(className, tuples, foundList)
		
		for el in self.conn:
			el.getByAttrValues(className, tuples, foundList)
		
		for el in self.cfg:
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
				if n.nodeType==Node.ELEMENT_NODE and n.localName == 'pin':
					el=pin()
					el.loadXml(n)
					self.set_pin(el)
		
			for n in node.childNodes:
				if n.nodeType==Node.ELEMENT_NODE and n.localName == 'conn':
					el=conn()
					el.loadXml(n)
					self.set_conn(el)
		
			for n in node.childNodes:
				if n.nodeType==Node.ELEMENT_NODE and n.localName == 'cfg':
					el=cfg()
					el.loadXml(n)
					self.set_cfg(el)
		
			if node.hasAttributes():
				attrs=node.attributes
				attrId='a1'
				if attrId in attrs.keys():
					self.a1=str(attrs[attrId].value)
		
				attrId='a0'
				if attrId in attrs.keys():
					self.a0=str(attrs[attrId].value)
		
				attrId='a3'
				if attrId in attrs.keys():
					self.a3=str(attrs[attrId].value)
		
				attrId='a2'
				if attrId in attrs.keys():
					self.a2=str(attrs[attrId].value)
		
		
		
	def addToXmlString(self, attr, name, string):
		if attr!=None:
			string+=' '+name+'="'+attr+'"'
		return string
		
		
	def writeXml(self,outFile,indent):
		string='<'+self.moduleName
		string=self.addToXmlString(self.a1,'a1',string)
		string=self.addToXmlString(self.a0,'a0',string)
		string=self.addToXmlString(self.a3,'a3',string)
		string=self.addToXmlString(self.a2,'a2',string)
		string+='>'
		outFile.write(indent+string+'\n')
		
		indent+='	'
		for el in self.pin:
			if hasattr(el, 'writeXml'):
				el.writeXml(outFile,indent)
		
		for el in self.conn:
			if hasattr(el, 'writeXml'):
				el.writeXml(outFile,indent)
		
		for el in self.cfg:
			if hasattr(el, 'writeXml'):
				el.writeXml(outFile,indent)
		
		indent=indent[:-1]
		outFile.write(indent+'</'+self.moduleName+'>\n')
		
		
