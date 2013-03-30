from xml.dom.minidom import Node
		
		
class cfg():
	def __init__(self):
		self.moduleName='cfg'
		self.a1=None
		self.a0=None
		self.a3=None
		self.a2=None
		self.a5=None
		self.a4=None
		self.a7=None
		self.a6=None
		self.a8=None
		self.a20=None
		self.a21=None
		self.a22=None
		self.a23=None
		self.a24=None
		self.a25=None
		self.a26=None
		self.a27=None
		self.a28=None
		self.a29=None
		self.a31=None
		self.a30=None
		self.a15=None
		self.a14=None
		self.a17=None
		self.a16=None
		self.a11=None
		self.a10=None
		self.a13=None
		self.a12=None
		self.a19=None
		self.a18=None
		self.a9=None
		self.a60=None
		self.a37=None
		self.a36=None
		self.a33=None
		self.a35=None
		self.a34=None
		self.a51=None
		self.a50=None
		self.a53=None
		self.a52=None
		self.a55=None
		self.a54=None
		self.a57=None
		self.a56=None
		self.a59=None
		self.a58=None
		self.a32=None
		self.a39=None
		self.a38=None
		self.a46=None
		self.a47=None
		self.a44=None
		self.a45=None
		self.a42=None
		self.a43=None
		self.a40=None
		self.a41=None
		self.a48=None
		self.a49=None
		self.a62=None
		self.a63=None
		self.a61=None
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
		
		
	def get_a5(self):
		return self.a5
		
		
	def get_a4(self):
		return self.a4
		
		
	def get_a7(self):
		return self.a7
		
		
	def get_a6(self):
		return self.a6
		
		
	def get_a8(self):
		return self.a8
		
		
	def get_a20(self):
		return self.a20
		
		
	def get_a21(self):
		return self.a21
		
		
	def get_a22(self):
		return self.a22
		
		
	def get_a23(self):
		return self.a23
		
		
	def get_a24(self):
		return self.a24
		
		
	def get_a25(self):
		return self.a25
		
		
	def get_a26(self):
		return self.a26
		
		
	def get_a27(self):
		return self.a27
		
		
	def get_a28(self):
		return self.a28
		
		
	def get_a29(self):
		return self.a29
		
		
	def get_a31(self):
		return self.a31
		
		
	def get_a30(self):
		return self.a30
		
		
	def get_a15(self):
		return self.a15
		
		
	def get_a14(self):
		return self.a14
		
		
	def get_a17(self):
		return self.a17
		
		
	def get_a16(self):
		return self.a16
		
		
	def get_a11(self):
		return self.a11
		
		
	def get_a10(self):
		return self.a10
		
		
	def get_a13(self):
		return self.a13
		
		
	def get_a12(self):
		return self.a12
		
		
	def get_a19(self):
		return self.a19
		
		
	def get_a18(self):
		return self.a18
		
		
	def get_a9(self):
		return self.a9
		
		
	def get_a60(self):
		return self.a60
		
		
	def get_a37(self):
		return self.a37
		
		
	def get_a36(self):
		return self.a36
		
		
	def get_a33(self):
		return self.a33
		
		
	def get_a35(self):
		return self.a35
		
		
	def get_a34(self):
		return self.a34
		
		
	def get_a51(self):
		return self.a51
		
		
	def get_a50(self):
		return self.a50
		
		
	def get_a53(self):
		return self.a53
		
		
	def get_a52(self):
		return self.a52
		
		
	def get_a55(self):
		return self.a55
		
		
	def get_a54(self):
		return self.a54
		
		
	def get_a57(self):
		return self.a57
		
		
	def get_a56(self):
		return self.a56
		
		
	def get_a59(self):
		return self.a59
		
		
	def get_a58(self):
		return self.a58
		
		
	def get_a32(self):
		return self.a32
		
		
	def get_a39(self):
		return self.a39
		
		
	def get_a38(self):
		return self.a38
		
		
	def get_a46(self):
		return self.a46
		
		
	def get_a47(self):
		return self.a47
		
		
	def get_a44(self):
		return self.a44
		
		
	def get_a45(self):
		return self.a45
		
		
	def get_a42(self):
		return self.a42
		
		
	def get_a43(self):
		return self.a43
		
		
	def get_a40(self):
		return self.a40
		
		
	def get_a41(self):
		return self.a41
		
		
	def get_a48(self):
		return self.a48
		
		
	def get_a49(self):
		return self.a49
		
		
	def get_a62(self):
		return self.a62
		
		
	def get_a63(self):
		return self.a63
		
		
	def get_a61(self):
		return self.a61
		
		
	def set_a1(self,value):
		self.a1=str(value)
		
		
	def set_a0(self,value):
		self.a0=str(value)
		
		
	def set_a3(self,value):
		self.a3=str(value)
		
		
	def set_a2(self,value):
		self.a2=str(value)
		
		
	def set_a5(self,value):
		self.a5=str(value)
		
		
	def set_a4(self,value):
		self.a4=str(value)
		
		
	def set_a7(self,value):
		self.a7=str(value)
		
		
	def set_a6(self,value):
		self.a6=str(value)
		
		
	def set_a8(self,value):
		self.a8=str(value)
		
		
	def set_a20(self,value):
		self.a20=str(value)
		
		
	def set_a21(self,value):
		self.a21=str(value)
		
		
	def set_a22(self,value):
		self.a22=str(value)
		
		
	def set_a23(self,value):
		self.a23=str(value)
		
		
	def set_a24(self,value):
		self.a24=str(value)
		
		
	def set_a25(self,value):
		self.a25=str(value)
		
		
	def set_a26(self,value):
		self.a26=str(value)
		
		
	def set_a27(self,value):
		self.a27=str(value)
		
		
	def set_a28(self,value):
		self.a28=str(value)
		
		
	def set_a29(self,value):
		self.a29=str(value)
		
		
	def set_a31(self,value):
		self.a31=str(value)
		
		
	def set_a30(self,value):
		self.a30=str(value)
		
		
	def set_a15(self,value):
		self.a15=str(value)
		
		
	def set_a14(self,value):
		self.a14=str(value)
		
		
	def set_a17(self,value):
		self.a17=str(value)
		
		
	def set_a16(self,value):
		self.a16=str(value)
		
		
	def set_a11(self,value):
		self.a11=str(value)
		
		
	def set_a10(self,value):
		self.a10=str(value)
		
		
	def set_a13(self,value):
		self.a13=str(value)
		
		
	def set_a12(self,value):
		self.a12=str(value)
		
		
	def set_a19(self,value):
		self.a19=str(value)
		
		
	def set_a18(self,value):
		self.a18=str(value)
		
		
	def set_a9(self,value):
		self.a9=str(value)
		
		
	def set_a60(self,value):
		self.a60=str(value)
		
		
	def set_a37(self,value):
		self.a37=str(value)
		
		
	def set_a36(self,value):
		self.a36=str(value)
		
		
	def set_a33(self,value):
		self.a33=str(value)
		
		
	def set_a35(self,value):
		self.a35=str(value)
		
		
	def set_a34(self,value):
		self.a34=str(value)
		
		
	def set_a51(self,value):
		self.a51=str(value)
		
		
	def set_a50(self,value):
		self.a50=str(value)
		
		
	def set_a53(self,value):
		self.a53=str(value)
		
		
	def set_a52(self,value):
		self.a52=str(value)
		
		
	def set_a55(self,value):
		self.a55=str(value)
		
		
	def set_a54(self,value):
		self.a54=str(value)
		
		
	def set_a57(self,value):
		self.a57=str(value)
		
		
	def set_a56(self,value):
		self.a56=str(value)
		
		
	def set_a59(self,value):
		self.a59=str(value)
		
		
	def set_a58(self,value):
		self.a58=str(value)
		
		
	def set_a32(self,value):
		self.a32=str(value)
		
		
	def set_a39(self,value):
		self.a39=str(value)
		
		
	def set_a38(self,value):
		self.a38=str(value)
		
		
	def set_a46(self,value):
		self.a46=str(value)
		
		
	def set_a47(self,value):
		self.a47=str(value)
		
		
	def set_a44(self,value):
		self.a44=str(value)
		
		
	def set_a45(self,value):
		self.a45=str(value)
		
		
	def set_a42(self,value):
		self.a42=str(value)
		
		
	def set_a43(self,value):
		self.a43=str(value)
		
		
	def set_a40(self,value):
		self.a40=str(value)
		
		
	def set_a41(self,value):
		self.a41=str(value)
		
		
	def set_a48(self,value):
		self.a48=str(value)
		
		
	def set_a49(self,value):
		self.a49=str(value)
		
		
	def set_a62(self,value):
		self.a62=str(value)
		
		
	def set_a63(self,value):
		self.a63=str(value)
		
		
	def set_a61(self,value):
		self.a61=str(value)
		
		
	def getById(self,id):
		if hasattr(self,"id") and self.id==id:
			return self
		
		result=None
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
		
				attrId='a5'
				if attrId in attrs.keys():
					self.a5=str(attrs[attrId].value)
		
				attrId='a4'
				if attrId in attrs.keys():
					self.a4=str(attrs[attrId].value)
		
				attrId='a7'
				if attrId in attrs.keys():
					self.a7=str(attrs[attrId].value)
		
				attrId='a6'
				if attrId in attrs.keys():
					self.a6=str(attrs[attrId].value)
		
				attrId='a8'
				if attrId in attrs.keys():
					self.a8=str(attrs[attrId].value)
		
				attrId='a20'
				if attrId in attrs.keys():
					self.a20=str(attrs[attrId].value)
		
				attrId='a21'
				if attrId in attrs.keys():
					self.a21=str(attrs[attrId].value)
		
				attrId='a22'
				if attrId in attrs.keys():
					self.a22=str(attrs[attrId].value)
		
				attrId='a23'
				if attrId in attrs.keys():
					self.a23=str(attrs[attrId].value)
		
				attrId='a24'
				if attrId in attrs.keys():
					self.a24=str(attrs[attrId].value)
		
				attrId='a25'
				if attrId in attrs.keys():
					self.a25=str(attrs[attrId].value)
		
				attrId='a26'
				if attrId in attrs.keys():
					self.a26=str(attrs[attrId].value)
		
				attrId='a27'
				if attrId in attrs.keys():
					self.a27=str(attrs[attrId].value)
		
				attrId='a28'
				if attrId in attrs.keys():
					self.a28=str(attrs[attrId].value)
		
				attrId='a29'
				if attrId in attrs.keys():
					self.a29=str(attrs[attrId].value)
		
				attrId='a31'
				if attrId in attrs.keys():
					self.a31=str(attrs[attrId].value)
		
				attrId='a30'
				if attrId in attrs.keys():
					self.a30=str(attrs[attrId].value)
		
				attrId='a15'
				if attrId in attrs.keys():
					self.a15=str(attrs[attrId].value)
		
				attrId='a14'
				if attrId in attrs.keys():
					self.a14=str(attrs[attrId].value)
		
				attrId='a17'
				if attrId in attrs.keys():
					self.a17=str(attrs[attrId].value)
		
				attrId='a16'
				if attrId in attrs.keys():
					self.a16=str(attrs[attrId].value)
		
				attrId='a11'
				if attrId in attrs.keys():
					self.a11=str(attrs[attrId].value)
		
				attrId='a10'
				if attrId in attrs.keys():
					self.a10=str(attrs[attrId].value)
		
				attrId='a13'
				if attrId in attrs.keys():
					self.a13=str(attrs[attrId].value)
		
				attrId='a12'
				if attrId in attrs.keys():
					self.a12=str(attrs[attrId].value)
		
				attrId='a19'
				if attrId in attrs.keys():
					self.a19=str(attrs[attrId].value)
		
				attrId='a18'
				if attrId in attrs.keys():
					self.a18=str(attrs[attrId].value)
		
				attrId='a9'
				if attrId in attrs.keys():
					self.a9=str(attrs[attrId].value)
		
				attrId='a60'
				if attrId in attrs.keys():
					self.a60=str(attrs[attrId].value)
		
				attrId='a37'
				if attrId in attrs.keys():
					self.a37=str(attrs[attrId].value)
		
				attrId='a36'
				if attrId in attrs.keys():
					self.a36=str(attrs[attrId].value)
		
				attrId='a33'
				if attrId in attrs.keys():
					self.a33=str(attrs[attrId].value)
		
				attrId='a35'
				if attrId in attrs.keys():
					self.a35=str(attrs[attrId].value)
		
				attrId='a34'
				if attrId in attrs.keys():
					self.a34=str(attrs[attrId].value)
		
				attrId='a51'
				if attrId in attrs.keys():
					self.a51=str(attrs[attrId].value)
		
				attrId='a50'
				if attrId in attrs.keys():
					self.a50=str(attrs[attrId].value)
		
				attrId='a53'
				if attrId in attrs.keys():
					self.a53=str(attrs[attrId].value)
		
				attrId='a52'
				if attrId in attrs.keys():
					self.a52=str(attrs[attrId].value)
		
				attrId='a55'
				if attrId in attrs.keys():
					self.a55=str(attrs[attrId].value)
		
				attrId='a54'
				if attrId in attrs.keys():
					self.a54=str(attrs[attrId].value)
		
				attrId='a57'
				if attrId in attrs.keys():
					self.a57=str(attrs[attrId].value)
		
				attrId='a56'
				if attrId in attrs.keys():
					self.a56=str(attrs[attrId].value)
		
				attrId='a59'
				if attrId in attrs.keys():
					self.a59=str(attrs[attrId].value)
		
				attrId='a58'
				if attrId in attrs.keys():
					self.a58=str(attrs[attrId].value)
		
				attrId='a32'
				if attrId in attrs.keys():
					self.a32=str(attrs[attrId].value)
		
				attrId='a39'
				if attrId in attrs.keys():
					self.a39=str(attrs[attrId].value)
		
				attrId='a38'
				if attrId in attrs.keys():
					self.a38=str(attrs[attrId].value)
		
				attrId='a46'
				if attrId in attrs.keys():
					self.a46=str(attrs[attrId].value)
		
				attrId='a47'
				if attrId in attrs.keys():
					self.a47=str(attrs[attrId].value)
		
				attrId='a44'
				if attrId in attrs.keys():
					self.a44=str(attrs[attrId].value)
		
				attrId='a45'
				if attrId in attrs.keys():
					self.a45=str(attrs[attrId].value)
		
				attrId='a42'
				if attrId in attrs.keys():
					self.a42=str(attrs[attrId].value)
		
				attrId='a43'
				if attrId in attrs.keys():
					self.a43=str(attrs[attrId].value)
		
				attrId='a40'
				if attrId in attrs.keys():
					self.a40=str(attrs[attrId].value)
		
				attrId='a41'
				if attrId in attrs.keys():
					self.a41=str(attrs[attrId].value)
		
				attrId='a48'
				if attrId in attrs.keys():
					self.a48=str(attrs[attrId].value)
		
				attrId='a49'
				if attrId in attrs.keys():
					self.a49=str(attrs[attrId].value)
		
				attrId='a62'
				if attrId in attrs.keys():
					self.a62=str(attrs[attrId].value)
		
				attrId='a63'
				if attrId in attrs.keys():
					self.a63=str(attrs[attrId].value)
		
				attrId='a61'
				if attrId in attrs.keys():
					self.a61=str(attrs[attrId].value)
		
		
		
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
		string=self.addToXmlString(self.a5,'a5',string)
		string=self.addToXmlString(self.a4,'a4',string)
		string=self.addToXmlString(self.a7,'a7',string)
		string=self.addToXmlString(self.a6,'a6',string)
		string=self.addToXmlString(self.a8,'a8',string)
		string=self.addToXmlString(self.a20,'a20',string)
		string=self.addToXmlString(self.a21,'a21',string)
		string=self.addToXmlString(self.a22,'a22',string)
		string=self.addToXmlString(self.a23,'a23',string)
		string=self.addToXmlString(self.a24,'a24',string)
		string=self.addToXmlString(self.a25,'a25',string)
		string=self.addToXmlString(self.a26,'a26',string)
		string=self.addToXmlString(self.a27,'a27',string)
		string=self.addToXmlString(self.a28,'a28',string)
		string=self.addToXmlString(self.a29,'a29',string)
		string=self.addToXmlString(self.a31,'a31',string)
		string=self.addToXmlString(self.a30,'a30',string)
		string=self.addToXmlString(self.a15,'a15',string)
		string=self.addToXmlString(self.a14,'a14',string)
		string=self.addToXmlString(self.a17,'a17',string)
		string=self.addToXmlString(self.a16,'a16',string)
		string=self.addToXmlString(self.a11,'a11',string)
		string=self.addToXmlString(self.a10,'a10',string)
		string=self.addToXmlString(self.a13,'a13',string)
		string=self.addToXmlString(self.a12,'a12',string)
		string=self.addToXmlString(self.a19,'a19',string)
		string=self.addToXmlString(self.a18,'a18',string)
		string=self.addToXmlString(self.a9,'a9',string)
		string=self.addToXmlString(self.a60,'a60',string)
		string=self.addToXmlString(self.a37,'a37',string)
		string=self.addToXmlString(self.a36,'a36',string)
		string=self.addToXmlString(self.a33,'a33',string)
		string=self.addToXmlString(self.a35,'a35',string)
		string=self.addToXmlString(self.a34,'a34',string)
		string=self.addToXmlString(self.a51,'a51',string)
		string=self.addToXmlString(self.a50,'a50',string)
		string=self.addToXmlString(self.a53,'a53',string)
		string=self.addToXmlString(self.a52,'a52',string)
		string=self.addToXmlString(self.a55,'a55',string)
		string=self.addToXmlString(self.a54,'a54',string)
		string=self.addToXmlString(self.a57,'a57',string)
		string=self.addToXmlString(self.a56,'a56',string)
		string=self.addToXmlString(self.a59,'a59',string)
		string=self.addToXmlString(self.a58,'a58',string)
		string=self.addToXmlString(self.a32,'a32',string)
		string=self.addToXmlString(self.a39,'a39',string)
		string=self.addToXmlString(self.a38,'a38',string)
		string=self.addToXmlString(self.a46,'a46',string)
		string=self.addToXmlString(self.a47,'a47',string)
		string=self.addToXmlString(self.a44,'a44',string)
		string=self.addToXmlString(self.a45,'a45',string)
		string=self.addToXmlString(self.a42,'a42',string)
		string=self.addToXmlString(self.a43,'a43',string)
		string=self.addToXmlString(self.a40,'a40',string)
		string=self.addToXmlString(self.a41,'a41',string)
		string=self.addToXmlString(self.a48,'a48',string)
		string=self.addToXmlString(self.a49,'a49',string)
		string=self.addToXmlString(self.a62,'a62',string)
		string=self.addToXmlString(self.a63,'a63',string)
		string=self.addToXmlString(self.a61,'a61',string)
		if self._text==None:
			string+='/>'
		else:
			string+='>'+self._text+'</'+self.moduleName+'>'
		outFile.write(indent+string+'\n')
		
