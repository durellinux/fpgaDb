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
class FpgaResource(Base):
  __tablename__="fpga_resource"
  id=Column(Integer,primary_key=True)
  model=Column(String)
  version=Column(String)
  speedGrade=Column(String)
  tileX=Column(Integer)
  tileY=Column(Integer)
  x=Column(Integer)
  y=Column(Integer)
  type=Column(String)
######################

Base.metadata.create_all()

Session=sessionmaker(bind=engine)
session=Session()


# Queries
#######################
def getFpgaResourceByPositionType(model,version,speedGrade,tileX,tileY,type):
  r = session.query(FpgaResource).filter(FpgaResource.model==model and FpgaResource.version==version and FpgaResource.speedGrade==speedGrade and FpgaResource.tileX==tileX and FpgaResource.tileY==tileY and FpgaResource.type==type).first()
  return r

def addResource(model,version,speedGrade,tileX,tileY,x,y,type):
  r = getFileByHashByPath(model,version,speedGrade,tileX,tileY,type)

  if r==None:
    r=FpgaResource()
    r.model=model
    r.version=version
    r.speedGrade=speedGrade
    r.tileX=tileX
    r.tileY=tileY
    r.x=x
    r.y=y
    r.type=type

    session.add(r)
    session.commit()

  return r
##########################