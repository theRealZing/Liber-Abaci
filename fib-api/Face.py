'''

 @author: Blair Elzinga
 create date: Nov 11, 2015

 module description:This module defines the format of the API messages,
 separating form from function

 This is of course overly verbose for a simple Fibonacci API, but I did
 it this way to make the API more fitting for something that would be longer
 term and have clients that perhaps were reading these off of an ESB...

'''
import datetime
import Stats
import json

class Face:
  def __init__(self, app, uri, reqType, desc, status='ok', result='"none"'):
    stime=datetime.datetime.now()
    self.app = app
    self.version = "0.1"
    self.uri = uri
    self.reqType = reqType
    self.description = desc
    self.status = status
    self.result = result
    self.start = str(stime)
    app.start(self.uri,stime) #update stats for this call

  def listToJson(self,inputList):
    return json.dumps(inputList)

  def dictionaryToJson(self,inputDictionary):
    return json.dumps(inputDictionary)

  def response(self,app,status,result):
    if status is not None: self.status = status
    if result is not None: self.result = result
    ftime=datetime.datetime.now()
    app.finish(self.uri,ftime,self.status)
    out = '{"uri":"'+self.uri+'"'
    out += ',"request type":"'+self.reqType+'"'
    out += ',"description":"'+self.description+'"'
    out += ',"version":"'+self.version+'"'
    out += ',"status":"'+self.status+'"'
    out += ',"result":'+self.result
    out += ',"start":"'+self.start+'"'
    out += ',"finish":"'+str(ftime)+'"'
    out += "}"
    return str(out)
