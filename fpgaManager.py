import types
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, String, Integer, DateTime, PickleType
import os
from threading import Thread
from threading import Lock
import time

class Fpga():

	def __init__(self):
		self.fd = None
		self.subclasses=list()
		self.allClass = dict()
		self.allClassName = list()
		self.i=0
		self.perc=0
		self.totalNumLines=0

	def __analizeXml(self,root):
		while 1:
			line = self.fd.readline()
			if self.i/(self.totalNumLines/100) == 1:
				self.perc += 1
				self.i=0	
				print str(self.perc)+"%"
			self.i+=1
			if not line:
				return
			words = line.split()
			if words[0][0] == '<':
				if words[0][1] != '/' and words[0][1] != '?' and words[0][1] != '!':

					if words[0][1:] in self.allClassName:
						t = (self.allClass[words[0][1:]])()
#					if words[0][1:] == 'xdl_resource_report':
#						self.board = words[2].split('"')[1]
					list_att = list()
					list_val = list()
					for w in words[1:-1]:
						a = w.split('=')[0]
						v = w.split('"')[1]
						if words[0][1:] in self.allClassName:
							t.__dict__[a]=v
						else:
							list_att.append(a)
							list_val.append(v)

					# if not exist create class in self.allClass with type()
					if words[0][1:] not in self.allClassName:
						dic_att = {'__tablename__':words[0][1:],'id':Column(Integer,primary_key=True),'board':Column(String)}
						dic_att['idFather'] = Column(Integer)
						dic_att['fatherType'] = Column(String)
						for att in list_att:
							dic_att[att] = Column(String)
						dic_att['subClasses'] = None
						dic_att['father'] = None
						self.allClassName.append(words[0][1:])
						self.allClass[words[0][1:]] = type(words[0][1:],(self.Base,),dic_att)
						self.Base.metadata.create_all()
						#create an instance of class with attrs and methods
						self.currentIdClass[(words[0][1:])] = 0
						t = (self.allClass[words[0][1:]])()
						for a, v in zip(list_att,list_val):
							t.__dict__[a]=v
#					t.__dict__['board'] = self.board
					t.__dict__['board'] = self.fpgaName
					t.__dict__['idFather'] = self.currentIdClass[root.__class__.__name__]
					t.__dict__['fatherType'] = root.__class__.__name__
					self.lock.acquire()
					self.session.add(t)
					self.lock.release()
					self.currentIdClass[t.__class__.__name__] += 1
					if words[-1][-1] == '>' and len(words[-1])==1:
						# continue with depth search
						self.__analizeXml(t)
						continue
					else:
						# continue with breadth search
						continue
				elif words[0][1] == '/':
					return
				else:
					continue

	def __createDbFromXml(self,speed=1,dbCreated=False):
		self.lock = Lock()
		self.i=0
		self.perc=0
		self.currentIdClass = {self.__class__.__name__ : 0}
		if dbCreated:
			for cn in self.allClassName:
				self.currentIdClass[cn] = self.session.query(self.allClass[cn]).count()
		try:
			self.fd = open(self.xmlFilename,"r")
			num=0
			while 1:
				if not self.fd.readline():
					break
				num+=1
			self.totalNumLines = num
			self.fd.close()
			self.fd = open(self.xmlFilename,"r")
		except	IOError as e:
			print "error: impossible to open file " + "\""+e.filename+"\""
			return False
		print str(self.perc)+"% loading..."
		t = Thread(target=self.__analizeXml, args=[self])
		t.start()
#		self.__analize()
		while t.isAlive():
			time.sleep(speed)
			self.lock.acquire()
			self.session.commit()
			self.lock.release()
		if not dbCreated:
			BoardList = type('boardList', (self.Base,), {'__tablename__':'boardList','id':Column(Integer,primary_key=True),'board':Column(String)})
			TableList = type('tableList', (self.Base,), {'__tablename__':'tableList','id':Column(Integer,primary_key=True),'name':Column(String)})
			self.Base.metadata.create_all()
			boardList = BoardList()
#			boardList.board = self.board
#			self.boardList = [self.board]
			boardList.board = self.fpgaName
			self.boardList = [self.fpgaName]
			for c in self.allClassName:
				tableList = TableList()
				tableList.name = c
				self.session.add(tableList)
			self.session.add(boardList)
		else:
			boardList = self.allClass['boardList']()
			boardList.board = self.fpgaName
#			self.boardList.append(self.board)
			self.boardList.append(self.fpgaName)
			self.session.add(boardList)
		self.session.commit()
		self.fd.close()
		return True

	def __loadTablesFromDb(self):
		boardList = type('boardList',(self.Base,),{'__table__': Table('boardList', self.Base.metadata, autoload=True, autoload_with=self.engine)})
		tableList = type('tableList',(self.Base,),{'__table__': Table('tableList', self.Base.metadata, autoload=True, autoload_with=self.engine)})
		self.Base.metadata.create_all()
		self.allClass['boardList'] = boardList
		for k in self.session.query(tableList):
			self.allClassName.append(k.name)
			self.allClass[k.name] = type(str(k.name),(self.Base,),{'__table__' : Table(k.name, self.Base.metadata, autoload=True, autoload_with=self.engine),'subClasses':None,'father':None})
		self.boardList = list()
		for b in self.session.query(boardList):
			self.boardList.append(b.board)
		self.Base.metadata.create_all()

	def __open_db(self,dbCreated=True):
		self.Base=declarative_base()
		self.engine=create_engine("sqlite:///"+self.dbName)
		self.Base.metadata.bind=self.engine
		self.Session=sessionmaker(bind=self.engine)
		self.session=self.Session()
		if not dbCreated:
			# generate xdlrc
			if (not os.path.exists(self.xdlrcName)):
				os.system("xdl -report "+ self.fpgaName)
				os.system("mv *.xdlrc inputs/")			
			if (not os.path.exists(self.xmlFilename)):
				os.system("python scripts/xdlrc2xml.py inputs/"+self.fpgaName+".xdlrc")
			self.__createDbFromXml(dbCreated=False)
		else:
			self.__loadTablesFromDb()
		if not self.fpgaName in self.boardList:
			print "fpgaName not in boardList, loading from xml file"
			# generate xdlrc
			if (not os.path.exists(self.xdlrcName)):
				os.system("xdl -report "+ self.fpgaName)
				os.system("mv *.xdlrc inputs/")
			if (not os.path.exists(self.xmlFilename)):
				os.system("python scripts/xdlrc2xml.py inputs/"+self.fpgaName+".xdlrc")
			self.__createDbFromXml(dbCreated=True)

	def loadFpga(self,fpgaName):
		self.fpgaName = fpgaName
		self.dbName = "fpgaDb/fpgaDb.db"
		self.xdlrcName = "inputs/" + fpgaName + ".xdlrc"
		self.xmlFilename = "inputs/" + fpgaName + ".xml"
		if (not os.path.exists(self.dbName)):
  			f=open(self.dbName,"w");
  			f.close()
			self.__open_db(dbCreated=False)
		else:
			self.__open_db()
		os.system("rm inputs/*.xdlrc inputs/*.xml")

	def __selectOnDb(self, table_name, conditions):
		return self.session.query(self.allClass[table_name]).filter(*conditions)

	def getTileByXY(self,x,y):
		return self.__selectOnDb('tile',[self.allClass['tile'].x==x, self.allClass['tile'].y==y, self.allClass['tile'].board==self.fpgaName]).first()

	def addSubClasses(self,objClass):
		children = list()
		for t in self.allClassName:			
			children += self.__selectOnDb(t,[self.allClass[t].idFather==objClass.id, self.allClass[t].fatherType==objClass.__class__.__name__, self.allClass[t].board==self.fpgaName]).all()
		objClass.subClasses = children
		return

	def addFather(self, objClass):
		father = self.__selectOnDb(objClass.fatherType,[self.allClass[objClass.fatherType].id==objClass.idFather,self.allClass[objClass.fatherType].board==self.fpgaName]).first()
		objClass.father = father
		return


