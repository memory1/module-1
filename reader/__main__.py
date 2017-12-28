print("execute __main__.py with name {}".format(__name__))
import sys
from reader import Reader
r = Reader(sys.argv[1])
try:
    print(r.read())
finally:
    r.close()