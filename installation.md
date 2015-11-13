1. grab a copy of the software:

  * You can pull a copy from github: https://github.com/theRealZing/Liber-Abaci.git

  * If you use git, a pull request will create the directory Liber-Abaci

  * If you download a ZIP file - unpack the files


2. make sure you have python 2.7 installed:

  * $python --version
  * Python 2.7.10

3. make sure you have a current Flask installed:

  * $sudo pip install Flask

4. cd to Liber-Abaci/fib-api and run the unit tests:

  * $cd Liber-Abaci
  * $cd fib-api
  * $ python -m unittest discover .
  <blockquote>
.....................................
----------------------------------------------------------------------
Ran 37 tests in 1.299s

OK
  </blockquote>

5. The code has debug set by default - edit the last two lines (use one or the other) of server1.py to 
   either enable/disable debug mode.

6. Now you can run the server.  It runs on port 5000.

  * $nohup python server1.py | tee server.log

7. you can interact with the API uing jsonium or postman or just a web browser.  Type the following into a browser:

  * http://hostname:5000/

you should get a response similar to this:
{"uri":"/","request type":"GET","description":"Welcome to Blair's Fibonacci API","version":"0.1","status":"ok","result":"none","start":"2015-11-13 08:14:10.173586","finish":"2015-11-13 08:14:10.173614"}
