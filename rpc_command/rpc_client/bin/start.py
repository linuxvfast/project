import os,sys
BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASE_DIR)
from core.client import FibonacciRpcClient
# print(sys.argv[0])
if __name__ == '__main__':
    start = FibonacciRpcClient()
    start.interactive()