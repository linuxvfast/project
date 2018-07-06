import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
sys.path.append(BASE_DIR)

ACCOUNT_DIR = '%s/%s/%s'%(BASE_DIR,'conf','account.cfg')
# print(ACCOUNT_DIR)