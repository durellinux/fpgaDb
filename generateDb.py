import os
import sys



############################################################################
# Preprocessing: Creating needed files

#TODO execute command to export boards
# Change os.system to Popen/Popen3

os.system("python ./scripts/parser_boards.py ./inputs/boards")


###################
# Generate Parser #
###################

os.system("python ./scripts/xdlrc2xml.py inputs/sample.xdlrc")

#Set to the proper path (read from config file)
pyParseCmd="~/Projects/others/pyParse/pyparse.py"
os.system("python "+pyParseCmd+" inputs/sample xml xdl_resource_report")
os.system("cp inputs/sample/* ./xdlrcParser/ -R")
os.system("rm inputs/sample -rf")

############################################################################


# Appending parser directory to path
sys.path.append("./xdlrcParser/python")

# Importing db class: it will create the db
import db


