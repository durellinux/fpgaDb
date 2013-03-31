import os
import sys

# Importing db class: it will create the db
import db

#Import xml minidom parse
from xml.dom.minidom import parse

# Appending parser directory to path
sys.path.append("./xdlrcParser/python")
from xdl_resource_report import xdl_resource_report

xmlFileIn="inputs/sample.xml"

xml=open(xmlFileIn,"r")
dom=parse(xml)
xml.close()

xdlrcClass=xdl_resource_report()
xdlrcClass.loadXml(dom)

tiles=xdlrcClass.getByAttrValues("tile",[])

print "Tiles number: "+str(len(tiles))
for t in tiles:
	print t.get_a0()+"\t"+t.get_a1()+"\t"+t.get_a2()
	primitives=t.getByAttrValues("primitive_site",[])
	for p in primitives:
		print "\t"+p.get_a0()+"\t"+p.get_a1()