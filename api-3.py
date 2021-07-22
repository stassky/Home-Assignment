from flask import Flask
from flask_restful import Resource, Api, reqparse
# import pandas as pd
import requests, json, os
from datetime import datetime
from elasticsearch import Elasticsearch
import getpass
es = Elasticsearch(['localhost'],port=9200)      # server's IP address
userName = print("user`s name is: ", getpass.getuser())
userName


app = Flask(__name__)
api = Api(app)

class places(Resource):
    def get(self):
        data = pd.read_csv('places.csv')  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code

api.add_resource(places, '/tracking')  # '/tracking' is our entry point

if __name__ == '__main__':
    app.run()  # run our Flask app

