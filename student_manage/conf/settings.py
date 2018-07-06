import os,sys
BASE= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASE)

db_file = '%s/%s/%s'%(BASE,'db','user.json')
# print(db_file)