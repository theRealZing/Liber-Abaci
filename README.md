# Liber-Abaci
An example web service that deals with Fibonacci sequence as a sample purpose.
## history
"Liber Abaci", or Book of Calculation was written in 1202 by Leonardo Pisano Bigollo, also known as Leonardo Bonacci or more popularly just Fibonacci.  This book is one way that the famous sequence was introduced to Europe. (reference: wikipedia "Fibonacci")
<p>
Note that the sequence as introduced only works on positive integers (including zero) and is usually thought of that way; but mathematically it can operate on negative numbers as well.  </p>
<p>
Another branch from the original is to specify any two starting integers and then following the same basic algorithm.  I probably won't venture there. </p>
## purpose of this repository
This repository is being created as a sample of my programming.  It isn't meant to break any new ground mathematically.  The main purpose is to create a simple API and flesh it out a bit, as if it were being done for commercial use - except the licensing of this exercise may not be appropriate for a commercial venture.
## the stack
<p>
At the outset, the entire stack is flexible and subject to change.  Here are my initial thoughts:
* python is a great choice to actually generate the Fibonacci sequence numbers since it has built-in support for very large integers.
* I've been teaching myself express/node.js recently, and it seems like a natural choice for creating a simple API.
* However, it would also be instructive to use python for the API, so  I'll probably do both at first to get a feel for which I like better for this case.
</p>
## the API

<p>My liber-abaci resource will use HTTP methods as follows:</p>
<table class="data">
<tr><th>HTTP Method</th><th>URI</th><th>Action</th></tr>
<tr><td>GET</td><td>http://[hostname]/liber-abaci/[stack]/v0.1/apiList</td><td>Retrieve list of api calls, including user methods</td></tr>
<tr><td>GET</td><td>http://[hostname]/liber-abaci/[stack]/v0.1/status</td><td>Health check and operational stats</td></tr>

<tr><td>GET</td><td>http://[hostname]/liber-abaci/[stack]/v0.1/sequence/[method]/[n]</td><td>Retrieve a Fibonacci sequence of length n using the specified method</td></tr>
<tr><td>GET</td><td>http://[hostname]/liber-abaci/[stack]/v0.1/value/[method]/[n]</td><td>Retrieve the value of the Fibonacci sequence at step n using the specified method</td></tr>
<tr><td>GET</td><td>http://[hostname]/liber-abaci/[stack]/v0.1/floor/[method]/[n]</td><td>Retrieve the value of the Fibonacci sequence lower than n</td></tr>
<tr><td>GET</td><td>http://[hostname]/liber-abaci/[stack]/v0.1/ceiling/[method]/[n]</td><td>Retrieve the value of the Fibonacci sequence higher than n</td></tr>
<tr><td>POST</td><td>http://[hostname]/liber-abaci/[stack]/v0.1/create/[method]</td><td>Create your own fibonacci routine and compare it with mine!</td></tr>
<tr><td>GET</td><td>http://[hostname]/liber-abaci/[stack]/v0.1/test/[method1,method2]/[n]</td><td>Compare two fibonacci methods for generating a sequence of n items</td></tr>
<tr><td>GET</td><td>http://[hostname]/liber-abaci/[stack]/v0.1/timer/[method1,method2]/[n]</td><td>Compare speed of two fibonacci methods for generating a sequence of n items</td></tr>
<tr><td>DELETE</td><td>http://[hostname]/liber-abaci/[stack]/v0.1/delete/[method]</td><td>Delete a user-defined Fibonacci routine</td></tr>
<tr><td>PUT</td><td>http://[hostname]/liber-abaci/[stack]/v0.1/update/[method]</td><td>Update an existing user-defined Fibonacci routine</td></tr>
</table>

##Fibonacci methods
The built-in methods available will be the following:
* recursive: a poor choice for implementing Fibonacci sequence because it is slow and can overflow the call stack.
* loop: an order-N solution that is accurate.
* fast: a constant order (for a single value) solution that uses the golden ratio and rounding to produce a result.  Only accurate at lower ranges.
