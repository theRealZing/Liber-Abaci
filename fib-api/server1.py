'''

 @author: Blair Elzinga
 create date: Nov 11, 2015

 module description:

'''

from flask import Flask, url_for, request
from Face import Face
from Stats import Stats
from FuncTest import FuncTest
from UserLib import UserLib

app = Flask(__name__)
appStats = Stats()
libs = UserLib()

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

@app.route('/')
def root():
    apiFace = Face(appStats,'/',request.method,"Welcome to Blair's Fibonacci API")
    return apiFace.response(appStats,None,None)

@app.route('/status/')
def status():
    apiFace = Face(appStats,'/status/',request.method,"health check")
    print url_for('status')
    #return status and result
    return apiFace.response(appStats,'healthy',apiFace.dictionaryToJson(appStats.getStats()))

@app.route('/apiList/')
def apiList():
    apiFace = Face(appStats,'/apiList/',request.method,"List of available API endpoints")
    links = []
    for rule in app.url_map.iter_rules():
      if rule.endpoint != 'static': links.append(rule.endpoint)
    return apiFace.response(appStats,'Pass',apiFace.listToJson(sorted(links)))

@app.route('/fibSequence/<fibMethod>/<fibLen>')
def fibSequence(fibMethod,fibLen):
    apiFace = Face(appStats,'/sequence/'+fibMethod,request.method,'Generate a Fibonacci sequence with '+fibLen+' elements using method '+fibMethod)
    if int(fibLen) < 0:
      return apiFace.response(appStats,'Fail',"API does not allow negative length")
    try:
      methodLoad = __import__(fibMethod)
      dynLoad = 'methodLoad.'+fibMethod+'()'
      fib = eval(dynLoad)
      list1 =  fib.fibList(int(fibLen))
    except:
      return apiFace.response(appStats,'Fail',fibMethod+' returned an error')
    else:
      return apiFace.response(appStats,'Pass',apiFace.listToJson(list1))

@app.route('/fibValue/<fibMethod>/<fibItem>')
def fibValue(fibMethod,fibItem):
    apiFace = Face(appStats,'/value/'+fibMethod,request.method,'Generate a Fibonacci number at sequence '+fibItem+' using method '+fibMethod)
    if int(fibItem) < 0:
      return apiFace.response(appStats,'Fail',"API does not support negative sequence values")
    try:
      methodLoad = __import__(fibMethod)
      dynLoad = 'methodLoad.'+fibMethod+'()'
      fib = eval(dynLoad)
      fibValue =  fib.fibAtN(int(fibItem))
    except:
      return apiFace.response(appStats,'Fail',fibMethod+' returned an error')
    else:
      return apiFace.response(appStats,'Pass',str(fibValue))

@app.route('/fibFloor/<fibMethod>/<fibItem>')
def fibFloor(fibMethod,fibItem):
    apiFace = Face(appStats,'/floor/'+fibMethod,request.method,'Generate a Fibonacci sequence with max value less than '+fibItem+' using method '+fibMethod)
    if int(fibItem) < 0:
      return apiFace.response(appStats,'Fail',"API does not support negative target values")
    try:
      methodLoad = __import__(fibMethod)
      dynLoad = 'methodLoad.'+fibMethod+'()'
      fib = eval(dynLoad)
      list1 =  fib.fibFloor(int(fibItem))
    except:
      return apiFace.response(appStats,'Fail',fibMethod+' returned an error')
    else:
      return apiFace.response(appStats,'Pass',apiFace.listToJson(list1))

@app.route('/fibCeiling/<fibMethod>/<fibItem>')
def fibCeiling(fibMethod,fibItem):
    apiFace = Face(appStats,'/ceiling/'+fibMethod,request.method,'Generate a Fibonacci sequence with max value one sequence item higher than '+fibItem+' using method '+fibMethod)
    if int(fibItem) < 0:
      return apiFace.response(appStats,'Pass',apiFace.listToJson([0]))
    try:
      methodLoad = __import__(fibMethod)
      dynLoad = 'methodLoad.'+fibMethod+'()'
      fib = eval(dynLoad)
      list1 =  fib.fibCeil(int(fibItem))
    except:
      return apiFace.response(appStats,'Fail',fibMethod+' returned an error')
    else:
      return apiFace.response(appStats,'Pass',apiFace.listToJson(list1))


@app.route('/userMethods', methods=['GET','PUT','POST','DELETE'])
def userMethods():
    if request.method == 'GET':
        response='list user methods'
        apiFace = Face(appStats,'/userMethods/',request.method,'list Fibonacci libraries available')
        return apiFace.response(appStats,'Pass',apiFace.dictionaryToJson(libs.list()))
    elif request.method == 'PUT':
        response='update user method'
        apiFace = Face(appStats,'/userMethods/',request.method,'update Fibonacci libraries available')
    elif request.method == 'POST':
        response='create user method'
        apiFace = Face(appStats,'/userMethods/',request.method,'create Fibonacci libraries available')
        #libs.add('TableFib','limited recursion with simple storage')
    elif request.method == 'DELETE':
        response='drop user method'
        apiFace = Face(appStats,'/userMethods/',request.method,'drop Fibonacci libraries available')

    return apiFace.response(appStats,'Fail','not supported:'+response)

@app.route('/test/<fibMethod1>/<fibMethod2>')
def test(fibMethod1,fibMethod2):
    apiFace = Face(appStats,'/test/'+fibMethod1+'/'+fibMethod2,request.method,'Compare library '+fibMethod2+' to '+fibMethod1)
    appTests = FuncTest()
    lib1 = appTests.getStandardDictionary()
    lib2 = appTests.getTestDictionary()
    appTests.runLibraryTests(fibMethod1,lib1)
    appTests.runLibraryTests(fibMethod2,lib2)
    testResults = appTests.compare()
    if appTests.testsPassed() == True: overall = "Pass"
    else: overall = "Fail"
    return apiFace.response(appStats,overall,apiFace.dictionaryToJson(sorted(testResults.iteritems())))

@app.errorhandler(400)
def bad_request(error=None):
  apiFace = Face(appStats,'400 Error',request.method,'malformed request')
  return apiFace.response(appStats,"Error",'400')

@app.errorhandler(401)
def unauthorized(error=None):
  apiFace = Face(appStats,'401 Error',request.method,'user is not authorized')
  return apiFace.response(appStats,"Error",'401')

@app.errorhandler(403)
def forbidden(error=None):
  apiFace = Face(appStats,'401 Error',request.method,'user is not allowed to access the resource')
  return apiFace.response(appStats,"Error",'403')

@app.errorhandler(404)
def not_found(error=None):
  apiFace = Face(appStats,'404 Error',request.method,'URL not found')
  links = []
  for rule in app.url_map.iter_rules():
    if rule.endpoint != 'static': links.append(rule.endpoint)
  return apiFace.response(appStats,'401 Error',apiFace.listToJson(sorted(links)))

@app.errorhandler(405)
def wrong_method(error=None):
  apiFace = Face(appStats,'405 Error',request.method,'request type not allowed')
  return apiFace.response(appStats,"Error",'405')

@app.errorhandler(500)
def runtime_error(error=None):
  apiFace = Face(appStats,'500 Error',request.method,'python runtime error encountered, see server output')
  return apiFace.response(appStats,"Error",'500')

if __name__ == '__main__':
    libs.add('TableFib','limited recursion with simple storage')
    libs.add('LoopFib','For-loop addition with simple storage')
    libs.add('GoldFib','Approximation using the Golden Ratio')
    app.run(host='0.0.0.0', debug=True)
    #app.run(host='0.0.0.0')
