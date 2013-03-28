#
#
# Written by Gianluca Durelli
#
#

from pprint import pprint

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, DateTime, PickleType

from uuid import uuid4

import datetime
import time

import os

dbName="fpgaDb.db"

if (not os.path.exists(dbName)):
  f=open(dbName,"w");
  f.close()

Base=declarative_base()
engine=create_engine("sqlite:///"+dbName)
Base.metadata.bind=engine

#Table description
#####################
class Docs(Base):
  __tablename__="docs"
  hashed=Column(String,primary_key=True)
  txt=Column(String)

class Files(Base):
  __tablename__="files"
  hashed=Column(String,primary_key=True)
  name=Column(String)
  path=Column(String)

class Lables(Base):
  __tablename__="labels"
  id=Column(Integer,primary_key=True)
  hashed=Column(String)
  label=Column(String)
######################

Base.metadata.create_all()

Session=sessionmaker(bind=engine)
session=Session()


# Queries
#######################
def getDocByHash(hashed):
  d = session.query(Docs).filter(Docs.hashed==hashed).first()
  return d

def getFileListByHash(hashed):
  f = session.query(Files).filter(Files.hashed==hashed).all()
  return f

def getFileByHashByPath(hashed,path):
  f = session.query(Files).filter(Files.hashed==hashed and Files.path==path).first()
  return f

def addFile(hashed,fileName,filePath):
  f = getFileByHashByPath(hashed,filePath)

  if f==None:
    f=Files()
    f.hashed=hashed
    f.name=fileName
    f.path=filePath
    session.add(f)
    session.commit()

  return f

def addDoc(hashed,txt,fileName,filePath):
  doc=getDocByHash(hashed)

  if doc==None:
    doc=Docs()
    doc.hashed=hashed
    doc.txt=txt
    session.add(doc)
    session.commit()

  addFile(hashed,fileName,filePath)

  return doc

def findDocList(queryTxt):
  docList=session.query(Docs).filter(Docs.txt.contains(queryTxt)).all()

  files=list()

  for d in docList:
    f=getFileListByHash(d.hashed)
    files.append(f)

  return files
  ##########################