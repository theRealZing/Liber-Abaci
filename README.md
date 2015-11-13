# Liber-Abaci
An example web service that deals with Fibonacci sequence as a sample purpose.

##purpose of this repository
This repository is being created as a sample of my design thinking, orgainization, and some programming.  It isn't meant to break any new ground mathematically.  The main purpose is to create a simple API and flesh it out a bit, as if it were being done for commercial use - except the licensing of this exercise may not be appropriate for a commercial venture.

## history
"Liber Abaci", or Book of Calculation was written in 1202 by Leonardo Pisano Bigollo, also known as Leonardo Bonacci or more popularly just Fibonacci.  This book is one way that the famous sequence was introduced to Europe. (reference: wikipedia "Fibonacci")
<p>
Note that the sequence as introduced only works on positive integers (including zero) and is usually thought of that way; but mathematically it can operate on negative numbers as well.  </p>
<p>
Another branch from the original is to specify any two starting integers and then following the same basic algorithm.  I probably won't venture there. </p>

##the stack
At the outset, the entire stack is flexible and subject to change.  Here are my initial thoughts:
* python is a great choice to actually generate the Fibonacci sequence numbers since it has built-in support for very large integers.
* Originally I toyed with doing the API in Node.js/express, However, since it would also be instructive to use python for the API, I chose to use python along with the "micro-framework" flask for defining the API routes.

##the vision
###more than just Fibonacci sequences
Not only provide something that can generate Fibonacci sequences, but also values in the sequence, and well as floor() and ceiling functions which provide the sequence below or above a non-Fibonacci number.
###built-in functional and performance comparisons of library vs library!
The user can ask for functional tests of the Fibonacci libraries as well as comparative performance measurements.
###dynamic code loading allow easy addition of new libraries!
The Fibonacci libraries are dynamically loaded, which means that a person can develop a new library and add it to the mix without changing any API code.
###API health check and status call
The API also tracks status on the calls used and can report on that through the status API.
###running server is available for your use!
A working server is running and available on the internet.  I'll provide the web address in my email response.

## the API
<p>The API responses are all wrapped in JSON, ready for ingestion by some future enterprise bus or client front-end.</p>
<p>There are three Fibonacci libraries available to use through the API, as well as compare results and performance of.  These are:</p>
### LoopFib
Uses a for-loop and simple list storage for performance improvement of subsequent calls.  Produces accurate large numbers.
### TableFib
Uses limited recursion along with simple list storage to avoid deep recursion. Fairly fast but can still get itself into stack trouble with large sequences.
### GoldFib
Uses an approximation of the golden ratio to directly estimate any given number in the Fibonacci sequence.  However, since it is an approximation method, the accuracy drops off as n increases.  Fastest at calculating a single number out of sequence, but otherwise isn't that great due to rounding issues.
<p>My liber-abaci resource will use HTTP methods as follows:</p>
<table class="data">
<tr><th>HTTP Method</th><th>URI</th><th>Action</th></tr>
<tr><td>GET</td><td>http://[hostname]/apiList</td><td>Retrieve list of api calls</td></tr>
<tr><td>GET</td><td>http://[hostname]/status</td><td>Health check and operational stats</td></tr>
<tr><td>GET</td><td>http://[hostname]/fibSequence/[method]/[n]</td><td>Retrieve a Fibonacci sequence of length n using the specified method</td></tr>
<tr><td>GET</td><td>http://[hostname]/fibValue/[method]/[n]</td><td>Retrieve the value of the Fibonacci sequence at step n using the specified method</td></tr>
<tr><td>GET</td><td>http://[hostname]/fibFloor/[method]/[n]</td><td>Retrieve the values of the Fibonacci sequence lower than n</td></tr>
<tr><td>GET</td><td>http://[hostname]/fibCeiling/[method]/[n]</td><td>Retrieve the values of the Fibonacci sequence higher than n</td></tr>
<tr><td>GET</td><td>http://[hostname]/userMethods/</td><td>List the Fibonacci libraries available for use.  Create your own Fibonacci routines and compare it with mine!</td></tr>
<tr><td>GET</td><td>http://[hostname]/test/[method1,method2]/</td><td>Compare two fibonacci methods for generating a sequence of n items on several tests, including performance runs</td></tr>
</table>

## installation
See the separate install instructions and API examples
