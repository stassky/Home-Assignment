from elasticsearch import Elasticsearch
import getpass
import datetime
es = Elasticsearch(['localhost'],port=9200)
print( "user`s name is: ", getpass.getuser())
print("time is now is :", (datetime.datetime.now()))
