#Andrew Seak
#5/5/2019
#Used for easy storage and retrieval of quotes from a JSON file

import random
import json
import os
from datetime import datetime

'''
quotes.newfile(directory, name): Used to create a new JSON file for quotes
    file = quotes.newfile('quotes/', 'newquotesfile')
quotes.addquote(file, quote, description=): Adds a quote to a JSON file
    quotes.addquote('quotes/newquotesfile.json', 'quote')
'''

def newfile(directory, name):
    file = open(directory+name+".json", "w+")
    file.write("{\"quotes\": []}")
    file.close()
    return file

def addquote(file, quote, description="Added "+ str(datetime.now().date())):
    if os.path.exists(file):
        data = None
        with open(file, "r+") as content:
            data = json.load(content)
            data["quotes"].append({"quote": quote, "desc": description})
        open(file, "w").close()
        json.dump(data, open(file, "r+"))
        return len(data["quotes"])

def delquote(file, index):
    if os.path.exists(file):
        data = None
        with open(file, "r+") as content:
            data = json.load(content)
            data["quotes"][index] = None
        open(file, "w").close()
        json.dump(data, open(file, "r+"))

def randomquote(file):
    if os.path.exists(file):
        with open(file, "r+") as content:
            data = json.load(content)
            length = len(data["quotes"])
            return data["quotes"][random.randint(0, length-1)]

def getquote(file, index):
    if os.path.exists(file):
        with open(file, "r+") as content:
            data = json.load(content)
            return data["quotes"][index-1]

def getquotes(file, index):
    if os.path.exists(file):
        with open(file, "r+") as content:
            return json.load(content)
