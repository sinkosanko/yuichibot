#Andrew Seak
#5/5/2019
#Used for easy storage and retrieval of quotes from a JSON file

import random
import json
import os
from datetime import datetime
random.seed(datetime.now())

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
    if os.path.isfile(file):
        data = None
        with open(file, "r+") as content:
            data = json.load(content)
            data["quotes"].append({"quote": quote, "desc": description})
        open(file, "w").close()
        json.dump(data, open(file, "r+"))
        return len(data["quotes"])

def delquote(file, index):
    if os.path.isfile(file):
        data = None
        with open(file, "r+") as content:
            data = json.load(content)
            data["quotes"][index] = None
        open(file, "w").close()
        json.dump(data, open(file, "r+"))
        return index

def getquote(file, index):
    if os.path.isfile(file):
        with open(file, "r+") as content:
            data = json.load(content)
            return data["quotes"][index]

def getquotes(file):
    if os.path.isfile(file):
        with open(file, "r+") as content:
            return json.load(content)["quotes"]

def getnumberremoved(file):
    removed = 0
    if os.path.isfile(file):
        with open(file, "r+") as content:
            data = json.load(content)
            for quote in data["quotes"]:
                if quote == None:
                    removed += 1
            return removed

def getexistingquotes(file):
    if os.path.isfile(file):
        data = None
        with open(file, "r+") as content:
            data = json.load(content)["quotes"]
        if not data == None:
            return [i for i in data if i]
        return None

def randomquote(file):
    if os.path.isfile(file):
        data = getexistingquotes(file)
        if not len(data) == 0:
            length = len(data)
            return data[random.randint(0, length-1)]
        return None
